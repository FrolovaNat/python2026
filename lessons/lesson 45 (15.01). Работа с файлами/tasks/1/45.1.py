def print_attendees(path: str):
     try:
        with open(path.txt, 'r', encoding='utf-8') as file:
            content = file.read()
            print(content)
     except FileNotFoundError:
         print("Файл не найден.")
