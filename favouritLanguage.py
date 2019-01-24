# 6-6

favourite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}

investigate_list = ['jen','sarah','bob','edward','phil','daney','pickie']

for name in investigate_list:
    if name in favourite_languages.keys():
        print('Thank you for the investigation,'+str(name.title())+'.')
    else:
        print('Come on do the investigation,'+str(name.title())+'.')