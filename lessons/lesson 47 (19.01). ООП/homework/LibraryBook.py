#1
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

     def open(self):
        print(f'Книга "{self.title}" открыта на первой странице.')

     def read(self):
         print(f'Читаем книгу "{self.title}" автора {self.author}.')

     def close(self):
         print(f'Книга "{self.title}" закрыта.')

     def info(self):
         print(f'"{self.title}" - {self.author}, {self.pages} стр.')

my_book = Book("1984", "Джордж Оруэлл", 328)
my_book.info()
my_book.open()
my_book.read()
my_book.close()

#2
class BankAccount:
    interest_rate = 0.05
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        if not amount:
            print("Некорректная сумма")
        else:
            self.balance += amount
    def withdraw(self, amount):
        if not amount:
            print("Некорректная сумма")
        if self.balance < amount:
            print("Недостаточно средств")
        self.balance -= amount
        
    @staticmethod
    def is_valid_amount(amount):
        if sum(amount) > 0
        return True
    
    @classmethod
    def set_interest_rate(cls, new_rate):
        cls.interest_rate = new_rate
        print(f"Процентная ставка изменена на {cls.interest_rate}")

shet1 = BankAccount("Наталья", 100000)
shet2 = BankAccount("Софья", 500)

shet1.deposit(50000)  
shet1.withdraw(1000) 

BankAccount.set_interest_rate(0.07)

shet2.deposit(30)   
shet2.withdraw(150) 

print(f"Баланс первого счета: {shet1.balance}")
print(f"Баланс второго счета: {shet2.balance}")

#3
class LibraryBook(Book):
    def __init__(self, reader=None):
        self.reader = reader
    def take(self, name):
        if self.reader is not None:
            print("Книга уже выдана")
        else:
            self.reader = name
            print(f"Книга выдана: {name}")

    def return_back(self):
        if self.reader is None:
            print("Книга и так в библиотеке")
        else:
            self.reader = None
            print("Книга возвращена")

