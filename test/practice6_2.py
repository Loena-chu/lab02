def append_item(lst=None):
    if lst==None:
        lst=[]
    lst.append(1)
    return(lst)
print(append_item())
print(append_item())
print(append_item())
#the default parameter would acumulate in the definition 
#function if the parameterr is dictionary or list!