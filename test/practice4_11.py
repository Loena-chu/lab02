d={'a':1,'b':2,'c':1}
d_t={}
for i in list(d.keys()):
    if d[i] not in list(d_t.keys()):
        d_t[d[i]]=[]
    d_t[d[i]].append(i)
print(d_t)