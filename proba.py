ook_book = {}
cook_book_keys = []
list_keys = ['ingredient_name', 'quantity', 'measure']

with open("recipes.txt", "r") as file:
    for line in file:
        print(line, end="")
        # dish_name =





    # x = file.readlines()
    # for i in x:
    #     v = i.rstrip().replace("|", " ")
    #     d = v.split()
    #     print(d)

        # dish_name = <что-то тут делаем>
        #     counter = <как-то получили кол-во строк>
        #     list_of_ingridient = <временный список>
        #     for i in <наш счетчик counter использовать range>:
        #         temp_dict = {} - временный словарь
        #         ingridient = file_work.readline() - вот так перемещаемся по файлу
        #         <заполняем словарь с ингридиетом>
        #         <добавляем словарь в список>
        #     <записываем в словарь cook_dict наш рецепт>
        #     file_work.readline() - еще раз смещаетмся т.к. там пустая срока