# looping from list

# for loop
print("=== FOR LOOP ===")
set_of_numbers = [4,3,2,5,6,1]
for numbers in set_of_numbers:
    print(f"numbers = {numbers}")

participant = ["Rama","Ikrama","Athena","Zeus","Hercules"]
for name in participant:
    print(f"name = {name}")
    
# for loop and range
print("\n=== FOR LOOP AND RANGE ===")
set_of_numbers = [10,5,4,2,6,5]
length = len(set_of_numbers)
for i in range(length):
    print(f"numbers = {set_of_numbers[i]}")
    
# while
print("\n=== WHILE LOOP ===")
set_of_numbers = [10,5,4,2,6,5]
length = len(set_of_numbers)
i = 0
while i < length:
    print(f"numbers = {set_of_numbers[i]}")
    i += 1
    
# list comprehension
print("\n=== LIST COMPREHENSION ===")
data = ["Rama",1,2,3,"Ikrama"]
[print(f"data = {i}") for i in data]

print("=== SQUARE NUMBERS ===")
numbers = [10,5,4,2,6,5]
square_number = [i**2 for i in numbers]
print(square_number)

# enumerate
print("\n=== ENUMERATE ===")
list_data = ["Rama",1,2,3,"Ikrama"]
for index,data in enumerate(list_data):
    print(f"index = {index}, data = {data}")