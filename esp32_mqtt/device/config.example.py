"""
Local Wi-Fi/MQTT configuration for test_umqtt.py.

Copy this file to config.py and fill in your real values:

    cp config.example.py config.py

config.py is gitignored — never commit it.
"""

# --- Wi-Fi (the ESP32 access point) ---
WIFI_SSID = ""
WIFI_PASS = ""

# --- MQTT broker ---
BROKER = ""            # must match the server certificate CN/SAN
PORT = 8883            # MQTT over TLS
USERNAME = ""
PASSWORD = ""

# --- Client / topic ---
CLIENT_ID = "umqtt-test"    # test_umqtt.py appends a unique MAC-based suffix
TOPIC = b"test/topic"
