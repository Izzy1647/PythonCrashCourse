# 8-3 8-4 8-5

def make_shirt(size='Large',pattern='I love Python'):
    print(size,pattern)

# make_shirt(size=12,pattern='r')
# make_shirt(12,'ew')
# make_shirt(12)
# make_shirt()
# make_shirt('middle')
# make_shirt(size='Large',pattern='sa')

def describe_city(city_name,country='USA'):
    print(city_name.title()+' is in '+country())

describe_city(city_name='Washington')
describe_city('Atlanta')
describe_city('Shanghai','China')

