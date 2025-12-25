#данные задания все делала в классе
#блок 1
#1
def rectangle_info(width, height):
 area = width * height
 perimeter = 2 * (width + height)
 return (area, perimeter)

#2
def is_adult(age):
 return age >= 18

#3
def safe_div(a, b):
 if b == 0:
     return None
     return a / b

#блок 2
def delivery_price(city, weight_kg, urgent):
    if urgent:
        return 500 + 30 * weight_kg
    else:
        return 300 + 20 * weight_kg

print(delivery_price("Москва", 5, True))
print(delivery_price("СПб", 3, False))

print(delivery_price(city="Казань", weight_kg=2, urgent=True))
print(delivery_price(urgent=False, weight_kg=4, city="Владивосток"))
#print(delivery_price("Москва", True))

#блок 3
def push_score(score, scores=None):
    if scores is None:
        scores = []
    scores.append(score)
    return scores

def top_scores(scores, n=3):
    return sorted(scores, reverse=True)[:n]

# Сценарий 1: Два вызова без передачи scores
print(push_score(85)) 
print(push_score(90)) 

# Сценарий 2: Вызов с существующим списком
existing = [70, 80]
print(push_score(95, existing)) 

# Сценарий 3: Проверка top_scores
scores = [85, 90, 70, 95, 60]
print(top_scores(scores, 2))

#блок 4
# 1
def make_multiplier(factor):
    def mul(x):
        return x * factor
    return mul

# 2
double = make_multiplier(2)
triple = make_multiplier(3)
print(double(10))  
print(triple(10)) 

# 3
def mean(*args):
    if not args:
        return None
    return sum(args) / len(args)

# 4
def build_profile(**kwargs):
    return {
        "name": kwargs.get("name", "Без имени"),
        "age": kwargs.get("age", 0)
    }
