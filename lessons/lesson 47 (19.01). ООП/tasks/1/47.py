class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    def open(self):
        print(f"Книга {self.title} открыта на первой странице")
    def read(self):
        print(f"Читаем книгу {self.title} автора {self.author}")
    def close(self):
        print(f"Книга {self.title} закрыта")
    def info(self):
        print(f"{self.title} - {self.author}, {self.pages} стр")
my_book = Book("1984", "Джордж Оруэлл", "328")
my_book.open()
my_book.read()
my_book.close()
my_book.info()

print(my_book.title, my_book.author,my_book.pages)
