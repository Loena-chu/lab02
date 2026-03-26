def remove_fail(lst):
    stu=[]
    for i in lst:
        if i['score']>=60:
            stu.append(i)
    return(stu)
students = [
    {'name': 'Tom', 'score': 90},
    {'name': 'Jerry', 'score': 55},
    {'name': 'Bob', 'score': 78},
    {'name': 'Alice', 'score': 82}
]
new=remove_fail(students)
print(new)