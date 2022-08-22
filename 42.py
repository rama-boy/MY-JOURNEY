# Multi keys & Nesting Dictionary

import datetime

student1 = {
    'name': 'rama',
    'nim': '21562020019',
    'graduated_sks': 130,
    'scholarship': False,
    'born': datetime.datetime(2001, 4, 10)
}

student2 = {
    'name': 'bana',
    'nim': '21562020017',
    'graduated_sks': 140,
    'scholarship': True,
    'born': datetime.datetime(2002, 10, 10)
}

student3 = {
    'name': 'ramaboy',
    'nim': '21562020014',
    'graduated_sks': 100,
    'scholarship': False,
    'born': datetime.datetime(2000, 3, 29)
}

student_data = {
    'STD001': student1,
    'STD002': student2,
    'STD003': student3,
}

print(f"{'KEY':<6} {'Name':17} {'SKS':<3} {'Scholarship':<9} {'Born':<10}")
print("-"*50)

for student in student_data:
    KEY = student

    NAME = student_data[KEY]['name']
    NIM = student_data[KEY]['nim']
    SKS = student_data[KEY]['graduated_sks']
    SCHOLARSHIP = student_data[KEY]['scholarship']
    BORN = student_data[KEY]['born'].strftime("%x")

    print(f"{KEY:<6} {NAME:17} {SKS:<3} {SCHOLARSHIP:^9} {BORN:<10}")
