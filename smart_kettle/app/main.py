
from machine import Pin, I2C
from time import sleep
import math
import json

# Import modules
import app.config as cfg
from app.utils.sensor_drivers import MLX90614, HX711
from app.utils.display import setup_oled, setup_writer, display_temperature, display_liters, display_error
from app.utils.mqtt_wifi import initialize_mqtt, close_mqtt, ping_mqtt
from app.utils.calibration import read_calibration_offset, perform_initial_calibration, weight_to_liters

from machine import WDT


import time

def run_smart_kettle():

    wdt = WDT(timeout=15000)
    boot_time = time.ticks_ms()

    # --- Initialize I2C bus ---
    i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=100000)
    mlx = MLX90614(i2c)

    # --- Setup OLED display ---
    oled = setup_oled(i2c)
    wri = setup_writer(oled)

    # --- Initialize HX711 ---
    hx = HX711(dout=33, pd_sck=32)

    # --- Calibration ---
    # Try to read stored calibration offset
    stored_offset = read_calibration_offset()
    if stored_offset is not None:
        # Apply stored offset
        hx.offset = stored_offset
        print("Loaded stored calibration offset:", stored_offset)
    else:
        # Perform initial calibration
        perform_initial_calibration(hx)

    hx.set_scale(10000)   # adjust this scale factor experimentally

    # --- MQTT Setup ---
    mqtt_client = initialize_mqtt()
    # Add a small delay to ensure MQTT connection is stable
    if mqtt_client is not None:
        sleep(1)

    # State variables to track previous values for change detection
    prev_temp = None
    prev_weight = None

    # --- Main loop ---
    counter = 0
    # Initialize MQTT client
    mqtt_client = None

    # Add watchdog timer to prevent freezing
    last_mqtt_connect = 0
    watchdog_timeout = 300  # 5 minutes

    # Add MQTT ping counter to keep connection alive
    mqtt_ping_counter = 0

    while True:
        counter += 3
        mqtt_ping_counter += 1
        
        try:
            # Add timeout for sensor readings to prevent hanging
            import time as time_module
            
            # Read temperature with timeout handling
            try:
                ambient = mlx.ambient()
                obj = mlx.object()
                # Convert temperature to Fahrenheit
                temp_f = (obj * 9/5) + 32
                
                # Apply 10-degree correction as temperature sensor is off by 10 degrees F
                temp_f_corrected = temp_f + 10
            except Exception as temp_e:
                print("Temperature reading error:", str(temp_e))
                temp_f_corrected = None
                
            # Read weight with timeout handling
            try:
                weight = hx.get_units()
                # Floor weight to 0 and format to 1 decimal point
                weight = max(0, weight)
                liters = weight_to_liters(weight)
            except Exception as weight_e:
                print("Weight reading error:", str(weight_e))
                weight = None
                liters = None
                
            # Update display
            try:
                oled.fill(0)
                if temp_f_corrected is not None:
                    display_temperature(wri, temp_f_corrected)
                if liters is not None:
                    display_liters(wri, liters)
                oled.show()
            except Exception as display_e:
                print("Display update error:", str(display_e))
                # Continue execution even if display fails
                
            # Publish data via MQTT
            try:
                # Check if we need to reconnect MQTT (every 5 minutes)
                current_time = time_module.ticks_ms()
                if (mqtt_client is None or 
                    time_module.ticks_diff(current_time, last_mqtt_connect) > watchdog_timeout * 1000):

                    if mqtt_client:
                        close_mqtt(mqtt_client)

                    mqtt_client = initialize_mqtt()
                    if mqtt_client is not None:
                        last_mqtt_connect = current_time
                        
                # Send MQTT ping every 30 seconds to keep connection alive
                if mqtt_client is not None and mqtt_ping_counter >= 10:  # Every 30 seconds (10 * 3 seconds)
                    
                    ping_mqtt(mqtt_client)
                    mqtt_ping_counter = 0  # Reset counter
                    
                # Only publish if we have valid data and MQTT is connected
                if mqtt_client is not None and temp_f_corrected is not None and liters is not None:
                    # Only publish temperature if it has changed
                    rounded_temp = round(temp_f_corrected)
                    if prev_temp is None or abs(rounded_temp - prev_temp) >= 1:  # 1 degree threshold
                        mqtt_client.publish(cfg.TOPIC_TEMPERATURE, "{:d}".format(rounded_temp))
                        prev_temp = rounded_temp
                        
                    # Only publish weight if it has changed
                    if prev_weight is None or abs(weight - prev_weight) >= 0.1:  # 0.1 unit threshold
                        mqtt_client.publish(cfg.TOPIC_WEIGHT, "{:.1f}".format(weight))
                        mqtt_client.publish(cfg.TOPIC_LITERS, "{:.1f}".format(liters))
                        prev_weight = weight
            except Exception as e:
                print("MQTT publish error:", str(e))
                # Continue execution even if publish fails
                # Reinitialize MQTT on error
                mqtt_client = None
                
        except Exception as e:
            # Handle any other errors that might occur
            print("Main loop error:", str(e))
            # Try to display the error on OLED
            try:
                display_error(wri, str(e))
            except:
                # If even display_error fails, just print to console
                print("Failed to display error on OLED")

        if time.ticks_diff(time.ticks_ms(), boot_time) > 3600 * 1000:
            import machine
            machine.reset()

        wdt.feed()            
        sleep(3)

if __name__ == "__main__":
    run_smart_kettle()