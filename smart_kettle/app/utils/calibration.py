import os

# Water Volume Calculation ---
# Calibration data: liters vs weight readings
# [0.5, 0.75, 1, 1.25] liters corresponds to [1.4, 2.1, 2.8, 3.5] weight
# Using linear regression to calculate conversion factor
# Weight per liter = (3.5 - 1.4) / (1.25 - 0.5) = 2.1 / 0.75 = 2.8
# So 1 liter = 2.8 weight units
LITERS_PER_WEIGHT = 2.90  # weight units per liter

CALIBRATION_FILE = "weight_calibration.txt"

def weight_to_liters(weight):
    """Convert weight reading to liters"""
    return weight / LITERS_PER_WEIGHT

def read_calibration_offset():
    """Read stored calibration offset from file (ignores # comment lines)"""
    try:
        with open(CALIBRATION_FILE, 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    return float(line)
    except:
        # Return None if file doesn't exist or can't be read
        return None

def save_calibration_offset(offset):
    """Save calibration offset to file"""
    try:
        with open(CALIBRATION_FILE, 'w') as f:
            f.write(str(offset))
    except Exception as e:
        print("Failed to save calibration:", e)

def perform_initial_calibration(hx):
    """Perform initial calibration by taring"""
    print("Performing initial calibration...")
    hx.tare()
    # Save the offset for future use
    save_calibration_offset(hx.offset)
    print("Saved initial calibration offset:", hx.offset)
    return hx.offset

