# Width and multiline

# data

name_data = "Rama Ikrama"
age_data = 19
high_data = 170
shoe_number_data = 43

# string standard
data_string = f"Name = {name_data}, Age = {age_data}, High = {high_data}, Shoe = {shoe_number_data}"
print(5*"="+" Data String "+5*"=")
print(data_string)

# string multiline (by using enter, newline, \n)
data_string = f"Name = {name_data},\nAge = {age_data},\nHigh = {high_data},\nShoe = {shoe_number_data}"
print("\n"+5*"="+" Data String "+5*"=")
print(data_string)

# string multiline (quote triplets)
data_string = f"""Name = {name_data}
Age  = {age_data}
High = {age_data}
Shoe = {shoe_number_data}
"""
print("\n"+5*"="+" Data String "+5*"=")
print(data_string)

# set width
name_data = "Rama"
data_string = f"""
Name = {name_data:>5}
Age  = {age_data:>5}
High = {age_data:>5}
Shoe = {shoe_number_data:>5}
"""
print("\n"+5*"="+" Data String "+5*"=")
print(data_string)