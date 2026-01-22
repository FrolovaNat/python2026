#1
from abc import ABC, abstractmethod
class NotificationChannel(ABC):
    def __init__(self, sender_name: str):
        self.sender_name = sender_name
    
    @abstractmethod
    def send(self, recipient: str, message: str) -> None:
        pass

def format_message(message: str) -> str:
    return f"[{sender_name}] {message}"

#2
class EmailChannel(NotificationChannel):
    def __init__(self, sender_name, sender_email):
        super().format_message(message)

print(EMAIL to <recipient>: <formatted_message> (from <sender_email>))

class SMSChannel(NotificationChannel):
    def __init__(self, sender_name, sender_phone):
