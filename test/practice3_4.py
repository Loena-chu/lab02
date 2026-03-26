temp=float(input("temp:"))
humi=float(input("humi:"))
if temp>35 and humi>80:
    print("高温高湿，停机！")
elif temp>35:
    print("高温")
elif temp<10:
    print("low温")
elif humi>90:
    print("高湿")
else: print("正常")