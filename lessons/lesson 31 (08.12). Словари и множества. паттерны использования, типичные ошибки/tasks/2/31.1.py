    
pledges = [('anna', 300), ('pavel', 150), ('anna', 200), ('dasha', 400)]
finished = ['pavel']

donations = {}
for name,count in pledges:
    donations[name] = donations.get(name,0) + count
for y in finished:
    removed = donations.pop(y, 'вернул деньги')
    print(f"{y}: {removed}")
print(donations)

