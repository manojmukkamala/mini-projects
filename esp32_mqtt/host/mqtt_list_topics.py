#!/usr/bin/env python3
"""
List topics observed on an MQTT broker.

Usage:
    python mqtt_list_topics.py <broker>

Credentials come from config.py (copy config.example.py and fill it in).
"""

import paho.mqtt.client as mqtt
import sys
import time

import config

topics = set()


def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code.is_failure:
        print(f"connection failed: {reason_code}")
        sys.exit(1)
    client.subscribe("#")
    print("subscribed to # — collecting topics for a few seconds...")


def on_message(client, userdata, msg):
    if msg.topic not in topics:
        topics.add(msg.topic)
        print(f"  found: {msg.topic}")


def main():
    if len(sys.argv) < 2:
        print(f"Usage: python {sys.argv[0]} <broker>")
        sys.exit(1)
    broker = sys.argv[1]

    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    client.username_pw_set(config.USERNAME, config.PASSWORD)
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(broker, config.PORT)
    client.loop_start()
    time.sleep(3)
    client.loop_stop()
    client.disconnect()

    print(f"\nTotal topics observed: {len(topics)}")


if __name__ == "__main__":
    main()
