# Print Pattern 
# A     
# A    B
# A    B    C
# A    B    C    D


rows = int(input("Enter number of rows: "))
for i in range(rows):
    for j in range(i + 1):
        print(chr(65 + j), end=" ")
    print()


# output
# Enter number of rows: 8
# A 
# A B
# A B C
# A B C D
# A B C D E
# A B C D E F
# A B C D E F G
# A B C D E F G H