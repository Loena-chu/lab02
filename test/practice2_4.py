nums=[1,2,3,4,5]
len=len(nums)
a=nums[4]
for i in range (len-1,0,-1):
    nums[i]=nums[i-1]
nums[0]=a
print(nums)