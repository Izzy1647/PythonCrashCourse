# 7-8 7-9

sandwich_orders = ['potato','pastrami','beef','salad','fish','green','pork','pastrami','pastrami']
finished_sandwich = []
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print(sandwich_orders)
print('================   ==================')
while sandwich_orders:
    making_sandwich = sandwich_orders.pop()
    print('I made your '+making_sandwich+' sandwich')
    finished_sandwich.append(making_sandwich)
    print('Made list:',finished_sandwich)
