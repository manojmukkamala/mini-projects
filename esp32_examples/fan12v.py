from machine import Pin
import time

# Define the GPIO pin connected to the base of the PN2222 transistor
fan_pin = Pin(23, Pin.OUT)

# Function to turn the fan on
def turn_fan_on():
    fan_pin.value(1)  # Set the GPIO pin high (3.3V) to turn the fan on

# Function to turn the fan off
def turn_fan_off():
    fan_pin.value(0)  # Set the GPIO pin low (0V) to turn the fan off

# Main loop
while True:
    turn_fan_on()  # Turn the fan on
    print("Fan is ON")
    time.sleep(5)  # Keep the fan on for 5 seconds
    
    turn_fan_off()  # Turn the fan off
    print("Fan is OFF")
    time.sleep(60)  # Keep the fan off for 60 seconds

