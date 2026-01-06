# Print even numbers fall between 2 given numbers E.g user enter 10 20 
# output 12,14,16,18

start = int(input("enter the starting no: "))
end = int(input("enter the ending no: "))
for i in range(start,end):
    if i % 2==0:
        print(f"{i}",end=",")

# output
# enter the starting no: 10
# enter the ending no: 20
# 10,12,14,16,18,