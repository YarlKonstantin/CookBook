from Task_1 import make_cook_book

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    cook_book = make_cook_book()
    for dish in dishes:
        receipt = cook_book[dish]
        for ingridient in receipt:
            name = ingridient['ingredient_name']
            if name in shop_list:
                shop_list[name]['quantity'] += ingridient['quantity']
            else:
                shop_list[name] = {'measure': ingridient['measure'], 'quantity': ingridient['quantity'] }
    for name in shop_list:
        shop_list[name]['quantity'] *= person_count
    return shop_list


if __name__ == '__main__':
    print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
