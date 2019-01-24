# 8-9 8-10 8-11

magician_name = ['a','b','c','d']
great_magician_name = []

def make_great(old_namelist,new_namelist):
    while old_namelist:
        current_name = old_namelist.pop()
        new_namelist.insert(0, 'The Great '+ current_name)




def show_magicians(namelist):
    for name in namelist:
        print(name)


make_great(magician_name[:],great_magician_name)
show_magicians(great_magician_name)
print(magician_name)
