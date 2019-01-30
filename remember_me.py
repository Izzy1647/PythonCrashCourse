import json
file_name = 'username.json'
try:
    with open(file_name) as f_obj:
        user_name = json.load(f_obj)
except FileNotFoundError:
    user_name = input('name: ')
    with open(file_name,'w') as f_obj:
        json.dump(user_name,f_obj)
        print('We will remember you when you come back! '+user_name)
else:
    print('Hi back '+user_name)
# with open(file_name,'w') as f_obj:
#     json.dump(user_name,f_obj)
