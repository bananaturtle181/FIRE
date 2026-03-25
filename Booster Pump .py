# Function 1 - Operating status based on both flow and time 
def operating_status(flow,time):
    if flow < 0:
        flow_status = "Invalid"

    elif flow <= 5:
        flow_status = "Low"
    
    elif 5 < flow <= 15:
        flow_status = "Normal"

    else:
        flow_status = "High"    

    if time < 0 or time > 23: 
        time_status = "Invalid"
    
    elif 7 <= time <= 9 or 18 <= time <= 20:
        time_status = "Peak"
    
    else:
        time_status = "Off peak"

    return flow_status, time_status
    
# Function 2 - Advisory message output 
def advisory_message(flow,time):

    flow_status, time_status = operating_status(flow,time) # I did not know I could do this - based on chatgpt previous task 

    if "Invalid" in flow_status or "Invalid" in time_status: # Also learn you can use "In" to check str values 
        message = "Error please check inputs"
    
    elif flow_status == "Low" and time_status == "Peak":
        message = "Investigate demand"

    elif flow_status == "High" and time_status == "Off peak":
        message = "Check for leaks"

    else: message = "Normal operation"

    return f"{message}"

print(operating_status(4,19))
print(advisory_message(-10,20))
print(advisory_message(4,19))
print(advisory_message(120,20))

