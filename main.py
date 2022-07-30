cook_book = {}
cook_book_keys = []
# list_values = []
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
            b = ((file.readline()).rstrip()).replace("|", " ")
            b = b.split()
            new_dict = dict(zip(list_keys, b))
            list_values.append(new_dict)
            i += 1
        cook_book[f"{key}"] = list_values
print(cook_book)
