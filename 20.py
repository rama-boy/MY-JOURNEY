# date and time (practice)

import datetime as dt

print("Please enter your date, \nmonth and year of birth \n")
date = int(input("Date \t\t: "))
month = int(input("Month \t\t: "))
year = int(input("Year \t\t: "))

date_of_birth = dt.date(year,month,date)
print(f"Your date of birth is : {date_of_birth}")


today = dt.date.today()
print(f"Today's date: {today}")
day_age = today - date_of_birth
years_old = day_age.days // 365
remaining_month = (day_age.days % 365) // 30
print(f"The day is : {date_of_birth:%A}")
print(f"Your age is: {years_old} year, {remaining_month} month")