# smart_kettle

ESP32 (MicroPython) smart kettle: reads water temperature (MLX90614 IR)
and water level (HX711 load cell on a scale), shows both on an I2C OLED,
and publishes them over MQTT (TLS) for Home Assistant.

    app/                             device code (flashed to the ESP32)
    publish_discovery_messages.py    host tool: publishes the HA discovery config
    weight_calibration.txt           stored load-cell tare offset (device state)

## app/ (device)

| file | what it does |
|---|---|
| `main.py` | Entry point — WDT, sensor reads, OLED display, change-detected MQTT publishes, 1-hour reboot |
| `config.py` | WiFi/MQTT creds + topics — gitignored; copy `config.example.py` and fill it in |
| `utils/sensor_drivers.py` | Inline MLX90614 (I2C) and HX711 (24-bit load cell) drivers |
| `utils/display.py` | OLED setup (SH1106/SSD1306 auto-detect) + display helpers |
| `utils/mqtt_wifi.py` | WiFi + MQTT (TLS) connect/ping/close helpers |
| `utils/calibration.py` | Tare-offset persistence (`weight_calibration.txt`) + weight→liters conversion |
| `utils/writer.py`, `freesans20.py`, `writer_gui.py`, `sh1106.py` | Display stack: font, text writer, OLED driver |

## How to run

Device:

1. `cp app/config.example.py app/config.py` and fill it in
   (WiFi, MQTT creds, topics).
2. Flash the `app/` package plus `weight_calibration.txt` to the flash
   root, e.g.:

    mpremote connect COMx copy app/ :/ copy weight_calibration.txt :/

Host, from this folder (one-off, no local env needed):

    uv run --with paho-mqtt==2.1.0 python publish_discovery_messages.py

## Notes

- MicroPython device project — no `pyproject.toml`/`uv` env for `app/`;
  the host discovery tool just needs `paho-mqtt`.
- `config.py` is gitignored — never commit it.
