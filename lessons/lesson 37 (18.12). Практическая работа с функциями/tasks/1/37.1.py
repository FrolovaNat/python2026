#1
def rectangle_info(width, height):
    result = width * height
    return result
s = rectangle_info(3, 5)
print(s)

#2
def is_adult(age):
    if age >=18:
        return True
result = is_adult(19)
print(result)

#3
def safe_div(a, b):
    if b==0:
        return None
    else:
        return a/b
result = safe_div(8, 4)
print(result)
