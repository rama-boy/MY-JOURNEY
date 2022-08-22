# string recognition
data = "this is a string"
print(data)
print(type(data))

# how to make strings

'''
    1. by using single quote '...'
    2. by using double quote "..."
'''

data = 'use single quote'
print(data)

data = 'use double quote'
print(data)

print('"Hello, how are you sir?"')
print("'Hello, how are you sir?'")
print("it's friday")

# 2. use the sign \

# make the ' sign into a string
print('it\'s okay enough I\'m waiting for you')
print('g\'day, isn\'t it?')

# backlash
print("C:\\user\\rama")

# tab
print("rama\tikrama, be far away")

# backspace
print("rama \bikrama, get close")

# newline
print("first line, \nsecond line.") # LF -> line feed -> unix, macos, linux
print("first line, \rsecond line.") # CR -> carriage return -> commodore, acorn, lisp
print("first line, \r\nsecond line.") # CRLF -> line feed carriage return -> windows

# 3. string literal or raw

print('C:\new folder') # the path will be wrong !

# using raw strings
print(r'C:\new folder')

# multiline literal string
print("""
Name : Rama
Age : 19
""")

# multiline literal string and RAW
print(r"""
Name : Rama
Age : 19
Website : www.ramarama.com/NewID
""")