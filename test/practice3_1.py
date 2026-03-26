car=input("请输入汽车品牌:").strip().lower()
if car=="bmw" or car=="benz":
    print("高端！")
elif car=="byd" and car!="tesla":
    print("国产新能源")
elif car=="xiaomi":
    print("乐色")
else:print("杂牌！")
