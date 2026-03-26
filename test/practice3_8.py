scores=[88,45,92,67,55,78,91,31,99,60]
index=[]
max,a,b=0,0,0
for i in range(len(scores)):
    if scores[i]<60:
        a+=1
        if scores[i]>max:
            max=scores[i]
    else:
        index.append(i)
        if scores[i]>=90:
            b+=1
print("不及格：",a,"    优秀:",b,"     及格编号",index,"     不及格最高：",max)


