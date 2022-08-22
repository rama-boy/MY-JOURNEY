# continue, pass, break

# pass -> he functions as a dummy, will not be executed

# number = 0

# while number < 5:
#    number += 1
    
#    if number == 3:
#        pass # will not be executed
#    print(number)

# continue
number = 0
print(f"number now -> {number}")

while number < 5:
    number += 1
    print(f"number now -> {number}") # action 1
    
    if number == 3:
        print("START! START!")
        continue # will make the loop jump to the next step

    print("Hello") # action 2
    
print("END PROGRAM")