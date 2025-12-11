meetings = [
    ("Старт проекта", 8, 25),
    ("Code review", 4, 30),
    ("Планирование", 3, 45),
    ("Демо", 2, 20)
]
for topic, members, minutes in meetings:
    #compact_meetings = []
    if members in meetings < 5:
     if minutes in meetings < 30:
        print(f"{topic}: {members} чел, {minutes} мин")
print(f"{topic}: {members} чел, {minutes} мин")
