month = input("enter the month: ")
year = int(input("enter year:"))
if month in ["january","march","may","july","august","october","december"]:
    print(f"{month} has 31 days")
elif month in ["april","june","september","november"]:
    print(f"{month} has 30 days")
elif month == "february":
    if year % 4 == 0:
        print(f"{month} has 29 days")
    else:
        print(f"{month} has 28 days")
else:
    print("Invalid month name")


# output:
# enter the month: february
# enter year:2004
# february has 29 days

# enter the month: february
# enter year:2002
# february has 28 days

# enter the month: april
# enter year:2023
# april has 30 days