# esp32_whistle_counter

ESP32 (MicroPython) whistle counter: reads a KY-037 breakout as a
digital input on GPIO 23, counts whistles with a 60-second minimum
between counts, and publishes the running total to an MQTT broker
over the LAN.

| file | what it does |
|---|---|
| `whistle_counter.py` | Main script — Wi-Fi + MQTT connect, count loop, publishes the total |
| `wifi.py` | Wi-Fi connect helper (retries 10×3 s, raises on failure) |
| `config.example.py` | Template — copy to `config.py` and fill in Wi-Fi + broker creds |

## How to run

1. Create `config.py` from the example (Wi-Fi SSID/password, MQTT
   broker/creds, topic). `config.py` is gitignored.
2. Flash to the ESP32 (`umqtt` must be on the flash root):

    mpremote connect COMx copy config.py wifi.py whistle_counter.py :/ reset

The script runs itself on boot — no manual `run()` call needed.

## Notes

- Plain MQTT (no TLS) — meant for a LAN broker (e.g. a Mosquitto container).
- No auto-reconnect: if the broker connection drops, the next publish
  raises and the loop stops.
- This is a MicroPython project — no `pyproject.toml`/`uv` env.
