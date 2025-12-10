#Блок 1
books = ["Властелин колец", "Гарри Поттер", "Хоббит"]
books.append("1984")
books.append("Мастер и Маргарита")
print(books)
dlina = len(books)
print(f"Общее количество книг: {dlina}")
print(f"Первая книга: {books[0]}")
print(f"Последняя книга: {books[-1]}")
x = 1
for i in books:
    print(x, '. ', i, sep='')
    x +=1

#Блок 2
temperatures = [15, 17, 16, 18, 19, 20, 18]
print(f"Начало недели: {temperatures[0:3]}")
print(f"Конец недели: {temperatures[-3:]}")
print(f"Каждый второй день: {temperatures[1:7:2]}")
print(f"Средняя неделя: {temperatures[1:6]}")

#Блок 3
tasks = ["проснуться", "позавтракать", "купить хлеб", "поработать"]
list1 = ["позвонить маме", "записаться к врачу"]
tasks.extend(list1)
print(tasks)
tasks.insert(3, "проверить почту")
print(tasks)
tasks.remove("купить хлеб")
print(tasks)
tasks.pop(5)
tasks.insert(0, "записаться к врачу")
print(tasks)

#Блок 4
movies = [
    {"name": "Интерстеллар", "stil": "фантастика", "ocenka": 9},
    {"name": "Маска", "stil": "комедия", "ocenka": 8},
    {"name": "Пираты Карибского моря", "stil": "приключения", "ocenka": 7},
    {"name": "Один дома", "stil": "комедия", "ocenka": 8}
]
for movie in movies:
    print(f"Наименование: {movie['name']}, Жанр: {movie['stil']}. (Рейтинг/{movie['ocenka']})")
#if ocenka in movies:
#    ocenka > 8
 #   print(f"Наименование фильма с высоким рейтингом: {name}")
 # 2, 3 и 4 пункт не могу сделать в 4 блоке
