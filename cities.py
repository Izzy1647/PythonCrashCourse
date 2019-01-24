# 6-11

cities = {'Shanghai':{'country':'China',
                      'continent':'Asia',
                      'level':'superb',},
          'Milan':{'country':'Italy',
                   'continent':'Europe',
                   'level':'superb',},
          'Denver':{'country':'USA',
                    'continent':'America',
                    'level':'fair',}
          }

for city,facts in cities.items():
    print('city:',city)
    for k,v in facts.items():
        print(k,':',v)
    print('\n')
