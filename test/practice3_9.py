scores=[78,95,88,67,50,85,99,76]
def sort(list,p,q):
    if p>=q:
        return
    pivot=list[q]
    i=p-1
    for j in range(p,q):
        if list[j]<pivot:
            i+=1
            list[i],list[j]=list[j],list[i]
    list[i+1],list[q]=list[q],list[i+1]
    sort(list,p,i)
    sort(list,i+2,q)
sort(scores,0,7)
print(scores[-3:])


