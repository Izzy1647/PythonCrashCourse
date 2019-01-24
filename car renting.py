# 7-1 7-2 7-3

# car = input('Which car do you want to rent? ')
# print('Let me see if we have a',car)

number_of_guests = input('How many guests? ')
if int(number_of_guests) > 8:
    print('Too many.')
else:
    print('Ok.')

number = input('Input a number: ')
if int(number) % 10 == 0:
    print('Yes.')
else:
    print('No.')
