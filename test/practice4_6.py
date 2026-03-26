dic={'a':1,'b':2,'c':3}
print(dic.keys())
print(dic.values())
print([i for i in list(dic.keys()) if dic[i] > 1])