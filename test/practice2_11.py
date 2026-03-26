a=0
b=1
c=0
for i in range (10):
    c=a
    a=b
    b=b+c
    print(c)