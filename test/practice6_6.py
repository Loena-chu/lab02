import pandas as pd
students = [
    {'name': 'Tom', 'score': 90},
    {'name': 'Jerry', 'score': 55},
    {'name': 'Bob', 'score': 78},
    {'name': 'Alice', 'score': 82}
]
def filter_passed(lst):
    for i in range(len(lst)):
        if lst[i]['score']>=60:
            lst[i]['passed']=True
        else:
            lst[i]['passed']=False
    return(lst)
def add_garde(lst):
    for i in range(len(lst)):
        if lst[i]['score']>=85:
            lst[i]['Grade']='A'
        elif lst[i]['score']>=70:
            lst[i]['Grade']='B'
        elif lst[i]['score']>=60:
            lst[i]['Grade']='C'
        else:
            lst[i]['Grade']='D'
    return(lst)
def sorted(lst):
    for i in range(len(lst)):
        for j in range(len(lst)-1,i,-1):
            if lst[j]['score']>lst[j-1]['score']:
                lst[j],lst[j-1]=lst[j-1],lst[j]
    return(lst)
def processed_stu(stu):
    return(filter_passed(add_garde(sorted(stu))))
processed_stu(students)
df = pd.DataFrame(students)
print(df)