"""Wi-Fi helper: connect the ESP32 to the AP from config.py."""

import network
import time
import config


def connect(tries=10, delay=3):
    """Connect to the configured AP; raise RuntimeError on failure."""
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print(f"connecting to Wi-Fi '{config.WIFI_SSID}'...")
        wlan.connect(config.WIFI_SSID, config.WIFI_PASS)
        for _ in range(tries):
            if wlan.isconnected():
                break
            time.sleep(delay)
        if not wlan.isconnected():
            raise RuntimeError(f"could not connect to '{config.WIFI_SSID}'")
    print(f"on '{config.WIFI_SSID}', ip {wlan.ipaddr()}")
    return wlan
