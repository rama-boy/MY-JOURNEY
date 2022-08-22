data_0 = [1,2]
data_1 = [3,4]
data_2D = [data_0,data_1,10]
data_2D_copy = data_2D.copy()
print(f"data = {data_2D}")
print(f"data copy = {data_2D_copy}")

# fetch data from nested list
data = data_2D[0][0]
print(f"data = {data}")

# all addresses
print(f"real address = {hex(id(data_2D))}")
print(f"fake address = {hex(id(data_2D_copy))}")

print("THE ADDRESS OF THE 1st MEMBER")
print(f"real address = {hex(id(data_2D[0]))}")
print(f"fake address = {hex(id(data_2D_copy[0]))}")

data_2D[1][0] = 5
data_2D[2] = 9
print(f"data = {data_2D}")
print(f"data copy = {data_2D_copy}")

# use deep copy
from copy import deepcopy
data_2D = [data_0,data_1,10]
data_2D_deepcopy = deepcopy(data_2D)
print(f"real address = {hex(id(data_2D))}")
print(f"deep address = {hex(id(data_2D_deepcopy))}")

print("THE ADDRESS OF THE 1st MEMBER")
print(f"real address = {hex(id(data_2D[0]))}")
print(f"deep address = {hex(id(data_2D_deepcopy[0]))}")

data_2D[1][0] = 30
print(f"data = {data_2D}")
print(f"data copy = {data_2D_copy}")
print(f"data deep = {data_2D_deepcopy}")