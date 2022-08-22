# string format

# generic example
# string
import numbers
from this import d


name = "ramarama"
format_str = f"hello {name}"
print(format_str)

# boolean
boolean = True
format_str = f"boolean = {boolean}"
print(format_str)

# numbers
numbers = 2003.3
format_str = f"numbers = {numbers}"
print(format_str)

# integers
numbers = 15
format_str = f"integers = {numbers:d}"
print(format_str)

# numbers of the order of thousands
numbers = 2000
format_str = f"thousands = {numbers:,}"
print(format_str)

numbers = 2000000
format_str = f"millions = {numbers:,}"
print(format_str)

# decimal number
numbers = 2003.34321
format_str = f"decimal = {numbers:.3f}"
print(format_str)

# display leading zero
numbers = 2003.34321
format_str = f"decimal = {numbers:010.3f}"
print(format_str)

# display a plus(+) or minus(-) sign
minus_number = -10
plus_number = 10
format_minus = f"minus = {minus_number:+d}"
format_plus = f"plus = {plus_number:+d}"
print(format_minus)
print(format_plus)

# format percent
percentage = 0.045
format_percent = f"percent = {percentage:.2%}"
print(format_percent)

# perform arithmetic operations inside placeholders
price = 10000
amount = 5
format_str = f"total price = Rp.{price*amount:,}"
print(format_str)

# other number formats (binary, octal, hexadecimal)\
numbers = 255
format_binary = f"binary = {bin(numbers)}"
format_octal = f"octal = {oct(numbers)}"
format_hex = f"hex = {hex(numbers)}"
print(format_binary)
print(format_octal)
print(format_hex)