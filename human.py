# 6-1 6-3 6-4

# information_1 = {'first_name':'Luiz','last_name':'David','age':31,'city':'London'}

# print(information_1['first_name'],information_1['last_name'],information_1['age'],information_1['city'])

vocabulary = {'int':'整数型','if':'条件判断','package':'库','array':'数组','str':'字符串类型','idle':'解释器'}

print('int:\n',vocabulary['int'])
print('if:\n',vocabulary['if'])
print('package:\n',vocabulary['package'])
print('array:\n',vocabulary['array'])
print('str:\n',vocabulary['str'])


for keys, values in vocabulary.items():
     print('\nvocabulary:',keys+'\nexplanation:',values)

# =======================


information_1 = {'first_name':'Luiz','last_name':'David','age':31,'city':'London'}
information_2 = {'first_name':'Hazard','last_name':'Eden','age':26,'city':'London'}
information_3 = {'first_name':'Costa','last_name':'Diego','age':30,'city':'Madrid'}
information_4 = {'first_name':'Pogba','last_name':'Paul','age':27,'city':'Manchester'}

people = [information_1,information_2,information_3,information_4]

for person in people:
    print(person['last_name'],person['first_name'],'City:',person['city'],'Age:',person['age'])