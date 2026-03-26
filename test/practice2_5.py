nums=[1,2,3,5,6]
len=len(nums)
sort=nums[0]
missing=-1
for i in range(len):
    if nums[i]!=sort:
        missing=sort
        sort=nums[i]
    sort+=1
print("Missing number",missing)