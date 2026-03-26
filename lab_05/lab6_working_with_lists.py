#Lab 6: Working with lists (loops, range, patterns)
magicians = ['alice', 'bob', 'chen']
for m in magicians:
    print(m.title())
    print(m.upper())
    print(f"Great job, {m.title()}!")
print("Finished processing magicians.\n")
print('Finished the loop.')
# Use enumerate to print item numbers starting at 1:
tasks = ['read sensor', 'filter noise', 'log data', 'analyze data', 'send alert']
for i, t in enumerate(tasks, start=1):
    print(f"{i}. {t}")
#Create sequences and simple patterns:
print(list(range(1, 6))) # 1..5
print(list(range(0, 11, 2))) # evens 0..10
# Squares 1..10
squares = []
for n in range(1, 11):
    squares.append(n * n)
print(squares)
# First 10 multiples of 3
multiples_of_3 = []
for n in range(1, 11):
    multiples_of_3.append(n * 3)
print(multiples_of_3)
values = [1, 2, 3, 4, 5, 6]
for v in values[:3]:
    print('First three:', v)
# Copying a list correctly
a = ['dumplings', 'noodles', 'tea']
b = a[:] # real copy
b.append('fruit')
print('a:', a)
print('b:', b)
# Aliasing (same list)
c = a # NOT a copy
# When c = a, both c and a refer to the same list object in memory.
# Appending to c modifies the shared list, so a also appears to change.
c.append('water')
print('a after alias change:', a)
print('c:', c)     