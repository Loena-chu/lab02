nums=[3,8,11,6,14,7]
evennumlist=[]
for i in range(len(nums)):
    for j in range (2,nums[i]):
        if nums[i]%j==0:
            evennumlist.append(nums[i])
            break
print(evennumlist)