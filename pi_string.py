filename = 'pi_million_digits.txt'

pi_string = ''
with open(filename) as file_project:
    lines = file_project.readlines()

for line in lines:
    pi_string += line.strip()

print(pi_string[:102])
print(len(pi_string))

while True:
    birthday = input('Input your birthday: ')
    if birthday in pi_string:
        where = pi_string.find(birthday)
        print('in,at',where)
    else:
        print('not in ')
    act = input('press q to quit, or c to continue: ')
    if act == 'q':
        break

