spisok = ["макароны", "сыр", "помидоры"]
#dobavka = ["руккола", "оливковое масло"]
#print(spisok+dobavka)
spisok.append("руккола")
spisok.append("оливковое масло")
x = len(spisok)
print(spisok)
print(x)
y = spisok[-1]
two = spisok[1]

print(f"Второй: {two}")
print(f"Последний: {y}")

x = 1
for i in spisok:
    print(x, '. ', i, sep='')
    x += 1
