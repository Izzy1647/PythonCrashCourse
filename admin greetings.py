# 5-8 5-9

users_list = ['anderson','admin','terry','zippo','todd']
if users_list:
    for user in users_list:
        if user == 'admin':
            print('Hello admin,would you like to see a status report?')
        else:
            print('Hello ',user,',thank you for logging again.')
else:
    print('We need to find some users!')

