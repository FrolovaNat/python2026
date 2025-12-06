produkt = ["гречка", "курица", "овощи"]
list1 = ["зелень", "авокадо"]

produkt.extend(list1)
print(produkt)

produkt.insert(1, "оливковое масло")
print(produkt)

produkt.remove("гречка")
print(produkt)

produkt.pop(4)
produkt.insert(2, "авокадо") 
print(produkt)

for index, item in enumerate(produkt, start = 1):
    print(f"{index}. {item}")
