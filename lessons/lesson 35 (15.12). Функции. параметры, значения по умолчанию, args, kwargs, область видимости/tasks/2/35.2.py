
def add_task (task_list, title, priority="medium", tags=None):
    if tags == None:
        tags = []
        slovar = {'title': title, 'priority':priority, 'tags': tags}
        add_task.append(slovar)
        return slovar
print(add_task)
    
    
#Объявить функцию с параметрами: task_list, title, priority, tags.
#Для параметра priority установить значение по умолчанию "medium".
#Для параметра tags установить безопасное значение по умолчанию (использовать None-паттерн).

#Внутри функции:
 #     a. Если tags равно None, создать новый пустой список.
  #    b. Создать словарь задачи с ключами "title", "priority", "tags" и соответствующими значениями.
   #   c. Добавить этот словарь в конец списка task_list.
    #  d. Вернуть созданный словарь.
