bucket=[0]*10
result=[]
nums=[1,3,5,3,7,1,9,5]
for i in nums:
    bucket[i]+=1
for i in range(10):
    if bucket[i] >=2:
        result.append(i)
print(result)