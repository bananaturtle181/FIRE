# Setting origianl readings list as from Chat
readings = [1.2, 1.3, None, -999, 1.5]

# Defining function for reusability 
def summarised_readings(readings):
    readings_cleaned = []
    # Looping through readings list to ommit NaN and negative values
    for value in readings: 
        if value is not None and value >= 0:
            readings_cleaned.append(value)

    # Defensive coding to ensure no dividing by 0, else return min, max mean and range values 
    if len(readings_cleaned) == 0:
        return None
    
    min_value = min(readings_cleaned)
    max_value = max(readings_cleaned)
    mean_value = sum(readings_cleaned) / len(readings_cleaned)
    range_value = max_value - min_value

# Setting return values if readings_cleaned exists 
    return {
        "min": min_value,
        "max": max_value,
        "mean": mean_value,
        "range": range_value

    }

summary = summarised_readings(readings)

if summary is None:
    print("No valid readings")
else:
    print(summary)