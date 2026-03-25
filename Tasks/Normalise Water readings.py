# Enter given data 
readings = [1.2, 1.3, 1.5, 1.4]

# Defining a function 
def normalise_readings(readings):

    normalised_values = []

    # Finding min and max values
    min_value = min(readings)
    max_value = max(readings)

    # Converting readings 
    for value in readings:
        normalised_value = (value - min_value)/(max_value - min_value)
        normalised_values.append(normalised_value)

    return{

    "min": min_value,
    "max": max_value,
    "Normalised values": normalised_values

    }

normalised = normalise_readings(readings)
if normalised is None:
    print ("No values in readings")
else: 
    print(normalised)