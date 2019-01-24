# 6-5
river = {'nile':'Egypt','YangzteRiver':'China','Amazon':'Brazil'}
for name,area in river.items():
    print('The '+str(name.title())+' runs through '+str(area.title())+'.')

for keys in river.keys():
    print(keys.title())
for area in river.values():
    print(area.title())