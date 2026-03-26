nums=[55,35,7,23,45,18]
max_num=nums[0]
sec_max_num=nums[0]
for i in range(len(nums)):
    if nums[i] > max_num:
        sec_max_num = max_num
        max_num = nums[i]
if sec_max_num == max_num:
    sec_max_num = nums[1]
    for i in nums[1:]:
        if i > sec_max_num :
            sec_max_num = i
print(sec_max_num)