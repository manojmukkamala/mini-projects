from machine import Pin, I2C
import app.utils.writer as writer
from app.utils import freesans20
from app.utils.writer_gui import Label

# --- OLED setup (auto-detect SH1106 or SSD1306) ---
def setup_oled(i2c):
    try:
        import ssd1306
        oled = ssd1306.SSD1306_I2C(128, 64, i2c)
    except ImportError:
        from app.utils.sh1106 import SH1106_I2C
        oled = SH1106_I2C(128, 64, i2c)
    return oled

# --- Initialize Writer with custom font ---
def setup_writer(oled):
    return writer.Writer(oled, freesans20)

# --- Display functions ---
def display_temperature(writer, temperature_f):
    """Display temperature on OLED"""
    try:
        Label(writer, 20, 40, "{:.0f} F".format(temperature_f))
    except Exception as e:
        print("Error displaying temperature:", str(e))

def display_liters(writer, liters):
    """Display liters on OLED"""
    try:
        Label(writer, 40, 40, "{:.2f} L".format(liters))
    except Exception as e:
        print("Error displaying liters:", str(e))

def display_error(writer, error_message):
    """Display error message on OLED"""
    try:
        writer.device.fill(0)
        writer.device.text("Sensor error", 0, 0, 1)
        # Limit the error message length to prevent display issues
        if len(error_message) > 15:
            error_message = error_message[:12] + "..."
        writer.device.text(error_message, 0, 16, 1)
        writer.device.show()
    except Exception as e:
        # If we fail to display error, at least print to console
        print("Failed to display error on OLED:", str(e))
