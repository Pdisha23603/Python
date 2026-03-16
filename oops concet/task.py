# create book class. contain title, author, price, no of pages and display method.

class Book:
    def __init__(self,title,author,price,no_page):
        self.title=title
        self.author=author
        self.price=price
        self.no_page=no_page

    def Details(self):
        print(self.title,self.author,self.price, self.no_page)

obj1 = Book("book1","author1",234,235)
obj1.Details()

obj2 = Book("book2","author2",254,453)
obj2.Details()
