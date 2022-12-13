import os

def write_cookbook():
    with open("recipe.txt") as f:
        cook_book = {}
        cook_list = [i.replace("\n", "") for i in f.readlines() if i != "\n"]
        while cook_list:
            cook_book[cook_list[0]] = []
            q_step = int(cook_list[1]) + 2
            for i in cook_list[2:q_step]:
                ingredient_dict = {}
                item1, item2, item3 = str(i).split("|")
                ingredient_dict['ingredient_name'] = item1.strip(" ")
                ingredient_dict['quantity'] = item2.strip(" ")
                ingredient_dict['measure'] = item3.strip(" ")
                cook_book[cook_list[0]].append(ingredient_dict)
            del cook_list[:q_step]
    return cook_book


def ingridient_quantity(cook_list, guest_quantity):
    cookbook = write_cookbook()
    result_dict = {}
    for dish, ingridient in cookbook.items():
        if dish in cook_list:
            for item in ingridient:
                if item['ingredient_name'] not in result_dict:
                    result_dict[item['ingredient_name']] = {'measure': item['measure'],\
                    'quantity': int(item['quantity']) * guest_quantity}
                else:
                    result_dict[item['ingredient_name']]['quantity'] += int(item['quantity']) * guest_quantity
    return result_dict

def sort_files():
    file_list = [i for i in os.listdir() if i.endswith(".txt")]
    sort_dict = {}
    for i in file_list:
        with open(i) as f:
            content = f.read()
        quantity = content.count('\n') + 1
        sort_dict[i] = {'quantity': int(quantity), 'content': content}
    with open('sort.txt', "w") as f:
        for key, value in sorted(sort_dict.items(), key=lambda x: x[1]['quantity']):
            f.write(f"{key}\n{value['quantity']}\n{str(value['content'])}\n")
    return

