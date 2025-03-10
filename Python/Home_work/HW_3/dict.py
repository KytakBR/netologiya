items = {
 'milk15':{'name': 'молоко 1.5%', 'count': 34, 'price': 89.9},
 'cheese':{'name': 'cыр молочный 1 кг.', 'count': 12, 'price': 990.9},
 'sausage':{'name': 'колбаса 1 кг.', 'count': 122, 'price': 1990.9}
}
items_2 = {}
for i in items.keys():
    if (items[f'{i}']['count']) < 20:
        items_2[i] = True
    else:
        items_2[i] = False
print(items_2)