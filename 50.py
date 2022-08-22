'''*args on function'''

# input data or argument

def function(name,tall,weight):
    print(f"{name} tall body is {tall} weight body {weight}")
function("Rama",175,60)

def function(data_list):
    data = data_list.copy()
    name = data[0]
    tall = data[1]
    weight = data[2]
    print(f"{name} tall body is {tall} weight body {weight}")
function(["Budi",178,67])

# acquaintance with *args

def function(*args):
    name = args[0]
    tall = args[1]
    weight = args[2]
    print(f"{name} tall body is {tall} weight body {weight}")
function("Rama1",178,56)

# case study

def increase(*data):
    # data type is tuple, and data can be iterated
    output = 0
    for number in data:
        output += number
    return output
results = increase(1,2,3,4,5,6,7,8,9)
print(f"results is a = {results}")
results = increase(10,5,15)
print(f"results is a = {results}")