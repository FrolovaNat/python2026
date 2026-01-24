def print_participants(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            content = file.read()
            print(content)
            if not content:
                print("Нет файла со списком участников")
                return   
            participants = [line.strip() for line in lines if line.strip()]
            if not participants:
                print("Список участников пуст")
                return
        except FileNotFoundError:
            print("Нет файла со списком участников") 
        
