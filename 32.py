# duplicating list technique

a = ["Rama","Ikrama","Athena"]
print(f"a = {a}")
b = a # pass by reference
print(f"b = {b}")

# change member from data a

# will still change both lists
a[1] = "Zeus"
b.sort()
print(f"a = {a}")
print(f"b = {b}")

# address of both lists a and b
print(f"address a = {hex(id(a))}")
print(f"address b = {hex(id(b))}")

# duplicate list with copy
print(f"make list c with a.copy()")
c = a.copy() # full duplicate / new data

print(f"address a = {hex(id(a))}")
print(f"address b = {hex(id(b))}")
print(f"address c = {hex(id(c))}")

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

print(f"we change the data 0")
c[0] = "Hena"
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

print(f"we change the data 1")
a[1] = "RAMARAMA"
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")