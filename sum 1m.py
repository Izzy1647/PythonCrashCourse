# 4-5 4-6 4-7 4-8 4-9 4-10(slices)

million = []
for i in range(1,1000001):
    million.append(i)
print(min(million),max(million))
print(sum(million))


odd_numbers = list(range(1,20,2))
print(odd_numbers)
for odd_number in odd_numbers:
    print(odd_number)


three_numbers = []
for i in range(3,31,3):
    three_numbers.append(i)
    print(i)
print(three_numbers)

cubic_numbers = []
for i in range(1,11):
    cubic_numbers.append(i**3)
    print(i**3)
print(cubic_numbers)

cubic_numbers2 = [i**3 for i in range(1,11)]
print(cubic_numbers2)

print('The first three numbers in cubic_numbers are',cubic_numbers2[0:3])
print('The last three are:',cubic_numbers2[-3:])
