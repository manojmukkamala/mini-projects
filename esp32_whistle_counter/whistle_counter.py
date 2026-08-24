import machine
import time
import ubinascii
from umqtt.simple import MQTTClient

import config
import wifi


def run():
    wifi.connect()

    # Initialize MQTT (unique client ID: prefix + MAC)
    print("Initialize MQTT Broker!")
    client_id = f"{config.CLIENT_ID}-{ubinascii.hexlify(machine.unique_id()).decode()}"
    client = MQTTClient(
        client_id,
        config.BROKER,
        port=config.PORT,
        user=config.USERNAME,
        password=config.PASSWORD,
    )
    client.connect()
    print("Connected to MQTT Broker!")

    # Setup whistle sensor (KY-037 breakout) on GPIO 23
    whistle_sensor = machine.Pin(23, machine.Pin.IN)

    whistle_count = 0
    last_whistle_time = 0
    THRESHOLD_TIME = 60  # minimum seconds between counts

    print("Counting Whistles!")

    while True:
        if whistle_sensor.value() == 1:  # whistle detected
            current_time = time.time()
            if current_time - last_whistle_time >= THRESHOLD_TIME:
                whistle_count += 1
                last_whistle_time = current_time
                print(f"Whistle detected! Total count: {whistle_count}")

                # Publish to MQTT
                client.publish(config.TOPIC, str(whistle_count))
                print("Published to MQTT:", whistle_count)

        time.sleep(0.1)  # small delay to keep CPU usage low


if __name__ == "__main__":
    run()
