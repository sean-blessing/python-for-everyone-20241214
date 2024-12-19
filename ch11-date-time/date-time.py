print('Welcome to date times!')
from datetime import date, time, datetime, timedelta

date_now = date.today()
datetime_now = datetime.now()
time_only = time(14, 30)

print(f'date_now = {date_now}')
print(f'datetime_now = {datetime_now}')
print(f'time_only = {time_only}')

halloween = date(2025,10,31)
appointment = datetime(2024, 12, 25, 7, 00, 00)

print(f'halloween: {halloween}')
print(f'appointment: {appointment}')

new_years_eve = datetime.strptime("12/31/2024", "%m/%d/%Y")
print(f'new_years_eve: {new_years_eve}')

end_of_class = datetime.strptime("12/19/24 14:30", "%m/%d/%y %H:%M")
print(f'end_of_class = {end_of_class}')

print(f'end_of_class (12HR): {end_of_class:%Y-%m-%d %I:%M %p}')
date_format = "%Y-%m-%d"
time_format = "%I:%M %p"
print(f'new_years_eve (12HR): {new_years_eve:{date_format} {time_format}}')

print('===== timedelta objects p. 310 =====')
three_weeks = timedelta(weeks = 3)
three_weeks_from_today = datetime.today() + three_weeks
print(f'three_weeks_from_today: {three_weeks_from_today}')

time_span_until_halloween = halloween - date_now
print(f'timespan until halloween - days: {time_span_until_halloween.days}')

print(f'days until halloween: {(halloween - date_now).days}')

print(f'Getting time parts - p. 316')
print(f'end_of_class - year: {end_of_class.year}')
print(f'end_of_class - hour: {end_of_class.hour}')
print(f'end_of_class - time: {end_of_class.time()}')

# date comparisons
if end_of_class < appointment:
    print('end of class is before appointment')

print('bye')