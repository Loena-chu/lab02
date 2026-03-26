list=["banana","apple","grape","passionfruit","strawberry"]
print(list[0])
print(list[-1])
def search(fruit):
    for i in range(len(list)):
        if list[i] == fruit:
            return i
    return -1
a="banana"
print(search(a)+1)
list[0]="watermelon"
print(list)
list .append("orange")
print(list)
list.extend(["kiwi","melon"])
print(list) 
list.insert(2,"peach")
print(list)
list.remove("grape")
print(list)
list.pop(3)
print(list)