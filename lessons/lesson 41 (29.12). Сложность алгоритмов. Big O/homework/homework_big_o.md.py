def min_max(nums):
    mn = float("inf")
    mx = float("-inf")
    for x in nums:
        if x < mn:
            mn = x
        if x > mx:
            mx = x
    return mn, mx
#Фрагмент A
#Линейный проход: О(n) - один полный проход по имеющимся данным


count_pairs def(nums):
 count = 0
    n = len(nums)
 for i in range(n):
 for j in range(i + 1, n):
 if nums[i] + nums[j] == 0:
 count += 1
    return count
#Фрагмент В
#Квадратичный алгоритм: O(n^2) - внутри одной функции, вложена вторая функция, т.еПолный проход внутри полного прохода, в связи с этим сложность алгоритма возрастает


has_duplicate def(nums):
 nums = sorted(nums)
 for i in range(1, len(nums)):
 if nums[i] == nums[i - 1]:
 return True
    return False
#Фрагмент С
#O(n log n) - Линейный проход плюс логарифмическая вложенность, логарифмическая сложность становится за счет сортировки, т.к. сначала данные сортируются, далее по ним происходит проход, вложенностью здесь явсяется сортировка
