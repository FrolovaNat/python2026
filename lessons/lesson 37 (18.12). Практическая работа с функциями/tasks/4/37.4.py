#1
def make_multipliter(factor):
    def mul(x):
        return x*factor
    return mul(x)

#2
#double = make_multiplier(2)
#triple = make_multiplier(3)
# не знаю как делать, в лекции не проходили

#3
def mean(*args):
    if not args:
        return None
    else:
        return sum(args)/args
#4
def build_profile(**kwargs):
     name = kwargs.get("name", "Без имени")
     age = kwargs.get("age", 0)
     profile = {name, age}
     return profile
     



