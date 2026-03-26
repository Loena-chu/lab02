d={
    's1':'math',
    's2':'math',
    's3':'english'
}
record=[]
for i in d.values():
    print(i) if i not in record else None
    record.append(i)