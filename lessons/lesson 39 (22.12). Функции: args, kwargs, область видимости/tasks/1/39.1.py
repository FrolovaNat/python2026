def mean_abs_deviation(*args):
    if not args:
        raise ValueError("Необходимо указать другое значение")
    len_score = sum(args)/len(args)
    new_spisok = []
    for score in args:
       new_spisok.append(round(score/len_score*100, 1))
       return tuple(new_spisok)

print(mean_abs_deviation(3, 5, 7, 9))
existing_scores = [10, 8, 6]
print(mean_abs_deviation(*existing_scores))
