# List

# number data set
data_numbers = [1,2,3]
print(data_numbers)

# string data set
data_str = ["rama","ikrama","bana"]
print(data_str)

# boolean data set
data_boolean = [True, False, True, True]
print(data_boolean)

# group data
data_group = [1,"Es Cream",2,"Mie Ayam","Rama",True,"Jojo",False]
print(data_group)

## alternative make a list
data_range = range(0,10,2) # range(start,stop,step)
print(data_range)
data_list = list(data_range)
print(data_list)

# create lists with for loops, list comprehensions
list_for = [i for i in range(0,10)]
print(list_for)
print("=== RANK TWO ==")
register_for_rank = [i**2 for i in range(0,10)]
print(register_for_rank)

# make a list using for and if
list_using_for_if = [i for i in range(0,10) if i != 5]
print(list_using_for_if)

# counting odd numbers
list_using_for_if = [i for i in range(0,10) if i%2 == 0]
print(list_using_for_if)

# counting even numbers
list_using_for_if = [i for i in range(0,10) if i%2 != 0]
print(list_using_for_if)