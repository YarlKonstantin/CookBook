def make_receipt_list(receipt_line_list):
    receipt_list = []
    for line in receipt_line_list[2:]:
        ingridient_dict = {}
        ingridient_list  = line.split(' | ')
        ingridient_dict['ingredient_name'] = ingridient_list[0]
        ingridient_dict['quantity'] = int(ingridient_list[1])
        ingridient_dict['measure'] = ingridient_list[2]
        receipt_list.append(ingridient_dict)

    return receipt_list

def make_cook_book():
    file = open('receipt.txt', 'r', encoding='utf-8')
    cook_book = {}
    for receipt in file.read().split('\n\n'):
        receipt_line_list = receipt.split('\n')
        name = receipt_line_list[0]
        cook_book[name] = make_receipt_list(receipt_line_list)
    return cook_book



if __name__=='__main__':
    print(make_cook_book())


