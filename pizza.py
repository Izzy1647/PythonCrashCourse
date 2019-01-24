# 4-1 4-11

pizza_list = ['NewYorkStyle','ChicagoStyle','PanPizza']
for pizza in pizza_list:
    print(pizza)
    print('I like '+pizza)
print('I really love pizza!')

friend_pizza_list = pizza_list[:]
pizza_list.append('ThickStyle')
friend_pizza_list.append('CaliforniaStyle')
print('My favourite pizzas are:')
for pizza in pizza_list:
    print(pizza)

print('My friend\'s favorite pizzas are:')
for pizza in friend_pizza_list:
    print(pizza)