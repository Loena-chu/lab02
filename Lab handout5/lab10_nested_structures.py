aliens = [
    {'color': 'green', 'points': 5, 'position_x': 0, 'position_y': 25, 'speed': 'slow'},
    {'color': 'yellow', 'points': 10, 'position_x': 50, 'position_y': 25, 'speed': 'medium'},
    {'color': 'red', 'points': 15, 'position_x': 100, 'position_y': 25, 'speed': 'fast'},
]
for a in aliens:
    print(a['color'], a['points'], a['position_x'], a['position_y'], a['speed'])

#task2
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'cheese', 'onion']
}
print('Crust:', pizza['crust'])
print('Toppings:')
for t in pizza['toppings']:
    print('-', t)