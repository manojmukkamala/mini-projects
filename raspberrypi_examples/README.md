# raspberrypi_examples

Small Raspberry Pi hardware experiments (GPIO + camera) and a Pi
provisioning script. Everything runs on the Pi itself, not on a dev
machine.

| file | what it does |
|---|---|
| `led_example.py` | Turns an LED on GPIO 23 on for 5 s |
| `camera_example.py` | Records 10 s of video with the Pi Camera to `example.h264` (uncomment the `capture` line for a still) |
| `distance_sensor.py` | One-shot HC-SR04 ultrasonic distance reading (TRIG=17, ECHO=24), prints cm |
| `garage_light.py` | Continuous loop: HC-SR04 (TRIG=4, ECHO=23) drives a green/yellow/red LED (GPIO 17/27/22) as an object approaches |
| `config.sh` | Provisioning scratch script: apt upgrade, VNC/xrdp reinstall, `raspi-config`, Kafka 3.2.1 install (was `RaspberryPi.sh` in the original local copy) |

## How to run

On the Pi, e.g.:

    python3 led_example.py
    python3 camera_example.py

`RPi.GPIO` ships with Raspberry Pi OS; `camera_example.py` needs the
legacy `picamera` Python 3 camera stack. There is deliberately no
`pyproject.toml`/`uv` env here — the deps are board-only.

Run `config.sh` only on a Pi you actually intend to reconfigure: it is
a scratchpad of sudo/interactive commands, not an idempotent script.
