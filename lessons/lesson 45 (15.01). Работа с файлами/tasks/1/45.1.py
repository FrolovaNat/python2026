def print_attendees(path: str):
     try:
        with open(path, 'r', encoding='utf-8') as file:
            names = [line.strip() for line in lines if line.strip()]
     except FileNotFoundError:
         print("Файл не найден.")
         return

