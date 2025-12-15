#задание 1
names = ["Антон", "Екатерина", "Ира", "Юля"]
result = [
 f"{name} — {len(name)} {'букв' if len(name) >= 5 else 'буквы'}"
    for name in names
    if len(name) < 6
]
print(result)

#задание 2
meetings = [
    ("Старт проекта", 8, 25),
    ("Code review", 4, 30),
    ("Планирование", 3, 45),
    ("Демо", 2, 20)
]
compact_meetings = [
    f"{topic}: {members} чел, {minutes} мин"
    for topic, members, minutes in meetings
    if members < 5 and minutes <= 30
]
print(compact_meetings) 

#задание 3
meetups = [
    {"city": "Москва", "tickets": 80, "sold": 75},
    {"city": "Казань", "tickets": 45, "sold": 30},
    {"city": "Пермь", "tickets": 60, "sold": 60}
]
availability = {
    meetup["city"]: "распродан" if meetup["sold"] >= meetup["tickets"] else "остались места"
    for meetup in meetups
    if meetup["tickets"] >= 50
}
print(availability)

#задание 4
# Вообще не поняла задание, первые 3 задания были аналогичными с заданиями в группе на занятии
