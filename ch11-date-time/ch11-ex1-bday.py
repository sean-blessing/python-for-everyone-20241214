from datetime import date, datetime
print('Birthday Calculator\n')
name = input("Enter name: ")
bdate_str = input("Enter birthday (MM/DD/YY): ")
birthdate = datetime.strptime(bdate_str, "%m/%d/%y")
today = datetime.today()
date_format = "%A, %B %d, %Y"
print(f'Birthday: {birthdate:{date_format}}')
print(f'Today:    {today:{date_format}}')
age = (today-birthdate).days
years = age // 365
print(f'{name} is {years} years old.')
# add get mm and dd of bdate, add 1 to yy and create next_bday
bday_mm = birthdate.month
bday_dd = birthdate.day
current_yy = today.year
next_bday = datetime(current_yy+1, bday_mm, bday_dd)
days_until_bday = (next_bday-today).days
if days_until_bday >= 365:
    days_until_bday -= 365
print(f"{name}'s birthday is in {days_until_bday} days.")
print('Bye')