list1=['apple','banana','apple','cherry','date']
list2=['banana','date','apple','elderberry']
def sort(list):
    res=[list[0]]
    for i in range(1,len(list)):
        key=list[i]
        if key in res:
            continue
        j=len(res)-1
        while j>=0 and key<=res[j]:
            j-=1
        res.append(0)
        for k in range(len(res)-1,j+1,-1):
            res[k]=res[k-1]
        res[j+1]=key
    return(res)
list3=list1+list2
print(sort(list3))

            

        