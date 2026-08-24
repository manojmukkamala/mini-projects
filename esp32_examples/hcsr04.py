from machine import Pin, time_pulse_us
import time

# Define GPIO pins for HC-SR04
TRIG_PIN = 2  # Adjust based on your wiring
ECHO_PIN = 4  # Adjust based on your wiring

# Initialize GPIO pins
trig = Pin(TRIG_PIN, Pin.OUT)
echo = Pin(ECHO_PIN, Pin.IN)

def measure_distance():
    # Ensure trigger is low
    trig.value(0)
    time.sleep_us(2)

    # Send 10µs pulse to trigger
    trig.value(1)
    time.sleep_us(10)
    trig.value(0)

    # Measure the pulse duration on Echo pin
    duration = time_pulse_us(echo, 1, 30000)  # Timeout at 30ms (max range ~5m)

    if duration < 0:
        return None  # Timeout occurred

    # Convert duration to distance in cm
    distance = (duration * 0.0343) / 2
    return round(distance, 2)

# Main loop
while True:
    dist = measure_distance()
    
    if dist is not None:
        print("Distance:", dist, "cm")
    else:
        print("Measurement timeout!")

    time.sleep(2)  # Read every 2 seconds

