#!/usr/bin/env python3
"""
Publish Home Assistant MQTT discovery config for the Smart Kettle.

Run from this folder (smart_kettle/) so `app.config` is importable:

    python publish_discovery_messages.py

Broker/credentials come from app/config.py (same file the device uses).
The weight/liters discovery blocks are kept for when the device starts
reporting those sensors — uncomment to enable.
"""

import paho.mqtt.client as mqtt
import json
import sys

import app.config as cfg

device_info = {
    "identifiers": ["smart_kettle_device"],
    "name": "Smart Kettle",
    "manufacturer": "ESP32",
    "model": "Smart Kettle",
    "sw_version": "1.0",
}


def publish_discovery_messages(broker, port=8883, username=None, password=None):
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    if username and password:
        client.username_pw_set(username, password)

    try:
        print(f"connecting to {broker}:{port}")
        client.connect(broker, port, 60)
        client.loop_start()

        # Temperature sensor discovery
        temp_config = {
            "name": "Smart Kettle Temperature",
            "state_topic": cfg.TOPIC_TEMPERATURE,
            "unit_of_measurement": "°F",
            "value_template": "{{ value }}",
            "device": device_info,
            "unique_id": "smart_kettle_temperature",
            "platform": "mqtt",
        }

        # Weight sensor discovery (enable when the device reports it)
        # weight_config = {
        #     "name": "Smart Kettle Weight",
        #     "state_topic": cfg.TOPIC_WEIGHT,
        #     "unit_of_measurement": "g",
        #     "value_template": "{{ value }}",
        #     "device": device_info,
        #     "unique_id": "smart_kettle_weight",
        #     "platform": "mqtt",
        # }
        # weight_topic = cfg.DISCOVERY_TOPIC_WEIGHT
        # client.publish(weight_topic, "", qos=0, retain=True)  # clear any stale config
        # client.publish(weight_topic, json.dumps(weight_config), qos=0, retain=True)

        # Liters sensor discovery (enable when the device reports it)
        # liters_config = {
        #     "name": "Smart Kettle Liters",
        #     "state_topic": cfg.TOPIC_LITERS,
        #     "unit_of_measurement": "L",
        #     "value_template": "{{ value }}",
        #     "device": device_info,
        #     "unique_id": "smart_kettle_liters",
        #     "platform": "mqtt",
        # }
        # liters_topic = cfg.DISCOVERY_TOPIC_LITERS
        # client.publish(liters_topic, "", qos=0, retain=True)  # clear any stale config
        # client.publish(liters_topic, json.dumps(liters_config), qos=0, retain=True)

        # Publish temperature discovery (clear any stale config first)
        temp_topic = cfg.DISCOVERY_TOPIC_TEMPERATURE
        client.publish(temp_topic, "", qos=0, retain=True)
        client.publish(temp_topic, json.dumps(temp_config), qos=0, retain=True)
        print(f"published temperature discovery to {temp_topic}")

        client.loop_stop()
        client.disconnect()

    except Exception as e:
        print(f"error publishing discovery messages: {e}")
        client.loop_stop()
        client.disconnect()
        sys.exit(1)


def main():
    publish_discovery_messages(cfg.MQTT_SERVER, 8883, cfg.MQTT_USER, cfg.MQTT_PASS)


if __name__ == "__main__":
    main()
