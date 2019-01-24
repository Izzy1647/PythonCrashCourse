# 3-4 3-5 3-6 3-7 3-9

guest_list = ['Jobs','Jordan','Hazard']
for guest in guest_list:
    print('Invite you to dinner,'+guest)

print('\nJordan is not coming,Jokic is coming.\n')

guest_list.remove('Jordan')
guest_list.append('Jokic')
for guest in guest_list:
    print('Invite you to dinner,'+guest)

print('\nWe have found a bigger table,and we will introduce Murray,Terry and Penny\n')

guest_list.insert(0,'Murray')
guest_list.insert(2,'Terry')
guest_list.append('Penny')
print(guest_list)
for guest in guest_list:
    print('Invite you to dinner,'+guest)
print(len(guest_list),'guests are in.')
print('\nOnly two will have this chance\n')

while len(guest_list)>2:
    popped_guest = guest_list.pop()
    print('Sorry that you cannot come,'+popped_guest)

for guest in guest_list:
    print('You are still in,'+guest)

del guest_list[1]
del guest_list[0]
print(guest_list)


print(len(guest_list),'guest is in.')
