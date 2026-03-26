# Block 5 Labs
## Files
- lab9_dictionary_basics.py: dictionary creation, access, get(),
add/modify/delete, loops
- lab10_nested_structures.py: nesting (list of dicts, list in dict, dict of
dicts), mini student records
## How to run
python lab9_dictionary_basics.py
python lab10_nested_structures.py
## Example output
```
{'type': 'humidity', 'unit': '%', 'value': 20.0}
Type: humidity
Unit: %
Location: None
Location (default): unknown
Start: {'color': 'green', 'points': 5}
After modify: {'color': 'yellow', 'points': 5}
After add: {'color': 'yellow', 'points': 5, 'x_position': 0, 'y_position': 25}
After delete: {'color': 'yellow', 'x_position': 0, 'y_position': 25}
len(sensor) = 3
'type' in sensor? True
Dictionary is empty
--- items() ---
EGJ040S -> Software Engineering
EGJ101A -> Signals and Systems
EGJ120B -> Control Fundamentals
--- keys() sorted ---
EGJ040S -> Software Engineering
EGJ101A -> Signals and Systems
EGJ120B -> Control Fundamentals
--- values() ---
Software Engineering
Signals and Systems
Control Fundamentals

Aligned modules:
EGJ040S    | Software Engineering
EGJ101A    | Signals and Systems
EGJ120B    | Control Fundamentals
```
```
green 5 0 25 slow
yellow 10 50 25 medium
red 15 100 25 fast
Crust: thick
Toppings:
- mushrooms
- cheese
- onion
mushrooms
cheese
onion
pepper
chujiaheng -> chu jia | Hz
[0, 1, 2, 3]
chujiaheng
lihua
wangwei
yihang
2025002 Liu Yan
2025001 Zhang Ming
 - EGJ101A Signals and Systems
```
## AI note (if used)
I asked AI to: explain KeyError and get() usage, safe deletion of keys, printing dictionary items in aligned columns with f-strings, suggest clearer key names for alien dictionary, safe access to nested dictionary keys.
I changed: added aligned printing code to lab9_dictionary_basics.py for better output formatting.
Verification: I ran both scripts and confirmed outputs match expected behavior for dictionary operations and nested structures.
