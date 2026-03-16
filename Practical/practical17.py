# Write a python program using function to find the sum of odd series and even series
# Odd series: 12/ 1! +32/ 3! + 52/ 5!+……n
# Even series: 22/ 2! + 42/ 4! + 62/ 6!+……n\

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def sum_of_odd_series(n):
    odd_sum = 0
    for i in range(1, n + 1, 2):
        odd_sum += (i ** 2) / factorial(i)
    return odd_sum

def sum_of_even_series(n):
    even_sum = 0
    for i in range(2, n + 1, 2):
        even_sum += (i ** 2) / factorial(i)
    return even_sum
n = int(input("Enter a number: "))
print("Sum of odd series is:", sum_of_odd_series(n))
print("Sum of even series is:", sum_of_even_series(n))


# output
# Enter a number: 10
# Sum of odd series is: 1.0
# Sum of even series is: 1.0
