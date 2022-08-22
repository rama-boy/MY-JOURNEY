# Operations that can be performed with shortening
# Operations plus assignment

a = 5 # is assignment
print("value a =", a)

a += 1 # the meaning is a = a + 1
print("value a += 1, the value of a becomes",a)

a -= 2 # the meaning is a = a - 2
print("value a -= 2, the value of a becomes",a)

a *= 5 # the meaning is a = a * 5
print("value a *= 5, the value of a becomes",a)

a /= 2 # the meaning is a = a / 2
print("value a /= 2, the value of a becomes",a)

b = 10
print("\nvalue b =",b)

# modulus and floor division
b %= 3
print("value b %= 3, the value of b becomes",b)

b = 10
print("\nvalue b =",b)

b //= 3
print("value b //= 3, the value of b becomes",b)

# rank or exponent
a = 5
print("value a =", a)
a **= 3
print("value a**= 3, the value of a becomes",a)

# bitwise operation
# OR
c = True
print("\nvalue c =",c)
c |= False
print("value c |= False, the value of c becomes",c)
c = False
print("value c =",c)
c |= False
print("value c |= False, the value of c becomes",c)

# AND
c = True
print("\nvalue c =",c)
c &= False
print("value c &= False, the value of c becomes",c)
c = True
print("value c =",c)
c &= True
print("value c &= True, the value of c becomes",c)

# XOR
c = True
print("\nvalue c =",c)
c ^= False
print("value c ^= False, the value of c becomes",c)
c = True
print("value c =",c)
c ^= True
print("value c ^= True, the value of c becomes",c)

# slide slide
d = 0b0100
print("\nvalue d =",format(d, '04b'))
d >>= 2
print("value d >>= 2, the value of d becomes",format(d,'04b'))
d <<= 1
print("value d <<= 1, the value of d becomes",format(d,'04b'))