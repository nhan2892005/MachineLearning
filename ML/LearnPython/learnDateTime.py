import datetime

today = datetime.datetime.now()

print(datetime.__file__)

#Name of weekday
d = today.strftime("%A, %B %d, %Y")
print(d)
# dd/mm/YY
d1 = today.strftime("%d/%m/%Y")
print("d1 =", d1)
# Textual month, day and year	
d2 = today.strftime("%B %d, %Y")
print("d2 =", d2)
# mm/dd/y
d3 = today.strftime("%m/%d/%y")
print("d3 =", d3)
# Month abbreviation, day and year	
d4 = today.strftime("%b-%d-%Y")
print("d4 =", d4)
# dd/mm/YY H:M:S
dt_string = today.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)

del today

createDay = datetime.datetime(2005,9,28)
d = createDay.strftime("%A")
print(d)