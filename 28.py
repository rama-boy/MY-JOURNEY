# Practice to make triangles

from re import A


side = 10

# 1. Using for

# Dummy variable
print("=== START FOR ===")
count = 1
for i in range(side):
	print("*"*count)
	count += 1
print("=== END OF FOR ===\n")

# 2. Use while
print("=== START WHILE ===")
count = 1
while True:
	print("*"*count)
	count += 1
	if count > side:
		break
print("=== END OF WHILE ===\n")

# 3. Just odd
print("=== START WHILE ===")
count = 1
while True:
    
    if ~(count%2):
        # print if odd
        print("*"*count)
        count += 1
    else:
        # will return to the top if odd
        count += 1
        continue

    # will break if count exceeds side
    if count > side:
        break
print("=== END OF WHILE ===\n")

# 4. Just odd
print("=== START WHILE ===")
count = 1
space = int(side/2)

while True:
    
    if (count%2):
        # print if odd
        print(" "*space,"*"*count)
        space -= 1
        count += 1
    else:
        # will return to the top if odd
        count += 1
        continue

    # will break if count exceeds side
    if count > side:
        break
print("=== END OF WHILE ===\n")

# inverted triangle
print("=== INVERTED TRIANGLE ===")
for i in range(5, 0, -1):
    print(" "*(5-i), end='')
    for x in range(i):
        print("+ ", end='')
    print()
print("=== INVERTED TRIANGLE ===")