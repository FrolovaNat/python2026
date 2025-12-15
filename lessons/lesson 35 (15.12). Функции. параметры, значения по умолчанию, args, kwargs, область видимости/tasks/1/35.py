def analize_grades(grades):
    summa = sum(grades)
    dlina = len(grades)
    sredni = sum(grades)/len(grades)
    maxsimum = max(grades)
    minimum = min(grades)
result = {
 "средний": sredni,
 "максимум": maxsimum,
 "минимум": minimum
    }
    return result
result = analyze_grades([5, 4, 3, 5, 2])
print(result)
