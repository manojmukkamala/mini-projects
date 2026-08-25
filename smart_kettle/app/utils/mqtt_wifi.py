import network
import time
from umqtt.simple import MQTTClient
import ubinascii
import machine
import app.config as cfg

# MQTT Configuration
MQTT_SERVER = cfg.MQTT_SERVER
MQTT_PORT = 8883
MQTT_SSL = True
MQTT_SSL_PARAMS = {'server_hostname': MQTT_SERVER}
MQTT_CLIENT_ID = ubinascii.hexlify(machine.unique_id()).decode()
MQTT_USER = cfg.MQTT_USER
MQTT_PASS = cfg.MQTT_PASS

# Wi-Fi Configuration
WIFI_SSID = cfg.WIFI_SSID
WIFI_PASS = cfg.WIFI_PASS

def connect_wifi():
    """Connect to Wi-Fi network"""
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print("Connecting to Wi-Fi...")
        wlan.connect(WIFI_SSID, WIFI_PASS)
        # Add timeout to prevent hanging
        timeout = 30
        start_time = time.ticks_ms()
        while not wlan.isconnected():
            if time.ticks_diff(time.ticks_ms(), start_time) > timeout * 1000:
                print("Wi-Fi connection timeout")
                return None
            time.sleep(1)
    print("Wi-Fi Connected:", wlan.ifconfig())
    return wlan

def initialize_mqtt():
    """Initialize and connect to MQTT broker"""
    try:
        # Connect to Wi-Fi
        wlan = connect_wifi()
        if wlan is None:
            print("Failed to connect to Wi-Fi")
            return None
        
        # Initialize MQTT
        print("Initialize MQTT Broker!")
        mqtt_client = MQTTClient(MQTT_CLIENT_ID
                            , MQTT_SERVER
                            , port=MQTT_PORT
                            , user=MQTT_USER
                            , password=MQTT_PASS
                            , ssl=MQTT_SSL
                            , ssl_params=MQTT_SSL_PARAMS
                            , keepalive=60  # Add keepalive
                            )        
        mqtt_client.connect()
        print("Connected to MQTT Broker!")
        return mqtt_client
        
    except Exception as e:
        # If MQTT fails, continue with normal operation
        print("MQTT initialization failed:", str(e))
        return None

def ping_mqtt(mqtt_client):
    # Do nothing on TLS — keepalive is handled internally
    return True

def close_mqtt(mqtt_client):
    try:
        mqtt_client.disconnect()
    except:
        pass
    try:
        mqtt_client.sock.close()
    except:
        pass  

# Don't initialize MQTT at import time - do it in the main loop
# initialize_mqtt()
