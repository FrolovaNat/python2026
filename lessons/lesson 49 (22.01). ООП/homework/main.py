from abc import ABC, abstractmethod
class DiscountPolicy(ABC):
    def __init__(self, name):
        self.name = name
        @abstractmethod
        def apply(self, price):
            pass 
        def clamp_price(self, price):
            if price < 0:
                return 0
            else:
                return price

class PercentDiscount(DiscountPolicy):
    def __init__(self, name, percent):
        super().__init__(name)
        self.percent = percent
    def apply(self, price):
        price = super().clamp_price(price)
        discount = price * (self.percent / 100)
        return price - discount
    
class FixedDiscount(DiscountPolicy):
    def __init__(self, name, amount):
        super().__init__(name)
        self.amount = amount
    def apply(self, price):
        price = super().clamp_price(price)
        return price - amount
        if price < 0:
            return None

class PriceCalculator:
    def __init__(self, policies: list[DiscountPolicy]):
        self.policies = policies
    def calculate(self, price):
        for policy in self.policies:
            price = policy.apply(price)
        return price
policies1 = PercentDiscount("Процентная", 10)
policies2 = FixedDiscount("Фиксированная", 250)


