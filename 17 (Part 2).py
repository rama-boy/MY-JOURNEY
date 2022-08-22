# operator in form method

## change case of string

# change everything to upper case

from doctest import Example
from turtle import left, title


regards = "hello bro!"
print("normal = " + regards)
regards = regards.upper()
print("upper = " + regards)

# change everything to lower case
ngalay = "gW GaNTeNgGzz BinGiTTzZz"
print("normal = " + ngalay)
ngalay = ngalay.lower()
print("lower = " + ngalay)

## checking with isX Method

# lower case checking example
regards = "wasap broh"
is_lower = regards.islower() # result is boolean
print(regards + " is lower = " + str(is_lower))
is_upper = regards.isupper() # result is boolean
print(regards + " is upper = " + str(is_upper))

# isalpha()   <-- to check all letters
# isalnum()   <-- letters and numbers
# isdecimal() <-- numbers only
# isspace()   <-- spasi, tab, newline\n
# istitle()   <-- all words start with a capital letter

title = "Ternyata Mertuaku Adalah Ibumu"
check_title = title.istitle() # result is boolean
print(title + " is title = " + str(check_title))

## check components startswith() endswith() <-- impressive
check_start = "Rama Go".startswith("Rama Go")
print("start = " + str(check_start))

check_end = "Rama Go".endswith("Go")
print("end = " + str(check_end))

## merge component join() split()
separate = ['aku','seorang','kapiten']
combined = ','.join(separate)
print(separate)
print(combined)

combined = ' '.join(separate)
print(combined)

combined = ' yosh '.join(separate)
print(combined)

combined = 'akuyoshseorangyoshkapiten'
print(combined.split('yosh'))

## character allocation rjust(), ljust(), center()
right = "right".rjust(10)
print("'"+right+"'")

left = "left".ljust(10)
print("'"+left+"'")

center = "center".center(20,":")
print("'"+center+"'")

# the opposite -> strip()
center = center.strip(":") # remove mark (:)
print("'"+center+"'")

# capitalize() = Change words with lowercase letters to uppercase
text = 'rama ganteng'.capitalize()
print(text)

# casefold() = returns all characters where all characters are lowercase
text = "RAMA GANTENG BANGETSSS".casefold()
print(text)