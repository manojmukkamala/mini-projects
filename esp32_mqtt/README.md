# esp32_mqtt

MQTT smoke-test tools for the homelab broker, in two halves:

- `host/` — paho-mqtt scripts that run on the PC
- `device/` — MicroPython scripts that run on the ESP32 (umqtt)

Together they verify end-to-end connectivity, including TLS through
the Traefik entrypoint.

## host/

| file | what it does |
|---|---|
| `mqtt_list_topics.py` | Subscribes to `#` and lists every topic observed in a 3 s window (`python mqtt_list_topics.py <broker>`) |
| `mqtt_subscriber.py` | Tails a device's HA MQTT discovery topic (set in `config.py`) and pretty-prints the JSON |
| `config.example.py` | Template — copy to `config.py` and fill in broker creds |

## device/

| file | what it does |
|---|---|
| `test_umqtt.py` | Connects to Wi-Fi, then to the broker over TLS (server cert verified), subscribes + publishes to a test topic, then listens. Client ID gets a unique MAC-based suffix |
| `wifi.py` | Wi-Fi connect helper (retries 10×3 s, raises on failure) |
| `config.example.py` | Template — copy to `config.py` and fill in Wi-Fi + broker creds |

## Setup

`config.py` is gitignored in both halves — create it from the example
when you need it:

    cp host/config.example.py host/config.py
    cp device/config.example.py device/config.py

`device/` flash must also contain the `umqtt` library (copy it to the
flash root alongside the scripts).

## How to run

Host, from this folder (one-time `uv sync` first):

    uv sync
    uv run host/mqtt_list_topics.py <broker>
    uv run host/mqtt_subscriber.py

Device, e.g. with mpremote:

    mpremote connect COMx copy config.py wifi.py test_umqtt.py :/ reset

The `uv` env covers the host tools only — `device/` is MicroPython and
has no host-side deps.
