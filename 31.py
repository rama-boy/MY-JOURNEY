data_numbers = [1,5,1,4,3,2,4,3,2,3,7,8,9,0]
print(f"data numbers = \n{data_numbers}")

# count data
amount_data_4 = data_numbers.count(4)
amount_data_3 = data_numbers.count(3)
print(f"amount numbers 4 = {amount_data_4}")
print(f"amount numbers 3 = {amount_data_3}")

# take data position (index)
data = ["Rama","Ikrama","Zeus","Athena"] # start calculation from 0
print(f"data = {data}")

index_zeus = data.index("Zeus")
print(f"index zeus = {index_zeus}")
index_athena = data.index("Athena")
print(f"index athena = {index_athena}\n")

# sort list
print(f"numeric data before sorting = \n{data_numbers}\n")
data_numbers.sort()
print(f"number data sort = \n{data_numbers}\n")

# sorted alphabetically
print(f"data = {data}")
data.sort()
print(f"data sort = {data}\n")

# back to the list
data_numbers.reverse()
data.reverse()
print(f"data reverse = \n{data_numbers} \n{data}") # sorted from smallest to largest