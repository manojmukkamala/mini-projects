# Raspberry Pi Spark Cluster — Setup Guide

A multi-node Apache Spark cluster running on Raspberry Pis, deployed with
Docker Compose.

## Topology

| Role | Node | Ports |
|---|---|---|
| Spark master | `rpi-node-01` | `7077` (scheduler), `8080` (UI) |
| Spark worker(s) | other Pi(s) | `8081` (worker UI) |
| Unity Catalog server | any node | `8081` (host) → `8080` (container) |
| RustFS object storage | any node | `9000` (S3 API), `9001` (console) |

Requirements:

- One Pi per role (master on `rpi-node-01`).
- Docker installed on **every** node (see step 1).
- Nodes must be able to resolve each other by hostname
  (`rpi-node-01`, ...). Add static entries to `/etc/hosts` on every node if
  you don't have DNS for the Pis.

## 1. Install Docker (on every node)

```sh
sudo apt update -y && sudo apt upgrade -y
sudo apt -y install lsb-release gnupg apt-transport-https ca-certificates curl
curl -fsSL https://download.docker.com/linux/debian/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker.gpg] https://download.docker.com/linux/debian trixie stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt update
sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin -y
```

Allow the current user to run Docker without `sudo`:

```sh
sudo usermod -aG docker ${USER}
newgrp docker
sudo systemctl is-active docker   # should print: active
```

> Note: `newgrp docker` only applies to the current shell. Log out and back
> in (or open a new terminal) for it to persist.

## 2. Start the Spark master (rpi-node-01)

Create `master.yml` on `rpi-node-01`:

```yaml
services:
  spark-master:
    image: spark:4.1.2
    command: /opt/spark/sbin/start-master.sh
    environment:
      - SPARK_NO_DAEMONIZE=true
    network_mode: host
```

Start it:

```sh
docker compose -f master.yml up -d
```

Check the master UI at `http://<rpi-node-01>:8080`.

## 3. Add Spark workers (other nodes)

Create `worker.yml` on each worker Pi:

```yaml
services:
  spark-worker:
    image: spark:4.1.2
    command: /opt/spark/sbin/start-worker.sh spark://rpi-node-01:7077
    environment:
      # Tune to the Pi's resources, e.g. for a 4 GB Pi:
      # - SPARK_WORKER_CORES=2
      # - SPARK_WORKER_MEMORY=3g
      - SPARK_NO_DAEMONIZE=true
    network_mode: host
    volumes:
      - /home/manoj/spark_cluster/work:/opt/spark/work
      # Optionally override defaults:
      # - ./spark-custom.conf:/opt/spark/conf/spark-defaults.conf:ro
```

Notes:

- With `network_mode: host` the worker UI is on the node itself at
  `http://<worker-ip>:8081` (no port mapping needed/used).
- Worker cores and memory are auto-detected by default — on small Pis you
  usually want to cap them so executors don't OOM the box.
- Create the working dir first: `mkdir -p /home/manoj/spark_cluster/work`.

Start the worker:

```sh
mkdir -p /home/manoj/spark_cluster/work
docker compose -f worker.yml up -d
```

The worker should appear on the master UI (`http://<rpi-node-01>:8080`)
within a few seconds.

## 4. Unity Catalog server (any node)

```yaml
services:
  uc-server:
    image: unitycatalog/unitycatalog:main-2f2e32d
    ports:
      - "8081:8080"
    volumes:
      - /home/manoj/unity_catalog/conf:/home/unitycatalog/etc/conf
      - /home/manoj/unity_catalog/data:/home/unitycatalog/etc/data
      - /home/manoj/unity_catalog/db:/home/unitycatalog/etc/db
```

```sh
mkdir -p /home/manoj/unity_catalog/{conf,data,db}
docker compose -f uc.yml up -d
```

- Put the Unity Catalog `application.yaml` (database connection etc.) in
  `/home/manoj/unity_catalog/conf` before starting.
- The server listens on port `8081` of the host. If this node also runs a
  Spark worker (which uses `8081` for its UI on the host), change the host
  port, e.g. `"8082:8080"`.

## 5. RustFS object storage (any node)

```yaml
services:
  rustfs-server:
    image: rustfs/rustfs:1.0.0-alpha.90
    ports:
      - "9000:9000"   # S3 API
      - "9001:9001"   # web console
    environment:
      - RUSTFS_VOLUMES=/data
      - RUSTFS_CONSOLE_ENABLE=true
      # - RUSTFS_ACCESS_KEY=...
      # - RUSTFS_SECRET_KEY=...
    volumes:
      - /home/manoj/rustfs/data:/data
```

```sh
mkdir -p /home/manoj/rustfs/data
docker compose -f rustfs.yml up -d
```

- S3 API: `http://<node>:9000`, console: `http://<node>:9001`.
- Uncomment and set `RUSTFS_ACCESS_KEY` / `RUSTFS_SECRET_KEY` for
  predictable credentials; otherwise the service generates them.

## 6. Test the cluster

From any machine that can reach the cluster, submit a distributed job that
spreads partitions across the workers (see `test.py` in this folder):

```sh
docker run --rm -v "$PWD":/work -w /work spark:4.1.2 python test.py
```

Expected output ends with:

```
SUCCESS: Distributed count completed.
Total Elements: 1000000000
```

If the count hangs, workers are not reaching the master — check hostname
resolution between nodes (`ping rpi-node-01` from a worker) and that port
`7077` is reachable (`nc -vz rpi-node-01 7077`).

## Troubleshooting

- **Worker never shows up on master UI** — worker can't resolve/reach
  `rpi-node-01:7077`; check `/etc/hosts` and firewall rules between Pis.
- **Port conflicts** — host networking means Spark services bind the node's
  real ports: master `8080`/`7077`, worker `8081`. Don't run two of these
  on the same host, and adjust the Unity Catalog host port if it lands on
  the same node as a worker.
- **Executors get killed / OOM** — lower `SPARK_WORKER_MEMORY` and executor
  memory; Pi RAM is shared with the OS.
- **Check container logs** — `docker compose -f <file>.yml logs -f`.
