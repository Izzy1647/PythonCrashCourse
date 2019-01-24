# 7-5 7-6
act = True
while act:
    age = input('Input your age: ')
    if int(age) < 3:
        print('0')
    elif int(age) >=3 and int(age) < 12:
        print('10')
    else:
        print('15')
    signal = input('Next one or quit? Input "next" or "quit": ')
    if signal == 'next':
        continue
    elif signal == 'quit':
        break

