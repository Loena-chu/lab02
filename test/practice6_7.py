def apply_filter(data,func):
    lst=[]
    for i in data:
        if func(i)==True:
            lst.append(i)
    return(lst)
    
def is_even(x):
    return(x%2==0)
print(apply_filter([1,2,3,4],is_even))