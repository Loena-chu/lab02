import random
list1=[0]*20
def bubble_sort(arr):
    for i in range(20):
        list1[i]=random.randint(1,100)
    print("Original list:")
    for i in range(len(list1)):
        flag=0
        for j in range(i+1,len(list1)):
            if list1[i]>list1[j]:
                list1[i],list1[j]=list1[j],list1[i]
                flag=1
        for j in range(len(list1)-1-i,-1):
            if list1[i]>list1[j]:
                list1[i],list1[j]=list1[j],list1[i]
                flag=1
        if flag==0:
            break
    return list1
bubble_sort(list1)
print("Sorted list:")
for i in range(20):
    print(f"{list1[i]:3d}", end=" ")