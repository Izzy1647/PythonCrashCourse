# 6-9

favaourite_place = {'Ashley':['Rome','Washington','SanTorini'],
                    'Yui':['Tokyo','Vietnam'],
                    'Izzy':['Taiwan','Sirilanka','Milan']
                    }

for name,places in favaourite_place.items():
    print(name,'wants to go to:')
    for place in places:
        print(place)
    print('\n')