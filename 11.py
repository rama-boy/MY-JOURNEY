# logical or boolean operations

# not, or, and, xor

# NOT
from operator import xor


print('==== NOT ====')
a = False
c = not a
print('data a =',a)
print('---- NOT ----')
print('data c = c',c)

# OR (if one is true, then the result is true)
print('==== OR ====')
a = False
b = False
c = a or b
print(a,'OR',b,'=',c)
a = False
b = True
c = a or b
print(a,'OR',b,' =',c)
a = True
b = False
c = a or b
print(a,' OR',b,'=',c)
a = True
b = True
c = a or b
print(a,' OR',b,' =',c)

# AND (if two values are true, then the result is true)
print('==== AND ====')
a = False
b = False
c = a and b
print(a,'AND',b,'=',c)
a = False
b = True
c = a and b
print(a,'AND',b,' =',c)
a = True
b = False
c = a and b
print(a,' AND',b,'=',c)
a = True
b = True
c = a and b
print(a,' AND',b,' =',c)

# XOR (will be true if one is true, the rest is false)
print('==== XOR ====')
a = False
b = False
c = a ^ b
print(a,'XOR',b,'=',c)
a = False
b = True
c = a ^  b
print(a,'XOR',b,' =',c)
a = True
b = False
c = a ^  b
print(a,' XOR',b,'=',c)
a = True
b = True
c = a ^  b
print(a,' XOR',b,' =',c)