#!/usr/bin/env python3
"""
MQTT subscriber that tails the Smart Kettle's Home Assistant discovery
topic and pretty-prints incoming JSON.

Broker/credentials come from config.py (copy config.example.py and fill it in).
"""

import paho.mqtt.client as mqtt
import json
import sys
import time

import config

TOPIC = "homeassistant/sensor/smart_kettle_temperature/config"


class MQTTSubscriber:
    def __init__(self, broker, port, username=None, password=None):
        self.broker = broker
        self.port = port
        self.client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
        self.client.on_connect = self.on_connect
        self.client.on_disconnect = self.on_disconnect
        self.client.on_message = self.on_message
        if username and password:
            self.client.username_pw_set(username, password)

    def on_connect(self, client, userdata, flags, reason_code, properties):
        if reason_code.is_failure:
            print(f"connection failed: {reason_code}")
            sys.exit(1)
        print(f"connected to {self.broker}:{self.port}")
        client.subscribe(TOPIC)
        print(f"subscribed to {TOPIC}")

    def on_disconnect(self, client, userdata, flags, reason_code, properties):
        print(f"disconnected: {reason_code}")

    def on_message(self, client, userdata, msg):
        print("\n--- Received Message ---")
        print(f"Topic: {msg.topic}")
        print(f"QoS: {msg.qos}")
        print(f"Retained: {msg.retain}")
        try:
            payload_json = json.loads(msg.payload.decode())
            print("\n--- Parsed JSON ---")
            for key, value in payload_json.items():
                print(f"{key}: {value}")
        except json.JSONDecodeError:
            print("\n--- Raw Payload ---")
            print(msg.payload.decode())

    def start_subscribing(self):
        try:
            self.client.connect(self.broker, self.port, 60)
            self.client.loop_start()
            print("waiting for messages... press Ctrl+C to stop")
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\nstopping subscriber...")
        finally:
            self.client.loop_stop()
            self.client.disconnect()


def main():
    subscriber = MQTTSubscriber(
        config.BROKER, config.PORT, config.USERNAME, config.PASSWORD
    )
    subscriber.start_subscribing()


if __name__ == "__main__":
    main()
