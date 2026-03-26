class Dog:
    leg_num=4
    has_hair=True
    has_tail=True

    def bark(self):
        print('狗叫')
    def bite(self):
        print(self.name,"咬人")
    def __init__(self,name,breed,age):
        self.name=name
        self.breed=breed
        self.age=age

    
cyh=Dog(name="程一航",breed="asia",age=19)
Dog.leg_num=3
print(cyh.leg_num)
print(cyh.age)
cyh.bite()