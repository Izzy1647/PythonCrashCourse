with open('pi_digits.txt') as file_object:
    # contents = file_object.read()
    # print(contents.rstrip())
    # for line in file_object:
    #     print(line)

    # for line in file_object:
    #     print(line.rstrip())

    lines = file_object.readlines()

pi = ''
for line in lines:
    # print(line.rstrip())
    pi += line.strip()

print(pi)


import math
print(round(math.pi,100))


if '98' in str(math.pi):
    print('yes')