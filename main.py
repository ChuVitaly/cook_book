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


# Задача №2-1

def get_shop_list_by_dishes(dishes, person_count):
    new_dict_ingredient_all = {}
    i = 0
    while i != len(dishes):
        new_dict_ingredient = {}
        for value in cook_book[dishes[i]]:
            x = value['ingredient_name']
            b = value['measure']
            c = int(value['quantity']) * person_count
            new_dict = {x: {'measure': b, 'quantity': c}}
            if x in new_dict_ingredient_all.keys():
                new_dict_ingredient_all[x]['quantity'] = new_dict_ingredient_all[x]['quantity'] + c
                break
            new_dict_ingredient.update(new_dict)
            new_dict_ingredient_all.update(new_dict_ingredient)
        i += 1
    pprint(new_dict_ingredient_all)


get_shop_list_by_dishes(["Омлет", "Фахитос"], 2)
