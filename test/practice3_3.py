banned=['admin','root','god']
username=input("请输入用户名：")
if username.strip().lower() not in banned:
    print("welcome logging")
else:print("the name is banned")