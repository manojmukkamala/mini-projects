from machine import Pin, I2C
import math
import time

# --- MLX90614 driver ---
class MLX90614:
    def __init__(self, i2c, address=0x5A):
        self.i2c = i2c
        self.address = address

    def read16(self, reg):
        try:
            data = self.i2c.readfrom_mem(self.address, reg, 3)
            return (data[1] << 8) | data[0]
        except Exception as e:
            print("I2C read error for MLX90614:", str(e))
            return None

    def read_temp(self, reg):
        raw = self.read16(reg)
        if raw is None:
            return None
        temp = (raw * 0.02) - 273.15
        return temp

    def ambient(self):
        return self.read_temp(0x06)

    def object(self):
        return self.read_temp(0x07)

# --- HX711 driver ---
class HX711:
    def __init__(self, dout, pd_sck, gain=128):
        self.dout = Pin(dout, Pin.IN)
        self.pd_sck = Pin(pd_sck, Pin.OUT)
        self.gain = gain
        self.offset = 0
        self.scale = 1

    def is_ready(self):
        return self.dout.value() == 0

    def read_with_timeout(self, timeout=1000):
        """Read from HX711 with timeout to prevent hanging"""
        start_time = time.ticks_ms()
        while not self.is_ready():
            if time.ticks_diff(time.ticks_ms(), start_time) > timeout:
                print("HX711 timeout waiting for data")
                return None
            time.sleep_ms(1)
        
        data = 0
        for _ in range(24):
            self.pd_sck.value(1)
            data = (data << 1) | self.dout.value()
            self.pd_sck.value(0)
        # set gain
        for _ in range({128: 1, 64: 3, 32: 2}[self.gain]):
            self.pd_sck.value(1)
            self.pd_sck.value(0)
        if data & 0x800000:
            data |= ~0xffffff
        return data

    def read_average(self, times=5, timeout=1000):
        """Read average with timeout to prevent hanging"""
        values = []
        for _ in range(times):
            val = self.read_with_timeout(timeout)
            if val is not None:
                values.append(val)
            else:
                print("HX711 read timeout during average")
                return None
        return sum(values) / len(values) if values else None

    def get_value(self):
        return self.read_average() - self.offset

    def get_units(self):
        return self.get_value() / self.scale

    def tare(self, times=15):
        self.offset = self.read_average(times)

    def set_scale(self, scale):
        self.scale = scale
