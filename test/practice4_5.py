scores={'Tom':80,'Jack':95,'Lucy':88}
max=0
for i in scores.keys():
    if scores[i]>=max:
        max=scores[i]
print(max)