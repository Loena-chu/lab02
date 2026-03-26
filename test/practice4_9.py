word=['a','b','a','c','b','a']
dic={}
for i in word:
    if i not in dic.keys():
        dic[i]=0
    dic[i]+=1
print(dic)