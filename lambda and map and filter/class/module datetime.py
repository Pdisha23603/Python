# classes: 
import datetime
print(datetime.date.today()) #give only date
print(datetime.datetime.now()) #give date and time both
cur_now = datetime.datetime.now()
# print(cur_now.year())
print(cur_now.day())

# print(cur_now.strftime("%d / %m / %y")) # small y give last 2 digit of year
print(cur_now.strftime("%d : %m : %Y")) # big Y gives whole year
# print(cur_now.strftime("%D / %M / %Y")) # big Y gives whole year

