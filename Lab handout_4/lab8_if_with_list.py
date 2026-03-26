# Lab 8: if statements with lists
allowed = ['start', 'stop', 'reset', 'status']
blocked = ['shutdown', 'format', 'delete']
cmd = input('Enter command: ').strip().lower()
if cmd in allowed:
    print('OK:', cmd)
elif cmd in blocked:
    print('Blocked command:', cmd)
else:
    print(f'I don\'t recognize "{cmd}". Try: {", ".join(allowed)}')
readings = [2.5, 0.2, 10.5, -1.0, 3.3]
for v in readings:
    if v < 0:
        print(v, '-> FAULT (negative)')
    elif v > 10:
        print(v, '-> FAULT (too high)')
    elif v < 1:
        print(v, '-> LOW')
    else:
        print(v, '-> OK')
readings = [2.5, 0.2, 3.3]
any_fault = any((v < 0 or v > 10) for v in readings)
all_ok = all((0 <= v <= 10) for v in readings)
print('any_fault =', any_fault)
print('all_ok =', all_ok)