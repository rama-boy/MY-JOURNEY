# Learn the casting
# change one data to another
# type data : integer, float, string, boolean

# INTEGER
print("=== INTEGER ===")
data_int = 5
print("data =", data_int, ",type =",type(data_int))

data_float = float(data_int)
data_str   = str(data_int)
data_bool  = bool(data_int) # will be false if int value is 0
print("data =", data_float, ",type =",type(data_float))
print("data =", data_str, ",type =",type(data_str))
print("data =", data_bool, ",type =",type(data_bool))

## FLOAT
print("=== FLOAT ===")
data_float = 8.5
print("data =", data_float, ",type =",type(data_float))

data_int   = int(data_float) # will be rounded down
data_str   = str(data_float)
data_bool  = bool(data_float) # will be false if float value is 0
print("data =", data_int, ",type =",type(data_int))
print("data =", data_str, ",type =",type(data_str))
print("data =", data_bool, ",type =",type(data_bool))

## BOOLEAN
print("=== BOOLEAN ===")
data_bool = True
print("data =", data_bool, ",type =",type(data_bool))

data_int   = int(data_bool) # will be rounded down
data_str   = str(data_bool)
data_float  = float(data_bool) # will be false if float value is 0
print("data =", data_int, ",type =",type(data_int))
print("data =", data_str, ",type =",type(data_str))
print("data =", data_float, ",type =",type(data_float))

## STRING
print("=== STRING ===")
data_str = "10"
print("data =", data_str, ",type =",type(data_str))

data_int   = int(data_str) # string must number
data_str   = str(data_str) # string must number
data_bool  = bool(data_str) # false if string is empty
print("data =", data_int, ",type =",type(data_int))
print("data =", data_float, ",type =",type(data_float))
print("data =", data_bool, ",type =",type(data_bool))