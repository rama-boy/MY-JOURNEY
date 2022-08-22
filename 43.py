import datetime
import os
import string
import random
# Dictionary Practice

# student dict template
student_template = {
    'name':'name',
    'nim':'00000000',
    'sks_graduated':0,
    'born':datetime.datetime(1111,1,11),
}

student_data = {}


while True:
    os.system("cls")
    # os.system("clear") for linux or MAC 
    print(f"{'WELCOME':^20}")
    print(f"{'STUDENT DATA':^20}")
    print("-"*20)

    student = dict.fromkeys(student_template.keys())
    student['name'] = input("Student Name: ")
    student['nim'] = input("Student NIM: ")
    student['sks_graduated'] = int(input("Student SKS: "))
    BORN_YEAR = int(input("Years Born (YYYY): "))
    BORN_MONTH = int(input("Month Born (1-12): "))
    BORN_DATE = int(input("Date Born (1-31): "))
    student['born'] = datetime.datetime(BORN_YEAR,BORN_MONTH,BORN_DATE)

    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))
    student_data.update({KEY:student})

    print(f"\n{'KEY':<6} {'Name':<17} {'NIM':<10} {'Graduate SKS':<10} {'Born':^9}")
    print("-"*60)

    for student in student_data:
        KEY = student

        NAME = student_data[KEY]['name']
        NIM = student_data[KEY]['nim']
        SKS = student_data[KEY]['sks_graduated']
        BORN = student_data[KEY]['born'].strftime("%x")

        print(f"{KEY:<6} {NAME:17} {NIM:<8} {SKS:^10} {BORN:^10}")
    
    print("\n")
    is_done = input("Is it done? (y/n) ")
    if is_done == "y":
        break
print("\nEND PROGRAM, Thanks You!")