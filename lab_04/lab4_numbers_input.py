seconds_total = 3601
minutes = seconds_total // 60
seconds = seconds_total % 60
print(f"{seconds_total} seconds is {minutes} minutes and {seconds} seconds")
c = 23.0
f = (c * 9/5) + 32
print(f"Celsius: {c:.2f} °C")
print(f"Fahrenheit: {f:.2f} °F")
name = "S1"
val = 2.5
print(f"{name:10s} {val:8.3f}")
text=input("Enter a voltage value between 0 and 10: ")
try:
    voltage = float(text)
except ValueError:
    print("Error: please enter a number, for example 2.5")
else:
    if voltage < 0 or voltage > 10:
        print("Error: V must be between 0 and 10")
    else:
        physical_value = 3 * voltage
print(f"Voltage: {voltage:.3f} V")
print(f"Scaled value: {physical_value:.3f} units")