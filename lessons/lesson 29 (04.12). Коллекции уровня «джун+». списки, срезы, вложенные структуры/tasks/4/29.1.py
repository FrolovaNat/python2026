vendors = [
    {"name": "Сады Данилы", "category": "овощи", "products": ["морковь", "свекла"], "price_level": "low"},
    {"name": "Пасека", "category": "мёд", "products": ["липовый", "гречишный"], "price_level": "medium"},
    {"name": "Сырная лавка", "category": "молочное", "products": ["бри", "качотта"], "price_level": "high"},
    ]

for vendor in vendors:
    print(f"{vendor['name']} ({vendor['category']}). Уровень цен: {vendor['price_level']}, товары: {', '.join(vendor['products'])}")
    
all_products = set()  
for vendor in vendors:  
    all_products.update(vendor['products'])  
print("Все продукты:", all_products)

#category1 = {}
#for vendor in vendors:
#    count +=1
    

#print(f"Категории: {category1}")
#Не могу сделать дальше, тяжелая задача
