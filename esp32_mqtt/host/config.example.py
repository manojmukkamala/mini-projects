"""
Host-side MQTT configuration for the scripts in this folder.

Copy this file to config.py and fill in your real values:

    cp config.example.py config.py

config.py is gitignored — never commit it.
"""

# --- MQTT broker ---
BROKER = ""            # e.g. the TLS entrypoint hostname
PORT = 8883            # MQTT over TLS
USERNAME = ""
PASSWORD = ""

# --- Subscriber topic (mqtt_subscriber.py) ---
# HA MQTT discovery config topic, e.g. "homeassistant/sensor/<object_id>/config"
TOPIC = ""
