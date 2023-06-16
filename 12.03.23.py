goods = [
    {
        'name':'iphone',
        'brand': 'Apple',
        'price': 1200
    },
    {
        'name':'samsung A23',
        'brand': 'Samsung',
        'price': 600
    },

    {
        'name':'Xiaomi Mi13',
        'brand': 'Xiaomi',
        'price': 800
    },
    {
        'name':'Iphone 11',
        'brand': 'Apple',
        'price': 400
    }
]
'''
def item_price(item):
    return item['price']

print(sorted(goods,key=item_price))
'''
# ФУНКЦИЯ LAMBDA
'''
print(sorted(goods, key=lambda item: item['price']))
'''
# ФУНКЦИЯ FILTER
'''
apple_list = filter(lambda item: item['brand']=='Apple',goods)
print(list(apple_list))
'''
'''
for i in apple_list:
    print(i)
'''
# ФУНКЦИЯ MAP
'''
a=['1','2','3']
b=map(int,a)
print(list(b))
'''
'''
def sss(item):
    return item + 'sss'
print(list(map(sss,a)))
'''
# ФУНКЦИЯ NUMERATE
'''
for i, item in enumerate(goods):
    print(i, item)
'''

# ФУНКЦИЯ ZIP
'''
names = ['Илья', 'Артур', 'Дима', 'Денис']
surnames = ['Кочергин', 'Лобанов', 'Шикирюк', 'Додолин']
ages = ['13', '12', '15', '14']

for name, surname, age in zip(names,surnames,ages):
    print(name, surname, age)
'''
# a='диана'
# print(a.capitalize())

good_list = []
class Coods:
    def __init__(self, name):
        self.name=name
        
item1 = Coods('kkkkkk')
good_list.append()
