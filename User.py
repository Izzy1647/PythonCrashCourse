# 9-3 9-5 9-7 9-8
class User():
    def __init__(self,first,last,age):
        self.firstname = first
        self.lastname = last
        self.age = age
        self.login_attempts = 0

    def describe_users(self):
        print('first name: '+self.firstname)
        print('last name: '+self.lastname)
        print('age: '+str(self.age))

    def increment_login_attempt(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

    def greet_user(self):
        print('Hello!',self.lastname,self.firstname)

class Admin(User):
    def __init__(self,first,last,age):
        super().__init__(first,last,age)
        # self.privileges = ['can add post','can delete post','can ban user']
        self.privileges = Privileges()

    # def show_privileges(self):
    #     print('PRIVILEGES:')
    #     for privilege in self.privileges:
    #         print(' ',privilege)

    def greet_user(self):
        print('Hello Admin!', self.lastname, self.firstname)

class Privileges():
    def __init__(self):
        self.privileges = ['can add post','can delete post','can ban user']

    def show_privileges(self):
        print('PRIVILEGES:')
        for privilege in self.privileges:
            print(' ',privilege)

user1 = User('s','cs',19)
user1.describe_users()
user1.greet_user()
user1.increment_login_attempt()
user1.increment_login_attempt()
print(user1.login_attempts)

user1.reset_login_attempts()
print(user1.login_attempts)

admin1 = Admin('xdc','sac',19)
admin1.greet_user()
# admin1.show_privileges()
admin1.privileges.show_privileges()

