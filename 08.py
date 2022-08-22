# arithmetic operations

from unittest import result


a = 10
b = 3

print("=== add operation(+) ===")
result = a + b
print(a,'+',b,'=',result)

print("=== operation subtraction(-) ===")
result = a - b
print(a,'-',b,'=',result)

print("=== multiplication operation(*) ===")
result = a * b
print(a,'*',b,'=',result)

print("=== distribution operation(/) ===")
result = a / b
print(a,'/',b,'=',result)

print("=== exponential operation(**) ===")
result = a ** b
print(a,'**',b,'=',result)

print("=== modulus operation(%) ===")
result = a % b
print(a,'%',b,'=',result)

print("=== floor division operation(//) ====")
result = a // b
print(a,'//',b,'=',result)

# operation priority, operational precedence

'''
    1. ()
    2. exponential **
    3. multiplication and more * / **, %, // 
    4. add and subtraction + -
'''
x = 3
y = 2
z = 4

result = x ** y * (z + x) / y - y % z // x
print(x,'**',y,'*',z,'+',x,'/',y,'-',y,'%',z,'//',x,'=',result)

result = x + y * z
print(x,'+',y,'*',z,'=',result)

# in brackets count first ()
result = (x + y) * z
print('(',x,'+',y,')*',z,'=',result)