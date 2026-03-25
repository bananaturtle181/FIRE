# Function for detgermining operational status 
def operation_status(pressure, time):
 
    if pressure < 0 or time <0 or time >23:
        return "Invalid pressure or time"
    
    if 0 <= time <= 6 or 9 <= time <= 17 or 20 <= time <= 23:
        time_status = "Off peak"
    else:
        time_status = "Peak"
    
    if pressure <= 300:
        pressure_status = "Low"

    elif 300 < pressure < 600:
        pressure_status = "Normal"

    elif pressure >= 600:
        pressure_status = "High"
    return f"Pressure = {pressure_status} during {time_status}"
         
    
# Function for produces advisory messages using status 
def warning_message(pressure, time):

    status = operation_status(pressure, time);

    if status == "Invalid pressure or time": return "Invalid sensor readings. Please check values"

    if status == "Pressure = Low during Off peak": 
        return "Suggesting monitoring"

    if status == "Pressure = High during Off peak":
        return "Advising immediate action"
    
    if status == "Pressure = Low during peak":
        return "Advising immediate action"

    if status == "Pressure = High during peak": 
        return "Suggesting monitoring"
    else: return "Indicating normal operation"

        
          

print(warning_message(20,10))
