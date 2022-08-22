'''Default argument'''

# def function(argument):
# def function(argument = default value):

# example 1
def hello(name = "Cool"):
    '''Function with argument default'''
    print(f"Hi {name}")
hello("RAMAKUN!")
hello()

# example 2
def hi(name, message = "How are you?"):
    '''function with one common input, and one default'''
    print(f"hello {name}, {message}")
hi("Rama","Hello handsome")
hi("RAMAA")

# example 3
def calculate_rank(numbers, rank=2):
    results = numbers**rank
    return results
print(calculate_rank(2,4))
results = calculate_rank(rank=3, numbers=5)
print(results)

# example 4
def function(input1=1,input2=2,input3=3,input4=4):
    results = input1 + input2 + input3 + input4
    return results
print(function())
print(function(input3=10))