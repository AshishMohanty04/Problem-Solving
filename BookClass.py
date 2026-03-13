class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def getDetails(self):
        return f"Title: {self.title}, Author: {self.author}, Price: {self.price}"

# Example
book1 = Book("Python Basics", "Ashish Mohanty", 499)
print(book1.getDetails())
