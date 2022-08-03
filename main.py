from pprint import pprint

cook_book = {}
cook_book_keys = []
list_keys = ['ingredient_name', 'quantity', 'measure']

with open("recipes.txt", "r") as file:
    for line in file:
        if line == "\n" or line == " ":
            continue
        cook_book_keys.clear()
        key = line.rstrip()
        cook_book_keys.append(key)
        count = int(file.readline())
        i = 0
        list_values = []
        list_values.clear()
        while i < count:
            b = (file.readline().rstrip()).split("|")
            new_dict = dict(zip(list_keys, b))
            list_values.append(new_dict)
            i += 1
        cook_book[f"{key}"] = list_values

# Вывод cook_book
# print('cook_book = {')
# for key in cook_book:
#     print(f"'{key}':")
#     for value in cook_book[key]:
#         print(f"{value}")
# print("}")

# Красивый вывод cook_book
# pprint(cook_book)

print("================================================================================")
print("")

# Задача №2-2
# dishes = ["Запеченный картофель"]
list_dishes = ["Омлет", "Утка по-пекински", "Запеченный картофель", "Фахитос"]
# person_count = 2


def get_shop_list_by_dishes(dishes, person_count):
    new_dict_ingredient = {}
    for value in cook_book[dishes[0]]:
        x = value['ingredient_name']
        b = value['measure']
        c = int(value['quantity']) * person_count
        new_dict = {x: {'measure': b, 'quantity': c}}
        new_dict_ingredient.update(new_dict)
    pprint(new_dict_ingredient)


get_shop_list_by_dishes(["Запеченный картофель", "Омлет"], 2)
