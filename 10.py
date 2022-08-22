# comparison operation

#every result of the comparison operation is a boolean

# >,<,>=,<=,==,!=,is,is not

a = 4
b = 2

# greater than >
print('=== greater than (>) ===')
result = a > 3
print(a,'>',3,'=',result)
result = b > 3
print(b,'>',3,'=',result)
result = b > 2
print(b,'>',2,'=',result)

# less than <
print('=== less than (<) ===')
result = a < 3
print(a,'<',3,'=',result)
result = b < 3
print(b,'<',3,'=',result)
result = b < 2
print(b,'<',2,'=',result)

# more than equal to >=
print('=== more than equal to (>=) ===')
result = a >= 3
print(a,'>=',3,'=',result)
result = b >= 3
print(b,'>=',3,'=',result)
result = b >= 2
print(b,'>=',2,'=',result)

# less than equal to <=
print('=== less than equal to (<=) ===')
result = a <= 3
print(a,'<=',3,'=',result)
result = b <= 3
print(b,'<=',3,'=',result)
result = b <= 2
print(b,'<=',2,'=',result)

# together with (==)
print('=== together with (==) ====')
result = a == 4
print(a,'==',4,'=',result)
result = b == 4
print(b,'==',4,'=',result)

# not equal to (!=)
print('=== not equal to (!=) ====')
result = a != 4
print(a,'!=',4,'=',result)
result = b != 4
print(b,'!=',4,'=',result)

# 'is' as a comparison object identity
print('=== object identity (is) ====')
x = 5 # this is assignment to create object
y = 5
print('value x =',x,',id = ',hex(id(x)))
print('value y =',y,',id = ',hex(id(y)))
result = x is y
print('x is y =',result)

x = 5 # this is assignment to create object
y = 6
print('value x =',x,',id = ',hex(id(x)))
print('value y =',y,',id = ',hex(id(y)))
result = x is y
print('x is y =',result)

print('=== object identity (is not) ====')
x = 5 # this is assignment to create object
y = 5
print('value x =',x,',id = ',hex(id(x)))
print('value y =',y,',id = ',hex(id(y)))
result = x is not y
print('x is y =',result)

x = 5 # this is assignment to create object
y = 6
print('value x =',x,',id = ',hex(id(x)))
print('value y =',y,',id = ',hex(id(y)))
result = x is not y
print('x is y =',result)