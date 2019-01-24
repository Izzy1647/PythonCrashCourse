aliens = []
for alien_number in range(0,30):
    new_alien = {'colour':'green',
                 'points':5,
                 'speed':'slow',
                 }
    aliens.append(new_alien)
print(len(aliens))

for alien in aliens[:3]:
    if alien['colour'] == 'green':
        alien['colour'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'

for item in aliens[:10]:
    print(item)

print('\n')

for alien in aliens[:10]:
    if alien['colour'] == 'yellow':
        alien['colour'] = 'red'
        alien['points'] = 15
        alien['speed'] = 'fast'
    elif alien['colour'] == 'green':
        alien['colour'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'

for _ in aliens[:15]:
    print(_)