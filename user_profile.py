# 8-13

def build_file(first,last,**user_info):
    profile={}
    profile['first name'] = first
    profile['last name'] = last
    for k,v in user_info.items():
        profile[k] = v
    return profile

print(build_file('zhiyu','zhou',livingPlace = 'Shanghai',school = 'ShanghaiUniversity',height = 187))




