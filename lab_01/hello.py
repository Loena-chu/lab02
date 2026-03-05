print ('202521516048')
print ('JiahengChu')
print(chr(ord('J')+1))
V = float(input("Enter voltage V (0 to 10 V): "))
a = float(input("Enter calibration slope a (degC per V): "))
b = float(input("Enter calibration offset b (degC): "))
T = a * V + b
print(f"Voltage: {V:.3f} V")
print(f"Temperature: {T:.3f} degC")