nums=[3,5,2,7,8]
len=len(nums)
for i in range(len-1):
    if nums[i]<nums[i+1]:
        print(nums[i],"<",nums[i+1])