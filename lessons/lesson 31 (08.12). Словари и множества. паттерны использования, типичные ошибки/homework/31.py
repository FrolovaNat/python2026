#задание 1
pledges = [
    ("anna", 300),
    ("pavel", 150),
    ("anna", 200),
    ("dasha", 400),
]
finished = ["pavel", "ivan"]
donations = {}
for name,summ in pledges:
    if name in donations:
        donations[name] += summ
    else:
        donations[name] = summ
for name in finished:
    donations.pop(name, "ещё не жертвовал")
print(donations)

#задание 2
emails = [
    "user1@corp.ru",
    "user2@example.com",
    "user3@corp.ru",
    "user4@test.io",
]
trusted = {"corp.ru", "example.com"}
domains = {email.split('@')[1] for email in emails}
print(domains)
print(f"Не входят: {domains-trusted}")
print (f"Все е-mail: {domains|trusted}")

#задание 3
a = {"natalya", "ivan", "olga"}
b = {"olga", "petr", "natalya"}
c = {"ivan", "sergey"}
print(f"В группах А и В: {a&b}")
print(f"В А, но не в С: {a-c}")

#задание 4
topics = [
    ("dict", 4),
    ("set", 3),
    ("list", 5),
    ("dict", 2),
]
limit = 5
hours_by_topic = {}
for topic, summ in topics:
    if topic in hours_by_topic:
        hours_by_topic[topic] += summ
    else:
        hours_by_topic[topic] = summ
print(hours_by_topic)
hours_by_topic_new = {}
for topic, limit in topics:
    if topic in hours_by_topic_new:
        hours_by_topic_new[topic] >= limit
    else:
        hours_by_topic_new[topic] = limit
print(hours_by_topic_new)
#не уверена в правильности 4 задачи    
