import random
name_length = int(input('请问你想要多长的名字？'))
a=input('请问你想要那个首字母？')
for I in range (name_length):
    name = a + ''.join(random.sample('abcdefghijklmnopqrstuvwxyz', name_length-1))
print(name)
print(i for i in range (1,11))