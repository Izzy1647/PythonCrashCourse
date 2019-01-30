# 10-10

file_name = 'ATaleofTwoCities.txt'

try:
    with open(file_name) as file_object:
        contents = file_object.read()
except FileNotFoundError:
    msg = 'No such file as '+str(file_name)
    print(msg)
else:
    words = contents.split()
    num = len(words)
    print(num)
    # print(type(contents))
    num_of_word = contents.lower().count('whore')
    print(num_of_word)
