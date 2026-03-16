#  enter month name from user & display days accoundly (using match case with in operator)

# month = input("enter month name: ")
# match month:
#     case month if month in ("january","march","may","july","august","october","december"):
#         print("31 days")
#     case month if month in ("april","june","september","november"):
#         print("30 days")
#     case month if month == "february":
#         print("28 or 29 days")
#     case _:
#         print("invalid month name")

# 2.1 advance version

year = int(input("enter the year: "))
month = input("enter the month: ").lower()
match month:
    case month if month in ("january","march","may","july","august","october","december" ):
        print("31 days")

    case month if month in ("april","june", "september","november"):
        print("30 days")
    case "february":
      if(year%4==0):
        print("29 days")
      else:
        print("28 days")
    case _ : 
        print("invalid month name")

    
