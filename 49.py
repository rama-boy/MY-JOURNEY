'''Type Hints on Functions'''

# the standard form of the function we have studied

'''case study
def function(parameter):
    results = parameter**2
    print(results)
function(1)
function("Rama")
function(True)
'''


import string
def ten_rank(argument:int) -> int:
    '''function with hints'''
    output = 10**argument
    return output
RESULTS = ten_rank(2)
print(RESULTS)

def display(argument:string):
    print(argument)
display("Rama")