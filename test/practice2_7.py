sentence="Python is very useful"
signpost=[0]
for i in range(len(sentence)):
    if sentence[i]==' ':
        signpost.append(i)
signpost.append(len(sentence))
print(signpost)
for i in range (len(signpost)-1,-1,-1):
    print(sentence[signpost[i-1]+1:signpost[i]],end=' ')