# Instance Methods are bound to a specific instance. 
# Instance Methods can access and modify the state of the bound object.

# Class Methods are bound to a class.
# Class Methods can access and modify the class state.

# Static Methods cannot access and modify an object state.
# Static Methods cannot access and modify the class's state.
# Python doesn't implicitly pass the cls parameter (or the self parameter) to static methods.

# Static Methods are used to define utility methods or group functions that have some logical relationships in a class.

class TemperatureConverter:
    KELVIN = 'K'
    FAHRENHEIT = 'F'
    CELSIUS = 'C'

    @staticmethod
    def celsius_to_fahrenheit(c):
        return 9 * c/5 + 32

    @staticmethod
    def fahrenheit_to_celsius(f):
        return 5 * (f - 32)/9

    @staticmethod
    def celsius_to_kelvin(c):
        return c + 273.15

    @staticmethod
    def kelvin_to_celsius(k):
        return k - 273.15

    @staticmethod
    def fahrenheit_to_kelvin(f):
        return 5 * (f + 459.67) / 9

    @staticmethod
    def kelvin_to_fahrenheit(k):
        return 9 * k/5 - 459.67

    @staticmethod
    def format(value, unit):
        symbol = ''
        if unit == TemperatureConverter.FAHRENHEIT:
            symbol = '°F'
        elif unit == TemperatureConverter.CELSIUS:
            symbol = '°C'
        elif unit == TemperatureConverter.KELVIN:
            symbol = '°K'
        
        return f'{value} {symbol}'

f = TemperatureConverter.celsius_to_fahrenheit(32)
print(TemperatureConverter.format(f, TemperatureConverter.FAHRENHEIT))        