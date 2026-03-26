student={'name':'Tom','score':80}
key=input("输入要查询的字段：")
try:
    print(student[key])
except:
    print("Not Found")
print (list(student.keys()))