num_terms = 10

sum = 0
tmp_sum = 1
for i in range(1, num_terms + 1):
    sum+=1/tmp_sum
    tmp_sum*= i
print("the result is ",sum) #Maybe this is Euler's number :)
