# Break

number = 0

while number == 5:
    number += 1
    print(f"number now -> {number}") # action 1
    
    if number == 3:
        print("START! START!")
        break 

    print("Hello") # action 2
    
print("END PROGRAM")

# example (2)
data_int = int(input("count to = "))
number = 0

while True:
    number += 1
    print(f"number now -> {number}") # action 1
    
    if number == data_int:
        print("START! START!")
        break 

    print("Hello") # action 2
    
print("END PROGRAM")