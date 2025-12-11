names = ["Антон", "Светлана", "Ира", "Борис", "Юля", "Даниил"]
len_name = [f"{name}-{len(name)} букв" for name in names if len(name) < 6]
print(len_name)

#result = [name for name in names if len(name)<6]
#print(result)

#name = []
#for x in names:
#    if len(x) < 6:
#        print(x)
        
