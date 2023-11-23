class Book:
    def __init__(self, title, quantity, author, price):
        self.title = title
        self.quantity = quantity
        self.author = author
        self.price = price

    def get_info(self):
        return f"Book: {self.title}, Quantity: {self.quantity}, Author: {self.author}, Price: {self.price}"
    
    def change_price(self):
        new_price=input("New Price: ")
        self.price = new_price
        return new_price

#overriding
class Overloading:
    def add(self, x, y):
        print(x+y)

    def add(self, x, y, z):
        print(x+y+z)


obj = Overloading()
obj.add(2, 3)

book1 = Book('Book 1', 12, 'Author 1', 120)
book2 = Book('Book 2', 20, 'Author 2', 200)

print(book1.get_info())
print(book2.get_info())
