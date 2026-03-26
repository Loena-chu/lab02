import random
students=['张三','李四','王五','赵六','孙七']
lenth=len(students)
def select():
    global lenth
    if lenth==0:
        print('所有都回答过')
        return
    p=random.randint(0,lenth-1)
    if len (students[p])==2:
        print('幸运儿',end='')
    print(students.pop(p))
    lenth-=1
    select()
select()

