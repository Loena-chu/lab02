import random
score=[0]*8
for i in range(8):
    score[i]=random.randint(0,100)
print("Original scores:")
for i in range(8):
    print(f"{score[i]:3d}", end=" ")
print(max(score))
print(min(score))
print(f"Average score: {sum(score)/len(score):.2f}")
print([n for n in score if n>=60])
print([n**2 for n in range(1,11) if n%2==0])