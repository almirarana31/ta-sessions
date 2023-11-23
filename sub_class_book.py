from main_class import Book

#inheritance
class Novel(Book):
    def __init__(self, title, quantity, author, price, pages):
        super().__init__(title, quantity, author, price)
        self.pages = pages


class Academic(Book):
    def __init__(self, title, quantity, author, price, branch):
        super().__init__(title, quantity, author, price)
        self.branch = branch

#abstraction
class Report(Book):
    def cover(self):
        pass

class New(Report):
    def cover(self):
        print("There is no cover")

novel1 = Novel('Novel 1', 5, 'Novel Author 1', 100, 20)
academic1 = Academic('Study 1', 20, 'Author 2', 1000, 'CS')

print(novel1.get_info())
print(academic1.get_info())

#polymorphism
novel1.change_price()
print(novel1.get_info())

report1 = Report()
report1.cover_type()

abstract_cover = New()   
abstract_cover.cover()   



