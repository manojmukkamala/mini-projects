# esp32_examples

Small ESP32 hardware experiments (MicroPython). Everything runs on
the ESP32 itself, not on a dev machine.

| file | what it does |
|---|---|
| `fan12v.py` | Toggles a 12 V fan via a PN2222 transistor on GPIO 23: 5 s on, 60 s off, forever |
| `hcsr04.py` | Continuous HC-SR04 ultrasonic distance readings (TRIG=2, ECHO=4), prints cm every 2 s |

## How to run

Copy the script onto the ESP32's flash (e.g. as `main.py`), e.g. with
mpremote:

    mpremote connect COMx copy fan12v.py :main.py reset

Pin numbers are at the top of each file — adjust to your wiring.

There is deliberately no `pyproject.toml`/`uv` env here — these are
MicroPython device scripts with no host-side deps.

This project lives only in this repo — no Nextcloud working copy.

## Wiring notes

- `fan12v.py`: GPIO 23 drives the PN2222 base — use a 1 k–4.7 k base
  resistor; collector to the 12 V fan, emitter to GND.
- `hcsr04.py`: the HC-SR04 ECHO line is 5 V while ESP32 GPIOs are
  3.3 V — add a voltage divider if you see erratic readings or resets.
