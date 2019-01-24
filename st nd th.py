# 5-11
digits = list(range(1,10))
# print(digits)

for digit in digits:
    if digit == 1:
        print('1st')
    elif digit == 2:
        print('2nd')
    elif digit == 3:
        print('3rd')
    else:
        number = str(digit)+'th'
        print(number)


