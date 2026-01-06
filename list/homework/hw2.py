# check the list contains valid mobile number or not

lst = ["test1234", "1234567890","9090909090",4567890,9876543211,"45654","3345testwe"]
for i in lst:
    mo = str(i)
    if mo.isdigit() and len(mo) == 10:
        print(f"{mo} is a valid mobile number")
    else:
        print(f"{mo} is not a valid mobile number")
        

# output
# test1234 is not a valid mobile number 
# 1234567890 is a valid mobile number
# 9090909090 is a valid mobile number
# 4567890 is not a valid mobile number
# 9876543211 is a valid mobile number
# 45654 is not a valid mobile number
# 3345testwe is not a valid mobile number   
