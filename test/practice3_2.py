try:
    age=int(input("请输入年龄："))
except:
    age=-1
if age<0:
    print("无效！")
elif age <18:
    print("未成年人")
elif age <65:
    print("成年人")
else: print("老年人")
if age >=100:
    print("长寿传奇！")