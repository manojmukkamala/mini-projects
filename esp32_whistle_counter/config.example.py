"""
Whistle counter configuration.

Copy this file to config.py and fill in your real values:

    cp config.example.py config.py

config.py is gitignored — never commit it.
"""

# --- Wi-Fi ---
WIFI_SSID = ""
WIFI_PASS = ""

# --- MQTT broker (plain MQTT over the LAN) ---
BROKER = ""                    # Mosquitto host IP or hostname
PORT = 1883
USERNAME = ""
PASSWORD = ""
CLIENT_ID = "whistle-counter"  # a MAC-based suffix is appended automatically
TOPIC = "esp32/device/<device_name>"
