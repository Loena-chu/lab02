# Lab 7: Decisions and branching
brand = input('Enter a car brand: ').strip()
if brand.lower() == 'geely':
    print('Local brand detected: Geely')
else:
    print('Brand entered:', brand)
# the format we enter might contain spaces, 
# so we use strip() to remove them. 
# We also use lower() to make the comparison case-insensitive.
text = input('Enter temperature in °C: ').strip()
try:
    temp = float(text)
except ValueError:
    print('Error: please enter a number')
else:
    if temp < -20 or temp > 120:
        print('FAULT')
    elif temp < 10:
        print('COLD')
    elif temp < 60:
        print('NORMAL')
    else:
        print('HOT')

# Boundary tests
test_temps = [-20, 10, 60]
for t in test_temps:
    if t < -20 or t > 120:
        print(f'For {t}: FAULT')
    elif t < 10:
        print(f'For {t}: COLD')
    elif t < 60:
        print(f'For {t}: NORMAL')
    else:
        print(f'For {t}: HOT')

# Alarm rule
temp = 85
pressure = 5.1
emergency_stop = True
high_temp = temp > 80
high_pressure = pressure > 5
alarm_on = (high_temp and high_pressure) or emergency_stop
print('alarm_on =', alarm_on)
