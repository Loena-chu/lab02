d={'a':0,'b':None,'c':1}
print([d[i] for i in d if (d[i] is not None) and (d[i]!= 0) ])