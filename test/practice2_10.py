num=input()
flag=0
for j in range (2,int(num)):
    if int(num)%j==0:
        flag=1
        break
        
if num==2 or flag==0:
    print('prime')