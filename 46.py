'''function with return value'''

# template
# def function_name(argument):
#   function body
#   return output

# square function
def square(input_numbers):
    '''square function'''
    square_output = input_numbers**2
    return square_output
y = square(5)
print(y)
print(square(6))
z = 10 + square(7)
print(z)

# add function
def add(numbers_1,numbers_2):
    '''return function with multi input'''
    return numbers_1 + numbers_2
a = add(10,8)
print(a)

# function with multiple returns
def math_operation(numbers_1,numbers_2):
    increase = numbers_1 + numbers_2
    subtraction = numbers_1 - numbers_2
    multiplication = numbers_1 * numbers_2
    distribution = numbers_1 / numbers_2

    return increase,subtraction,multiplication,distribution
i,s,m,n = math_operation(10,5)

print(f"results increase = {i}")
print(f"results subtraction = {s}")
print(f"results multiplication = {m}")
print(f"results distribution = {n}")