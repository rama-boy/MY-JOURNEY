# bitwise operators, binary operation

a = 9
b = 5

# bitwise OR (|)
c = a | b
print('\n=====OR=====')
print('value :',a,' , binary :',format(a,'08b'))
print('value :',b,' , binary :',format(b,'08b'))
print('------------ (|)')
print('value :',c,', binary :',format(c,'08b'))

# bitwise AND (&)
c = a & b
print('\n=====AND=====')
print('value :',a,' , binary :',format(a,'08b'))
print('value :',b,' , binary :',format(b,'08b'))
print('------------ (&)')
print('value :',c,' , binary :',format(c,'08b'))

#bitwise XOR (^)
c = a ^ b
print('\n=====XOR=====')
print('value :',a,' , binary :',format(a,'08b'))
print('value :',b,' , binary :',format(b,'08b'))
print('------------- (^)')
print('value :',c,' , binary :',format(c,'08b'))

# bitwise NOT (~)
c = ~a
print('\n=====NOT=====')
print('value :',a,' , binary :',format(a,'08b'))
print('------------- (~)')
print('value :',c,', binary :',format(c,'08b'))
print('------------- (^)')
d = 0b0000001001
e = 0b1111111111
print('value :',e^d,'  , binary :',format(e^d,'08b'))

#shifting

# shift right (>>)
c = a >> 2
print('\n=====>>=====')
print('value :',a,' , binary :',format(a,'08b'))
print('------------- (>>)')
print('value :',c,', binary :',format(c,'08b'))

# shift left (<<)
c = a << 2
print('\n=====>>=====')
print('value :',a,' , binary :',format(a,'08b'))
print('------------- (>>)')
print('value :',c,', binary :',format(c,'08b'))