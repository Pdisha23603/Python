# Given a number n, write a python program to make and print the list of Fibonacci
# series up to n. Input : n=7 Hint : first 7 numbers in the series Expected output :
# First few Fibonacci numbers are 0, 1, 1, 2, 3, 5, 8, 13

n = int(input("Enter a number: "))
a, b = 0, 1
fibonacci_series = []
for _ in range(n):
    fibonacci_series.append(a)
    a, b = b, a + b
print("First few Fibonacci numbers are:", fibonacci_series)

# output
# Enter a number: 15
# First few Fibonacci numbers are: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]