Дней на выполнение: 2

result: 60/100

1) **Сильные стороны**
- Использован абстрактный класс `ABC` и декоратор `@abstractmethod`, что соответствует требованию.
- Классы `PercentDiscount` и `FixedDiscount` наследуют `DiscountPolicy`, и в их `__init__` используется `super().__init__(name)`.
- В методе `apply` классов-наследников используется `super().clamp_price(price)`, как требовалось.
- Создан класс `PriceCalculator` с методом `calculate`, который применяет политики по очереди.
- В конце программы созданы объекты политик (хотя и не полностью корректно).

2) **Ошибки и недочёты**

**Блокирующие (ломает выполнение требований задания)**
- В классе `FixedDiscount` метод `apply` содержит ошибку: переменная `amount` не определена (должна быть `self.amount`). Это вызовет `NameError` при вызове метода. Также логика метода некорректна: сначала вычисляется `price - amount`, затем эта цена не используется, и проверка `if price < 0` никогда не выполняется, так как после `return` код не работает. Это нарушает требование "итоговая цена не должна быть меньше 0".  
  Пример исправления:
  ```python
  def apply(self, price):
      price = super().clamp_price(price)
      result = price - self.amount
      if result < 0:
          return 0
      return result
  ```
- В конце программы не создан объект `PriceCalculator` и не вызван метод `calculate` для проверки, как требуется в условии: "создай минимум 2 политики скидок (процентную и фиксированную), передай их в PriceCalculator, посчитай цену минимум для 2 разных исходных цен". Это невыполнение явного требования.

**Значимые (может дать неверный результат на части кейсов, сильно ухудшает качество)**
- В классе `DiscountPolicy` метод `clamp_price` и абстрактный метод `apply` определены внутри `__init__` (из-за неправильного отступа). Это приводит к тому, что `clamp_price` становится методом экземпляра, но `apply` не определяется корректно (он становится локальной функцией внутри `__init__`). В результате класс не может быть инстанциирован, так как `apply` остаётся абстрактным. Это критическая ошибка, нарушающая работу всей системы.
  Пример исправления (правильные отступы):
  ```python
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
  ```
- Отсутствует реализация класса `MinPriceDiscount` из задачи 2, хотя условие требует его создания и проверки. Это невыполнение части задания.

**Минорные (стиль, читаемость, мелкие улучшения без влияния на правильность)**
- В конце программы переменные названы `policies1` и `policies2`, но они являются объектами политик, а не списком. Лучше использовать имена, отражающие их тип, например `percent_policy` и `fixed_policy`.
- Нет аннотаций типов для методов (например, `apply(price: float) -> float`), хотя в условии они указаны как пример. Это не является требованием, но улучшило бы читаемость.
- В классе `PriceCalculator` в `__init__` указана аннотация типа `list[DiscountPolicy]`, но для Python 3.8 и ниже может потребоваться `from typing import List`. Однако если используется Python 3.9+, это допустимо.

3) **Оценка и как она посчитана**
- Функциональность и соответствие условию: 20/50 (минус 30 за: некорректную работу `FixedDiscount`, неправильное определение методов в `DiscountPolicy`, отсутствие создания и использования `PriceCalculator` для проверки, отсутствие реализации `MinPriceDiscount`).
- Качество кода: 20/30 (минус 10 за серьёзные ошибки в структуре классов и логике, которые делают код нерабочим).
- Стиль и тесты: 20/20 (тесты не требовались, стилевые замечания незначительны, баллы не снижаются).

4) **Если задание выполнено не полностью**
- Отсутствует класс `MinPriceDiscount`.
- Не выполнена проверка работы: не создан `PriceCalculator`, не вызван `calculate`.
- Частично выполнено: классы `PercentDiscount` и `FixedDiscount` реализованы, но с ошибками; `DiscountPolicy` имеет структурную ошибку.

**Вариант полного решения (краткий код):**
```python
from abc import ABC, abstractmethod

class DiscountPolicy(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def apply(self, price: float) -> float:
        pass

    def clamp_price(self, price: float) -> float:
        return max(price, 0)

class PercentDiscount(DiscountPolicy):
    def __init__(self, name: str, percent: float):
        super().__init__(name)
        self.percent = percent

    def apply(self, price: float) -> float:
        price = super().clamp_price(price)
        return price * (1 - self.percent / 100)

class FixedDiscount(DiscountPolicy):
    def __init__(self, name: str, amount: float):
        super().__init__(name)
        self.amount = amount

    def apply(self, price: float) -> float:
        price = super().clamp_price(price)
        return max(price - self.amount, 0)

class MinPriceDiscount(DiscountPolicy):
    def __init__(self, name: str, min_price: float, percent: float):
        super().__init__(name)
        self.min_price = min_price
        self.percent = percent

    def apply(self, price: float) -> float:
        price = super().clamp_price(price)
        if price < self.min_price:
            return price
        return price * (1 - self.percent / 100)

class PriceCalculator:
    def __init__(self, policies: list[DiscountPolicy]):
        self.policies = policies

    def calculate(self, price: float) -> float:
        for policy in self.policies:
            price = policy.apply(price)
        return price

# Проверка
if __name__ == "__main__":
    percent_policy = PercentDiscount("Процентная", 10)
    fixed_policy = FixedDiscount("Фиксированная", 250)
    min_price_policy = MinPriceDiscount("Пороговая", 1000, 15)

    calculator = PriceCalculator([percent_policy, fixed_policy, min_price_policy])
    print(calculator.calculate(1500))  # Пример 1
    print(calculator.calculate(500))   # Пример 2
```
