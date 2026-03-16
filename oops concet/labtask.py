# book example dynamic -- ask from user
#  no of book ask from user only


books = []

num = int(input("Enter number of books: "))


for i in range(num):
    print(f"\nEnter details for Book {i+1}")
    
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")
    price = float(input("Enter Price: "))
    

    book = {
        "Title": title,
        "Author": author,
        "Price": price
    }
    
    books.append(book)
    # books += [book] 

print("\n   Book List  ")
for i, book in enumerate(books, start=1):
    print(f"\nBook {i}")
    print("Title :", book["Title"])
    print("Author:", book["Author"])
    print("Price :", book["Price"])

print(books)
