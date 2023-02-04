goods = []


def fill_goods_database():
    i = 1
    ans = input(f"Enter new element? yes/no: ")
    while ans == 'yes':
        tur = (i, {"name": input(f"Enter good name:"),
                   "price": input(f"Enter good price:"),
                   "quantity": input(f"Enter good quantity:"),
                   "unit": input(f"Enter good unit:")})
        goods.append(tur)
        i += 1
        ans = input(f"Enter new element? yes/no: ")
    return goods


def goods_database_analytics(goods):
    temp_list_names = []
    temp_list_prices = []
    temp_list_quantities = []
    temp_list_unit = []
    for element in goods:
        temp_list_names.append(element[1]['name'])
        temp_list_prices.append(element[1]['price'])
        temp_list_quantities.append(element[1]['quantity'])
        temp_list_unit.append(element[1]['unit'])
    result_dict = {"names": temp_list_names, "prices": temp_list_prices,
                   "quantities": temp_list_quantities, "unit": temp_list_unit}
    return [f"{el}\n" for el in result_dict.items()]


print(*goods_database_analytics(fill_goods_database()))
