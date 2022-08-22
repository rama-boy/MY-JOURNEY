# a = 10, a is a variable with a value of 10

# data type : unit digit
data_integer = 1
print("data : ", data_integer)
print("- type : ", type(data_integer))

# data type : float (there is a comma)
data_float = 1.5
print("data : ", data_float)
print("- type : ", type(data_float))

# data type : string (character set)
data_string = "Rama"
print("data : ", data_string)
print("- type : ", type(data_string))

# data type : boolean (biner true/false)
data_boolean = True
print("data : ", data_boolean)
print("- type : ", type(data_boolean))

## special type data

# complex number
data_complex = complex(5,6)
print("data : ", data_complex)
print("- type : ", type(data_complex))

# type data from languange C
from ctypes import c_double
data_c_double = c_double(10.5)
print("data : ", data_c_double)
print("- type : ", type(data_c_double))