'''Function exercise'''
# Program to calculate area and around of rectangle

# create program headers
import os
# os.system("cls")

# print(f"{'AREA CALCULATION PROGRAM':^40}")
# print(f"{'AND AROUND OF RECTANGLE':^40}")
# print(f"{'-'*40:^40}")

# # take user input
# WIDTH = int(input("Input width value: "))
# LONG = int(input("Input long value: "))

# # program area calculate
# AREA = LONG*WIDTH
# AROUND = 2*(LONG+WIDTH)

# # show the results
# print(f"area calculation result = {AREA}")
# print(f"around calculation result = {AROUND}")


def header():
    '''function headers'''
    os.system("cls")
    print(f"{'AREA CALCULATION PROGRAM':^40}")
    print(f"{'AND AROUND OF RECTANGLE':^40}")
    print(f"{'-'*40:^40}")

def input_user():
    '''function user input'''
    width = int(input("Input width value: "))
    long = int(input("Input long value: "))
    return width,long  

def calculate_area(width,long):
    '''area function'''
    return width*long 

def around_calculate(width,long):
    '''function around calculate'''
    return 2*(width + long)   

def display(message,value):
    '''display function'''
    print(f"the calculation results {message} = {value}")

# MAIN PROGRAM
while True:
    header()
    WIDTH,LONG = input_user()
    AREA = calculate_area(WIDTH,LONG)
    AROUND = around_calculate(WIDTH,LONG)

    display("area", AREA)
    print("around", AROUND)

    isContinue = input("what's next? (y/n) ")
    if isContinue == "n":
        break

print("END PROGRAM, THANK!")