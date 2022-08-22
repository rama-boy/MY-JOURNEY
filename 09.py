# Simple Calculation Exercise

# temperature unit conversion exercise

# Celsius conversion program to other units

print("\nTEMPERATURE CONVERSION PROGRAM\n")

print("=== CELCIUS ===")
celcius = float(input('Enter temperature in celsius : '))
print("temperature is",celcius, "Celcius")

print("=== REAMUR ===")
reamur = (4/5) * celcius
print("the temperature in reamur is",reamur, "Reamur")

print("=== FAHRENHEIT ===")
fahrenheit = ((9/5) * celcius) + 32
print("the temperature in fahrenheit is",fahrenheit, "Fahrenheit")

print("=== KELVIN ===")
kelvin = celcius + 273
print("the temperature in kelvin is",kelvin, "Kelvin")