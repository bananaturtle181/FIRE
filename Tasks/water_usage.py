# Water values given by Chat 
readings = [120, 135, None, 142, -5, 150, None, 160]

# Removing non applicable values. Creating empty list and filling in with for loop 
readings_cleaned = []

for value in readings:
    if value is not None and value >= 0:
        readings_cleaned.append(value)

# Obtaining the total number of valid readings using len
valid_readings = len(readings_cleaned)

# Calculating total and average usages 
total_usage = sum(readings_cleaned)
average_usage = total_usage / valid_readings

#Testing results
print(f"Valid readings: {valid_readings}")
print(f"Total usage: {total_usage} units")    
print(f"Average usage: {average_usage}")

# Optional task - warning if less than 25% of original values are valid
if valid_readings <= 0.25 * len(readings):
    print(f"Warning: Number of valid readings is less than 25% of original list")
