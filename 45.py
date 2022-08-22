'''Functions with arguments (input)'''

# Template
# def function_name(argument):
#   Function body

def hello_world(name):
    '''hello world function accepts input with variable name'''
    print(f"welcome to the world oh {name}")
hello_world("rama")


# add-on program

def add(numbers_1,numbers_2):
    '''add function'''
    results = numbers_1 + numbers_2
    print(f"{numbers_1} + {numbers_2} = {results}")
add(1,5)

def hi(participant_list):
    '''hi function'''
    participant_data = participant_list.copy()
    for participant in participant_data:
        print(f"dear {participant}")
members = ["rama","rama2","rama3"]
hi(members)