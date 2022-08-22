# string operations and manipulation

# 1. concatenate string

name_first = "Rama"
name_middle = "De"
name_end = "Family"

full_name = name_first + " " + name_middle + "'" + name_end
print(full_name)

# 2. calculate string length
length = len(full_name)
print(length)
print("length of " + full_name + " = " + str(length))

# 3. operator for string

# checks if there is a character or string component in the string

d = "d"
status = d in full_name
print(d + " It is in " + full_name + " = " + str(status))

D = "D"
status = D in full_name
print(D + " It is in " + full_name + " = " + str(status))

d = "d"
status = d not in full_name
print(d + " not in " + full_name + " = " + str(status))

# repeating string
print("rama"*3)
print(3*"rama")

# indexing
print("0th index :" + full_name[0])
print("1st index :" + full_name[1])
print("2nd index :" + full_name[2])
print("3rd index :" + full_name[3])
print("index-(-1) :" + full_name[-1])
print("index-(-2) :" + full_name[-2])
print("index-[0:3]:" + full_name[0:4])
print("index-[5:13]:" + full_name[5:14])
print("index-[0,2,4,6,8,10]:" + full_name[0:10:2])

# smallest item
print("the smallest : " + min(full_name)) # sorted alphabetically
# biggest item
print("the biggest : " + max(full_name)) # sorted alphabetically

ascii_code = ord(" ")
print("ascii code for spaces is : " + str(ascii_code))
data = 90
print("char for ASCII 90 is " + chr(data))

# 4. operator in the form of method

data = "rama rama rama"
amount = data.count("a")
print("jumlah pada " + data + " = " + str(amount))