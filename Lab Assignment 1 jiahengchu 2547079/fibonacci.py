num_terms = 10

first_num= 0
second_num = 1 
for i in range(num_terms):
    first_num,second_num=second_num,first_num+second_num #using an interesting operating method in this program:)
    print("Fibonacci Number:",i+1,"=",first_num)    