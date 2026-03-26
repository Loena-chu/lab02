students=[
    {'name':'Tom','Score':90},
    {'name':'Jerry','Score':55},
    {'name':'BOb','Score':78}
]
def get_passed(lst):
    passed=[]
    for i in lst:
        if i['Score']>=60:
            passed.append(i['name'])
    return(passed)
print(get_passed(students))
def get_top_student(lst):
    sum=0
    num=0
    max=0
    for i in lst:
        sum+=i['Score']
        num+=1
        if i['Score']>=max:
            max=i['Score']
            Max_stu=i
    return(sum/num,Max_stu)
print(get_top_student(students))