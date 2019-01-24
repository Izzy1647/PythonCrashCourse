# 5-10
current_users = ['AshLey','kat','cuRry','david','fabian']
new_users = ['kAt','Ashley','cindy','fog','yeezy']
current_users_lower = []
for user in current_users:
    user = user.lower()
    current_users_lower.append(user)

for user in new_users:
    if user.lower() in current_users_lower:
        print('Name being used.Change a name.')
    else:
        print('Available.')