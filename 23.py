# Practice

# simple calculator

print(20*"=")
print("simple calculator")
print(20*"=" + "\n")

number_1 = float(input("input number 1 = "))
operator = input("operator (+,-,x,/) : ")
number_2 = float(input("input number 2 = "))

# branching

if operator == "+":
    results = number_1 + number_2
    print(f"the result is {results}")
elif operator == "-":
    results = number_1 - number_2
    print(f"the result is {results}")
elif operator == "x" or operator == "*":
    results = number_1 * number_2
    print(f"the result is {results}")
elif operator == "/":
    results = number_1 / number_2
    print(f"the result is {results}")
else:
    print("You're wrong!")
print("END PROGRAM!")