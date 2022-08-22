# operation

# index 0(-3)    1(-2)   2(-1)
data = ["rama","ikrama","bana"]

# retrieve data from this list
data_0 = data[0]
print(f"first data (index 0) = {data_0}\n")

final_data = data[-1]
print(f"the last data is = {final_data}\n")

rama_data = data[-3]
print(f"data rama is = {rama_data}\n")

# retrieve info on the amount of data in the list
data_length = len(data)
print(f"data length = {data_length}\n")

## Data list manipulation

# Add items to the list according to the position
print(f"data before addition = \n{data}\n")

data.insert(1,"robert")
print(f"data last addition = \n{data}\n")

# Add at the end of the list
data.append("sukro")
print(f"add data at the end = \n{data}\n")

# add list with list
new_data = ["Gesya","Marco","Pedro"]
data.extend(new_data)
print(f"combined data = \n{data}\n")

# change data
# we change data 2(bana) into new data(Zeus)
data[2] = "Zeus"
print(f"new data change = \n{data}\n")

# remove data
data.remove("Zeus")
print(f"remove data = \n{data}\n")

# remove the last data
data.pop()
print(f"last data = \n{data}\n")

last_data = data.pop()
print(f"last data (2) = \n{data}\n")
print(last_data)