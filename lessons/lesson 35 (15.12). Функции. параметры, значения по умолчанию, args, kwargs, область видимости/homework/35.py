#1
def format_product (name, price):
    return f"Товар: {name}, Цена: {price} руб."
print(format_product("Молоко", 90))
print(format_product("Хлеб", price=50))
print(format_product(price=120, name="Яблоки"))

#2
def add_note (text, notes_list=None):
    if notes_list is None:
        notes_list = []
        data = ("2024-12-15")
        notes_list.append(data + text)
        return notes_list
print(add_note("Купить молоко"))
print(add_note("Позвонить маме"))
print(add_note("Первая"), add_note("Вторая"))

#3
def calculate_total (*args, tip_percent=0, discount=0):
    total = sum(args)
    if tip_percent > 0:
        total += total*(tip_percent / 100)
    if discount > 0:
        total -= discount
    return total
print(calculate_total(100, 200, 300))
print(calculate_total(50, 75, tip_percent=10))
print(calculate_total(400, discount=50))

#4
def create_profile (**kwargs):
    profile = {
        'name': kwargs.get('имя', ''),
        'age': kwargs.get('возраст', 0),
        'city': kwargs.get('город', ''),
        'language': kwargs.get('язык', ''),
        'level': 'Новичок'  
    }
    return profile
    base_info = {"name": "Наталья", "age": 25}
    extra_info = {"city": "Москва", "language": "Python"}
print(create_profile(base_info, extra_info))
#не выводит результат принта 4 задачи
    
