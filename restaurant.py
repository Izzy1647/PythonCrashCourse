# 9-1 9-2 9-4 9-6

class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = 0
        # print('name:'+self.name+'\ntype:'+self.type)

    def describe_restaurant(self):
        print('name:' + self.name + '\ntype:' + self.type)

    def set_number_served(self,number):
        self.number_served = number

    def increment_number_served(self,increment):
        self.number_served += increment

    def open_restaurant(self):
        print('Welcome...')

class IceCreamStand(Restaurant):
    def __init__(self,name,type):
        super().__init__(restaurant_name=name,cuisine_type=type)
        self.flavours = ['chocolate','vacine','mango']
    def displayIcecream(self):
        print(self.flavours)
        print(self.number_served)


#
# williles = Restaurant('Williles','Indian Food')
# williles.describe_restaurant()
# williles.open_restaurant()
# print(williles.number_served)
# williles.set_number_served(12)
# williles.increment_number_served(10)
# williles.increment_number_served(10)
# print(williles.number_served)

baxi = IceCreamStand('baxi','Tradition')

baxi.displayIcecream()
