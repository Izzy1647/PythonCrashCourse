# 8-14

def mobile_profile(manufacturer,model,**mobile_info):
    profile = {}
    profile['manufacturer'] = manufacturer
    profile['model'] = model
    for k,v in mobile_info.items():
        profile[k] = v
    return profile

car = mobile_profile('subaru','outback',color = 'blue',tow_package = True)
print(car)