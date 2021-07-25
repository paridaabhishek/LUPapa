import datetime as dt

todaysDate = dt.date.today().strftime('%Y-%m-%d')
print(todaysDate)
print(dt.date.today().weekday())

if str(dt.date.today().weekday()) in '01234':
    print('Haha')
else:
    print('HoHo')