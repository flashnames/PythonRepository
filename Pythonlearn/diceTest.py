users={
    'aeinstein':{
        'first':'albert',
        'last':'einstein',
        'location':'princeton',
    },
    'mcurie':{
        'first':'marie',
        'last':'curie',
        'location':'paris',
    },
}

for username,user_info in users.items():
    print("\nUsername:"+username)
    full_name=user_info['first']+" "+user_info['last']
    location=user_info['location']
    print('\n fullname:'+full_name.title())
    print('\n location:'+location.title())
print("-------------------fix it after--------------------")
for username,user_info in users.items():
    print("\nUsername:"+username.title())
    full_name=user_info['first']+" "+user_info['last']
    location=user_info['location']
    print('\n fullname:'+full_name.title()+'\n location:'+location.title())


print("------------------------------------")

userinfos={
    "username":"胡峻豪",
    "lastname":"胡峻豪",
    "age":22,
    "city":"江西赣州",
}
userinfors={
    "username":"张权",
    "lastname":"张权",
    "age":21,
    "city":"江西赣州",
}
userinformations={
    "username":"伍香军",
    "lastname":"伍香军",
    "age":20,
    "city":"江西赣州",
}


people=[userinfos,userinformations,userinfors]

for peopleinfo in people:
    for personinfo,personinfomation in peopleinfo.items():
        print(personinfo+"是"+str(personinfomation))


purplecat={
    "pettype":"cat",
    "mastername":"jerry",
}


orangedog={
    "pettype":"dog",
    "mastername":"tom",
}

redpig={
    "pettype":"pig",
    "mastername":"charls",
}

pets=[purplecat,orangedog,redpig]

for pet in pets:
    print("\n pettype is %s \n mastername is %s"%(pet['pettype'],pet['mastername']))

favorite_plces={
    "胡峻豪":["科技馆","历史馆","水族馆"],
    "朱晨光":["历史馆","博物馆","公园"],
    "伍香军":["河边","桥上","咖啡馆"],
}
for name,favorite_plce in favorite_plces.items():
    print(name+" favorite place:")
    for favoriteplce in favorite_plce:
        print(favoriteplce)


favorite_nums={
    "胡峻豪":[9,4,2,1,5],
    "张权":[7,11,33,66,99],
    "伍香军":[6,123,23,154],
    "鲁斌林":[321,5315,6757,342,7867],
    "朱晨光":[5345,231567,437658,2312313],
}

for name,favorite_num in favorite_nums.items():
    print(name+" favorite num:")
    for favoritenum in favorite_num:
        print(favoritenum)

cities={
    "洛阳":{
        "所属国家":"中国",
        "人口数":"713.67万",
        "现实":"河南省的城市",
    },
    "北京":{
        "所属国家":"中国",
        "人口数":"2154.00万",
        "现实":"中国的首都和行政中心,还是直辖市",
    },
    "上海":{
        "所属国家":"中国",
        "人口数":"2424.00万",
        "现实":"中国的经济中心以及特区,还是直辖市",
    }
}

for cityname,city_info in cities.items():
    print("这座城市的名字是"+cityname+",这座城市的信息如下:"+"\n")
    for cityinfo,cityinformation in city_info.items():
        print(cityinfo+"是"+cityinformation+"\n")