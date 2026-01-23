Дней на выполнение: 2

result: 60/100

1) **Сильные стороны**
- Класс `Book` реализован корректно, все методы выводят требуемые строки с использованием f-строк.
- В классе `BankAccount` правильно определены атрибут класса `interest_rate`, метод `set_interest_rate` как классовый метод и используется `@classmethod`.
- В классе `LibraryBook` логика методов `take` и `return_back` в целом соответствует условию, проверки на наличие читателя выполнены.
- В конце программы есть блок проверки для всех трёх задач, создаются объекты и вызываются методы.

2) **Ошибки и недочёты (сгруппировать по серьёзности)**

**Блокирующие (ломает выполнение требований задания)**
- В классе `BankAccount` метод `withdraw` содержит логическую ошибку: после проверки `if not amount:` и `if self.balance < amount:` выполнение продолжается, и операция `self.balance -= amount` выполняется всегда, даже если сумма некорректна или средств недостаточно. Это приводит к некорректному изменению баланса. Исправление: добавить `return` после вывода ошибок или использовать `elif`/`else`.
  Пример исправления:
  ```python
  def withdraw(self, amount):
      if not amount:
          print("Некорректная сумма")
          return
      if self.balance < amount:
          print("Недостаточно средств")
          return
      self.balance -= amount
  ```
- Статический метод `is_valid_amount` содержит синтаксическую ошибку: отсутствует двоеточие после условия `if sum(amount) > 0`, и используется `sum(amount)`, что не имеет смысла для числа. По условию метод должен возвращать `True`, если сумма больше 0. Исправление:
  ```python
  @staticmethod
  def is_valid_amount(amount):
      return amount > 0
  ```
- В классе `LibraryBook` конструктор `__init__` не вызывает конструктор родительского класса `Book` и не сохраняет атрибуты `title`, `author`, `pages`. Это нарушает наследование: объект `LibraryBook` не будет иметь этих атрибутов, что сделает невозможным использование методов из `Book` (например, `info()`). Исправление: добавить вызов `super().__init__(title, author, pages)` и соответствующие параметры.
  Пример исправления:
  ```python
  class LibraryBook(Book):
      def __init__(self, title, author, pages, reader=None):
          super().__init__(title, author, pages)
          self.reader = reader
  ```

**Значимые (может дать неверный результат на части кейсов, сильно ухудшает качество)**
- В классе `BankAccount` метод `deposit` проверяет `if not amount:`, что интерпретирует `amount = 0` как некорректную сумму (выведет ошибку), но по условию некорректной считается сумма, не проходящая проверку `is_valid_amount` (т.е. `amount <= 0`). Это может привести к ложным срабатываниям, например, для `amount = 0` (хотя 0 тоже некорректен, но условие не уточняет). Лучше использовать `if not self.is_valid_amount(amount):` для согласованности.
  Пример исправления:
  ```python
  def deposit(self, amount):
      if not self.is_valid_amount(amount):
          print("Некорректная сумма")
      else:
          self.balance += amount
  ```
- В блоке проверки для `LibraryBook` не создаётся объект с указанием названия, автора и количества страниц (из-за ошибки в конструкторе), и не демонстрируется вызов методов `take` и `return_back` в требуемой последовательности (выдать двум разным читателям подряд, затем вернуть). В текущем коде объект создаётся без параметров, что вызовет ошибку при попытке использования.

**Минорные (стиль, читаемость, мелкие улучшения без влияния на правильность)**
- В классе `Book` в методе `read()` вывод немного отличается от условия: в условии `Читаем книгу "<title>" автора <author>.`, в решении `Читаем книгу "{self.title}" автора {self.author}.` — это корректно, но можно отметить, что в условии кавычки вокруг названия не указаны, однако в примере вывода они есть, так что решение верное.
- Имена переменных: `shet1` и `shet2` (возможно, опечатка, должно быть `schet1`/`schet2` или `account1`/`account2`). Это не влияет на функциональность, но ухудшает читаемость.
- В коде есть лишние пробелы и несоответствие отступов (например, в определении методов `Book` есть лишние пробелы перед `def`). Это не критично, но снижает аккуратность.

3) **Оценка и как она посчитана**
- Функциональность и соответствие условию: 25/50 (минус 25 за блокирующие ошибки: некорректный `withdraw`, синтаксическая ошибка в `is_valid_amount`, неправильный конструктор `LibraryBook`, что ломает наследование и проверки)
- Качество кода (структура, читаемость, устойчивость, отсутствие дублирования): 20/30 (минус 10 за значимые ошибки: некорректная проверка в `deposit`, отсутствие демонстрации работы `LibraryBook`; минус 0 за минорные, так как они не сильно влияют)
- Стиль и тесты: 15/20 (минус 5 за стилевые недочёты: имена переменных, отступы; тесты не требовались, но блок проверки есть, хотя и неполный для `LibraryBook`)
Итог: 25 + 20 + 15 = 60/100.

4) **Если задание выполнено не полностью**
- Отсутствует корректная реализация конструктора `LibraryBook` с наследованием от `Book`.
- Не продемонстрирована работа `LibraryBook` согласно условию (выдать двум разным читателям подряд, затем вернуть).
- Метод `is_valid_amount` содержит синтаксическую ошибку и неверную логику.
- Метод `withdraw` не предотвращает списание при ошибках.

**Вариант полного решения (исправления):**
```python
# Задача 1
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

# Задача 2
class BankAccount:
    interest_rate = 0.05

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if not self.is_valid_amount(amount):
            print("Некорректная сумма")
        else:
            self.balance += amount

    def withdraw(self, amount):
        if not self.is_valid_amount(amount):
            print("Некорректная сумма")
            return
        if self.balance < amount:
            print("Недостаточно средств")
            return
        self.balance -= amount

    @staticmethod
    def is_valid_amount(amount):
        return amount > 0

    @classmethod
    def set_interest_rate(cls, new_rate):
        cls.interest_rate = new_rate
        print(f"Процентная ставка изменена на {cls.interest_rate}")

# Задача 3
class LibraryBook(Book):
    def __init__(self, title, author, pages, reader=None):
        super().__init__(title, author, pages)
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

# Проверка
if __name__ == "__main__":
    # Задача 1
    my_book = Book("1984", "Джордж Оруэлл", 328)
    my_book.info()
    my_book.open()
    my_book.read()
    my_book.close()

    # Задача 2
    account1 = BankAccount("Наталья", 100000)
    account2 = BankAccount("Софья", 500)
    account1.deposit(50000)
    account1.withdraw(1000)
    BankAccount.set_interest_rate(0.07)
    account2.deposit(30)
    account2.withdraw(150)
    print(f"Баланс первого счета: {account1.balance}")
    print(f"Баланс второго счета: {account2.balance}")

    # Задача 3
    lib_book = LibraryBook("Мастер и Маргарита", "Михаил Булгаков", 480)
    lib_book.take("Анна")
    lib_book.take("Борис")  # Должно сообщить, что книга уже выдана
    lib_book.return_back()
    lib_book.return_back()  # Должно сообщить, что книга и так в библиотеке
```
