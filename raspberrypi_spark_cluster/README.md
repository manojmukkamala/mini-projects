# raspberrypi_spark_cluster

Setup guide for a multi-node Apache Spark 4.1.2 cluster on Raspberry Pis,
deployed with Docker Compose — plus a test job to verify distribution
across workers.

| file | what it does |
|---|---|
| `setup.md` | End-to-end guide: Docker install, Spark master + workers, Unity Catalog, RustFS object storage, test + troubleshooting |
| `test.py` | PySpark job that parallelizes 10⁹ elements across 12 partitions and counts them — hangs if workers can't reach the master |

## How to run

Follow `setup.md` to bring up the cluster (master on `rpi-node-01`,
workers on the other Pis). Then, from any machine that can reach the
cluster:

    docker run --rm -v "$PWD":/work -w /work spark:4.1.2 python test.py

There is deliberately no `pyproject.toml`/`uv` env here — the script runs
inside the `spark:4.1.2` image, which ships PySpark.
