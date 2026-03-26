#task1
sensor = {'type': 'humidity', 'unit': '%', 'value': 20.0}
print(sensor)
print('Type:', sensor['type'])
print('Unit:', sensor['unit'])
# Missing key: use get()
location = sensor.get('location')
print('Location:', location)
# get() with a default value
location2 = sensor.get('location', 'unknown')
print('Location (default):', location2)
#A KeyError happens when you try to access a
#dictionary item with a key that doesn’t exist

#task2
alien = {}
alien['color'] = 'green'
alien['points'] = 5
print('Start:', alien)
# Modify
alien['color'] = 'yellow'
print('After modify:', alien)
# Add more keys
alien['x_position'] = 0
alien['y_position'] = 25
print('After add:', alien)
# Delete a key
del alien['points']
print('After delete:', alien)
#Add key"speed"
alien["speed"]="slow"
alien["spped"]="fast"
#If absence is unexpected and should be caught
#early: allow KeyError or handle it explicitly
#with try/except.


#task3
print('len(sensor) =', len(sensor))
print("'type' in sensor?", 'type' in sensor)
empty = {}
if empty:
    print('Not empty')
else:
    print('Dictionary is empty')

#task4
modules = {
    'EGJ040S': 'Software Engineering',
    'EGJ101A': 'Signals and Systems',
    'EGJ120B': 'Control Fundamentals'
}
print('--- items() ---')
for code_, name in modules.items():
    print(code_, '->', name)
print('--- keys() sorted ---')
for code_ in sorted(modules.keys()):
    print(code_, '->', modules[code_])
print('--- values() ---')
for name in modules.values():
    print(name)

print("\nAligned modules:")
for code, name in modules.items():
    print(f"{code:<10} | {name}")