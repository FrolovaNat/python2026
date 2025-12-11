meetups = [
    {"city": "Москва", "tickets": 80, "sold": 80},
    {"city": "Казань", "tickets": 45, "sold": 30},
    {"city": "Пермь", "tickets": 60, "sold": 40}
]
#for meetup in meetups:
#availability = [meetup for meetup in meetups if tickets >= 50]
    #if tickets >= 50:
#print(availability)

availability = {
    meetup["city"]: meetup["sold"], meetup["city"]: meetup["tickets"]
    for meetup in meetups
    if meetup[tickets] >= 50 
    }
print(availability)
