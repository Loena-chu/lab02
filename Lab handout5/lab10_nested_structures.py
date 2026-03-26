def count(dic,i):
    num=0
    for j in list(dic.keys()):
        if num==i:
            return(j)
        num+=1
def enroll_student(student_code, module_code):
    global student
    # 1. 找到目标学生
    for student in students:
         if student["student_code"] == student_code:
             # 2. 检查模块是否已存在
             if module_code in student["modules"]:
                 print(f"⚠️  警告：学生 {student_code} 已注册模块 {module_code}，无需重复注册！")
                 return
             print('ok')
aliens = [
    {'color': 'green', 'points': 5, 'position_x': 0, 'position_y': 25, 'speed': 'slow'},
    {'color': 'yellow', 'points': 10, 'position_x': 50, 'position_y': 25, 'speed': 'medium'},
    {'color': 'red', 'points': 15, 'position_x': 100, 'position_y': 25, 'speed': 'fast'},
]
for a in aliens:
    print(a['color'], a['points'], a['position_x'], a['position_y'], a['speed'])

#task2
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'cheese', 'onion']
}
print('Crust:', pizza['crust'])
print('Toppings:')
for t in pizza['toppings']:
    print('-', t)
pizza["toppings"].append("pepper")
for i in range (len(pizza["toppings"])):
    print(pizza["toppings"][i])

#task3
users = {
    'wangwei': {'first': 'Wei', 'last': 'Wang', 'location': 'Shanghai'},
    'lihua': {'first': 'Hua', 'last': 'Li', 'location': 'Beijing'},
    'chujiaheng':{'first':'chu','last':'jia','location':'Hz'}
}
for username, info in users.items():
    full_name = f"{info['first']} {info['last']}"
print(username, '->', full_name, '|', info['location'])
users["yihang"]={'first':'cheng','last':'yihang','location':'Maanshan'}
sort=list(range(len(users)))
print(sort)
for i in range(len(sort)):
    for j in range(0,len(sort)-i-1):
        if count(users,sort[j])>count(users,sort[j+1]):
            sort[j],sort[j+1]=sort[j+1],sort[j]
for i in sort:
    print (count(users,i))
#Safely accessing nested dictionary keys

#task4
students = [
    {'student_code': 2025001, 'first_name': 'Ming', 'family_name': 'Zhang',
    'modules': ['EGJ040S', 'EGJ101A']},
    {'student_code': 2025002, 'first_name': 'Yan', 'family_name': 'Liu',
    'modules': ['EGJ040S']},
]
modules = {
    'EGJ040S': {'name': 'Software Engineering', 'credits': 10, 'block': 'B1'},
    'EGJ101A': {'name': 'Signals and Systems', 'credits': 10, 'block': 'B1'},

}
students_sorted = sorted(students, key=lambda s: (s['family_name'],
s['student_code']))
for s in students_sorted:
    print(f"{s['student_code']} {s['family_name']} {s['first_name']}")
for mcode in s['modules']:
    minfo = modules.get(mcode)
if minfo is None:
    print(' -', mcode, '(unknown module)')
else:
    print(' -', mcode, minfo['name'])
students.append({'student_code': 2025003, 'first_name': 'Yihang', 'family_name': 'Cheng',
    'modules': ['EGJ120B']})
modules['EGJ120B']={'name': 'Control Fundamentals', 'credits': 10, 'block': 'B1'}
enroll_student('2025002','EGJ040S')