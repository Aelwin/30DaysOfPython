from datetime import datetime, date

now = datetime.now()
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
second = now.second
timestamp = now.timestamp()

print(now)
print(now.strftime("%d/%m/%Y, %H:%M:%S"))

date_string = "5 December, 2019"
print(date_string)
print(datetime.strptime(date_string, "%d %B, %Y"))

d = date(2020, 1, 1)
print(d)
print('Current date:', d.today())
# date object of today's date
today = date.today()
print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)

another_date = date(1983, 10, 5)
print(f"Han pasado {today - another_date} desde que nací")