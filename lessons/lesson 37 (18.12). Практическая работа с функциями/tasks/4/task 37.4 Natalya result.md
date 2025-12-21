result: 30/100

### 1. Формулировка задания
Требуется реализовать 4 функции:
1. `make_multiplier(factor)` → возвращает функцию `mul(x) = x * factor`.
2. Создать множители `double` и `triple` через `make_multiplier`, протестировать их.
3. `mean(*args)` → среднее арифметическое или `None` при отсутствии аргументов.
4. `build_profile(**kwargs)` → словарь с ключами `name` (по умолчанию "Без имени") и `age` (по умолчанию 0).

**Ограничения**: 
- Для `make_multiplier` требуется возврат функции, а не значения.
- В `mean` корректная обработка пустых аргументов и деления.
- В `build_profile` должен возвращаться словарь, а не множество.

---

### 2. Результаты проверки
**Файл**: `lessons/lesson 37 (18.12). Практическая работа с функциями/tasks/4/37.4.py`

#### Задание 1: `make_multiplier`
- **Ошибка в строке 2**: 
  ```python
  def make_multipliter(factor):  # Опечатка в имени (multipliter вместо multiplier)
  ```
- **Ошибка в строке 5**:
  ```python
  return mul(x)  # Возвращается результат вызова mul, а не сама функция
  ```
  **Тест**: 
  ```python
  double = make_multiplier(2)  # Вызовет ошибку, так как mul требует аргумент x
  ```

#### Задание 2: Создание множителей
- **Код закомментирован**, реализация отсутствует (строки 8-10).

#### Задание 3: `mean`
- **Ошибка в строке 14**:
  ```python
  return sum(args)/args  # Деление на кортеж args вместо len(args)
  ```
  **Тест**: 
  ```python
  mean(1, 2, 3)  # TypeError: unsupported operand type(s) for /: 'int' and 'tuple'
  ```

#### Задание 4: `build_profile`
- **Ошибка в строке 18**:
  ```python
  profile = {name, age}  # Создается множество, а не словарь
  ```
  **Тест**: 
  ```python
  build_profile(name="Alice", age=30)  # Вернет множество {0, 'Alice'}, а не словарь
  ```

---

### 3. Сильные стороны работы
- Базовое понимание замыканий (попытка реализации `make_multiplier`).
- Правильная проверка на пустые аргументы в `mean`.
- Использование `kwargs.get` для обработки значений по умолчанию в `build_profile`.

---

### 4. Ошибки
#### Блокирующие (делают код нерабочим):
1. **`make_multiplier` возвращает число, а не функцию**:
   - **Исправление**: Заменить `return mul(x)` на `return mul`.
   - **Пример**:
     ```python
     def make_multiplier(factor):
         def mul(x):
             return x * factor
         return mul  # Возвращаем функцию, а не её результат
     ```

#### Значимые (нарушена функциональность):
2. **Не созданы множители `double` и `triple`**:
   - **Исправление**: Раскомментировать и реализовать:
     ```python
     double = make_multiplier(2)
     triple = make_multiplier(3)
     print(double(10))  # 20
     print(triple(10))  # 30
     ```

3. **Ошибка в расчёте среднего значения**:
   - **Исправление**: Заменить `args` на `len(args)`.
   - **Пример**:
     ```python
     def mean(*args):
         if not args:
             return None
         return sum(args) / len(args)
     ```

4. **Некорректное создание профиля (множество вместо словаря)**:
   - **Исправление**: Использовать словарь с ключами `name` и `age`.
   - **Пример**:
     ```python
     def build_profile(**kwargs):
         return {
             "name": kwargs.get("name", "Без имени"),
             "age": kwargs.get("age", 0)
         }
     ```

#### Минорные:
5. **Опечатка в имени функции `make_multipliter`**:
   - **Исправление**: Переименовать в `make_multiplier`.

---

### 5. Оценка
- **Функциональность (50%)**: 10/50  
  - `make_multiplier` не работает, множители не созданы, `mean` и `build_profile` содержат критические ошибки.
- **Качество кода (30%)**: 10/30  
  - Ошибки в типах данных (множество вместо словаря), некорректная логика.
- **Стиль и тесты (20%)**: 10/20  
  - Нет тестов, но базовое форматирование соблюдено.

**Итог**: 30/100. Баллы сняты за нерабочие функции и частично реализованные требования.

---

### 6. Вариант полного решения
```python
# 1. make_multiplier
def make_multiplier(factor):
    def mul(x):
        return x * factor
    return mul

# 2. Множители
double = make_multiplier(2)
triple = make_multiplier(3)
print(double(10))  # 20
print(triple(10))  # 30

# 3. mean
def mean(*args):
    if not args:
        return None
    return sum(args) / len(args)

# 4. build_profile
def build_profile(**kwargs):
    return {
        "name": kwargs.get("name", "Без имени"),
        "age": kwargs.get("age", 0)
    }
```

---

Анализ выполнен моделью: GPT-4o.
