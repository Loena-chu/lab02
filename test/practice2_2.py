nums=[3,5,2,3,7,3,9]
a=len(nums)
b=0
for i in range(a):
    if nums[b]==3:
        for i in range(b,a-1):
            nums[i]=nums[i+1]
        a-=1
    else:
        b+=1
print(nums[:a])