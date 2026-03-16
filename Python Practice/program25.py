# Print Pattern
# ****
# ***
# **
# *

num = int(input("enter the number: "))
for i in range(num): # i means row and j means colums
    for j in range(num,i,-1):
        print("*", end=" " ) # or print("*", end="\t")
    print()


# output
# enter the number: 6
# * * * * * *
# * * * * *
# * * * *
# * * *
# * *
# *