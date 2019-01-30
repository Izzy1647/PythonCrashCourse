# 10-3 10-4

# guest_name = input('Input your name: ')
file_name = 'guest.txt'
with open(file_name,'w') as file_object:
    while True:
        guest_name = input('Input your name: ')
        print('Welcome,'+str(guest_name))
        file_object.write('Access '+str(guest_name)+'\n')
        act = input('"q" to quit; "c" to continue: ')
        if act == 'q':
            break
