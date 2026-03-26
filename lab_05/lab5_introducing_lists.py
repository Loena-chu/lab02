# Lab 5: Introducing lists
sensor = ['temperature', 'light', 'height', 'depth', 'proximity']
print(sensor)
print(sensor[0])
print(sensor[-1])
sensor_readings = [23.5, 1013.2, 12.8, 45.0]  # Temperature (°C), Pressure (hPa), Voltage (V), Humidity (%)
print(sensor_readings)  # Print all readings
print(sensor_readings[1])  # Access pressure reading
print(sensor_readings[-1])  # Access latest humidity reading
automation_tasks = ['initialize_system', 'calibrate_sensors', 'run_diagnostics', 'execute_process', 'log_results']
print(automation_tasks)  # Print all tasks
print(automation_tasks[0])  # Access first task
print(automation_tasks[-1])  # Access final task
device_statuses = ['active', 'inactive', 'active', 'maintenance', 'active']
print(device_statuses)  # Print all statuses
print(device_statuses[2])  # Check third device status
print(device_statuses[-2])  # Check second-to-last device status
cars = ['bmw', 'audi', 'nio', 'geely']
print(cars[3]) # IndexError on purpose
print(cars[-1])
print(cars[len(cars) - 1])
ev_brands = ['NIO', 'Geely', 'Chery', 'SAIC', 'Great Wall', 'Li Auto']
print(ev_brands[0:3]) # first 3
print(ev_brands[2:5]) # middle slice
print(ev_brands[:2]) # from start
print(ev_brands[3:]) # to end
print(ev_brands[-3:]) # last 3
print(ev_brands[::2]) # step = 2
print(ev_brands[1:4:2]) # step = 2, start from index 1
sensors = ['temperature', 'pressure', 'proximity']
print('Start:', sensors)
# Change an element
sensors[0] = 'temp'
print('Change:', sensors)
# Add elements
sensors.append('humidity')
sensors.insert(1, 'flow')
print('Add:', sensors)
# Extend using another list
more = ['level', 'vibration']
sensors.extend(more)
print('Extend:', sensors)
# Remove elements
del sensors[0]
sensors.remove('proximity')
last = sensors.pop()
print('After remove:', sensors)
print('Popped item:', last)

# --- explicit example matching user request ---
# start with a fresh sensor list
sensors2 = ['temperature', 'pressure', 'proximity']
print('\nOriginal sensors2:', sensors2)
# add two more sensors
sensors2.append('humidity')
sensors2.append('flow')
print('After adding two:', sensors2)
# remove one by value
sensors2.remove('pressure')
# remove one by index
del sensors2[0]
print('Final sensors2 after removals:', sensors2)