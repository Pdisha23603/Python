# count total_no of prime and not prime number in 1 to 100

a = int(input("enter the starting range: "))
b = int(input("enter the ending range: "))
prime_count = 0
notprime_count = 0
for num in range(a,b):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                notprime_count +=1
                break
            else:
                prime_count += 1
    else:
        notprime_count += 1
print("Total prime number:",prime_count)
print("Total prime number:",notprime_count)


# enter the starting range: 1
# enter the ending range: 100
# Total prime number: 1059
# Total prime number: 74