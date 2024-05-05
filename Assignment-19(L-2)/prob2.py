def celsiusToFahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheitToCelsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Example usage:
temperature_celsius = 20
temperature_fahrenheit = celsiusToFahrenheit(temperature_celsius)
print("20 degrees Celsius is equal to", temperature_fahrenheit, "degrees Fahrenheit.")

temperature_fahrenheit = 68
temperature_celsius = fahrenheitToCelsius(temperature_fahrenheit)
print("68 degrees Fahrenheit is equal to", temperature_celsius, "degrees Celsius.")
