import random

flag=0
a=[0]*20
for i in range(20):
    a[i]=random.randint(1,100)

for i in range(len(a)):
    j=len(a)-1
    flag=0
    while j>i:
        if a[j-1]<a[j]:
            a[j-1],a[j]=a[j],a[j-1]
            flag=1
        j-=1
    if flag==0:
        break
for i in range(len(a)):
    print(f"{a[i]:3d}", end=" ")        
