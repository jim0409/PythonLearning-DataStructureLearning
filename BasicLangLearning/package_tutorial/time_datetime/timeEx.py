from datetime import datetime,timedelta

a=1
b=2

crit =True

c = a if crit else b

print(c)

first_day = datetime(1989,4,9)
second_day = first_day - timedelta(10)
print(first_day)
print(second_day)