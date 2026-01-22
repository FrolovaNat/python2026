Время затраченное на выполнение: 0:22

result: 10/100

1) **Сильные стороны**
- Студент начал с импорта `abc` и создания абстрактного класса `NotificationChannel` с правильным `__init__` и абстрактным методом `send`.
- Есть попытка создать наследников `EmailChannel` и `SMSChannel`.

2) **Ошибки и недочёты**

**Блокирующие (ломает выполнение требований задания)**
- Метод `format_message` определён как обычная функция вне класса, а не как метод класса `NotificationChannel`. В условии требуется, чтобы `NotificationChannel` имел обычный метод `format_message(message: str) -> str`. В текущем виде функция `format_message` даже не имеет доступа к `sender_name`, так как `sender_name` — это атрибут экземпляра, а не глобальная переменная. Это делает невозможным корректное форматирование сообщений.
- Классы `EmailChannel` и `SMSChannel` не реализованы. В `EmailChannel.__init__` есть вызов `super().format_message(message)`, но `message` не определена в `__init__`, и сам метод `send` отсутствует. Вместо этого есть `print(EMAIL to <recipient>: ...)`, который является синтаксически неверным (строка не в кавычках) и находится вне какого-либо метода. `SMSChannel` имеет только `__init__` без тела.
- Отсутствует класс `NotificationService`, который должен принимать список каналов и иметь метод `notify_all`. Это прямое нарушение требования.
- Отсутствует демонстрация работы (создание каналов, сервиса, вызов `notify_all`). Код не запустится из-за синтаксических ошибок и неполных определений.

**Значимые (может дать неверный результат на части кейсов, сильно ухудшает качество)**
- В `EmailChannel.__init__` некорректный вызов `super().format_message(message)`. Во-первых, `format_message` должен вызываться из `send`, а не из `__init__`. Во-вторых, `super()` в данном контексте ссылается на `NotificationChannel`, но у него нет метода `format_message` (так как он определён как отдельная функция). Это приведёт к ошибке `AttributeError`.
- Даже если бы метод `format_message` был реализован правильно в классе, вызов `super().format_message(message)` в `__init__` не имеет смысла, так как `__init__` не принимает `message`.

**Минорные (стиль, читаемость, мелкие улучшения без влияния на правильность)**
- Комментарии `#1` и `#2` избыточны, лучше использовать docstrings или чёткую структуру.
- Имя файла в заголовке (`lessons/lesson 49 (22.01). ООП/tasks/1/notifications.py`) не нужно в коде, это может быть частью представления решения.
- Строка `print(EMAIL to <recipient>: ...)` содержит синтаксическую ошибку (отсутствуют кавычки), что делает код неисполняемым.

3) **Оценка и как она посчитана**
- Функциональность и соответствие условию: 5/50. Реализован только абстрактный класс частично (нет метода `format_message` внутри класса). Наследники не работают, отсутствует `NotificationService` и демонстрация. Выполнено менее 20% требований.
- Качество кода: 3/30. Код содержит синтаксические ошибки, неполные классы, нарушена структура (метод вне класса). Читаемость низкая.
- Стиль и тесты: 2/20. Стиль не соответствует PEP 8 (например, пробелы в именах), тестов нет. Есть синтаксические ошибки.

Итог: 10/100 (округление вниз от 10).

4) **Если задание выполнено не полностью**
- Отсутствует метод `format_message` внутри класса `NotificationChannel`.
- Классы `EmailChannel` и `SMSChannel` не реализованы: нет корректного `__init__`, нет метода `send`, не используется `super()` в `send`.
- Отсутствует класс `NotificationService`.
- Отсутствует демонстрация работы.

**Вариант полного решения (код):**

```python
from abc import ABC, abstractmethod

class NotificationChannel(ABC):
    def __init__(self, sender_name: str):
        self.sender_name = sender_name
    
    def format_message(self, message: str) -> str:
        return f"[{self.sender_name}] {message}"
    
    @abstractmethod
    def send(self, recipient: str, message: str) -> None:
        pass

class EmailChannel(NotificationChannel):
    def __init__(self, sender_name: str, sender_email: str):
        super().__init__(sender_name)
        self.sender_email = sender_email
    
    def send(self, recipient: str, message: str) -> None:
        formatted_message = super().format_message(message)
        print(f"EMAIL to {recipient}: {formatted_message} (from {self.sender_email})")

class SMSChannel(NotificationChannel):
    def __init__(self, sender_name: str, sender_phone: str):
        super().__init__(sender_name)
        self.sender_phone = sender_phone
    
    def send(self, recipient: str, message: str) -> None:
        formatted_message = super().format_message(message)
        print(f"SMS to {recipient}: {formatted_message} (from {self.sender_phone})")

class NotificationService:
    def __init__(self, channels: list[NotificationChannel]):
        self.channels = channels
    
    def notify_all(self, recipient: str, message: str) -> None:
        for channel in self.channels:
            channel.send(recipient, message)

# Демонстрация работы
if __name__ == "__main__":
    email_channel = EmailChannel("MyService", "noreply@example.com")
    sms_channel = SMSChannel("MyService", "+1234567890")
    
    service = NotificationService([email_channel, sms_channel])
    service.notify_all("user@example.com", "Hello via email and SMS!")
    service.notify_all("+0987654321", "Another notification")
```
