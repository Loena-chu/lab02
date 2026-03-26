data=[23,None,45,-10,999,34]
def clean_data(lst):
    return([i for i in lst if (i!=None)and(0<=i<100)])
print(clean_data(data))