# Comparison and Logic Exercises

# Create a composite range area from numbers

# ++++++3--------10++++++

inputUser = float(input("enter a number that is\nless than 3\nor \ngreater than 10\n:"))

# ++++++3----------------
# Check numbers less than 3
isLessThan = (inputUser < 3)
print("Less than 3 =", isLessThan)

# ----------------+++++10
# Check number more than 10
isMoreThan = (inputUser > 10)
print("More than 10 =", isMoreThan)

# ++++++3--------10++++++

isCorrect = isLessThan or isMoreThan
print("the number you entered: ", isCorrect)


# ------3++++++++10------
# slice case
print("\n",10*"=","\n")
inputUser = float(input("enter a number that is\ngreater than 3\nand \nless than 10\n:"))

# ---------3++++++++++++++
# more than 3
isMoreThan = inputUser > 3
print("More Than 3 = ", isMoreThan)

# +++++++++++++10---------
# less than 10
isLessThan = inputUser < 10
print("Less Than 10 = ", isLessThan)

# ------3++++++++10------
isCorrect = isLessThan and isMoreThan
print("the number you entered: ", isCorrect)