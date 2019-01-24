# 7-10

destinations = {}
act = True
while act:
    name = input('What is your name: ')
    destination = input('Where do you want to travel to most: ')
    destinations[name] = destination

    repeat = input('Next one? print"yes/no": ')
    if repeat == 'no':
        act = False
for name,destination in destinations.items():
    print(name+': '+destination)
