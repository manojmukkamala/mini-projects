from umqtt.simple import MQTTClient
import config
import wifi
import machine
import ubinascii
import ssl
import time

# Connection parameters come from config.py (local, gitignored).
# Copy config.example.py -> config.py and fill in real values.

# Get on Wi-Fi before touching the broker.
wifi.connect()

# Unique per-device client ID: <CLIENT_ID>-<MAC hex>
client_id = f"{config.CLIENT_ID}-{ubinascii.hexlify(machine.unique_id()).decode()}"

# ---------------------------
# TLS context
# ---------------------------
ssl_params = {"cert_reqs": ssl.CERT_REQUIRED}  # verify server cert using system CA

# ---------------------------
# Create client
# ---------------------------
client = MQTTClient(
    client_id=client_id,
    server=config.BROKER,
    port=config.PORT,
    user=config.USERNAME,
    password=config.PASSWORD,
    ssl=True,
    ssl_params=ssl_params
)

# ---------------------------
# Connect and subscribe
# ---------------------------
client.connect()
print(f"connected to {config.BROKER} via TLS")

client.subscribe(config.TOPIC)

# ---------------------------
# Publish and receive messages
# ---------------------------
client.publish(config.TOPIC, b"Hello from umqtt via TLS!")

try:
    while True:
        msg = client.check_msg()  # non-blocking, receives messages if any
        time.sleep(1)
except KeyboardInterrupt:
    client.disconnect()
    print("Disconnected")
