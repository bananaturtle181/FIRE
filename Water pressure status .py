# Given a water pressure reading, this script will determine its status 
def pressure_status(pressure_kpa):
    if pressure_kpa <= 0: return "Invalid" #Trying single line syntax for if statements
    elif pressure_kpa <= 300: return "Low"
    elif 300 < pressure_kpa <= 600: return "Normal"
    else: return "High"

def pressure_report(pressure_kpa, site_name="Unknown Site"):
    status = pressure_status(pressure_kpa)
    if status == "Invalid":
        return None
    else: return f"Pressure at {site_name} is {status} ({pressure_kpa}kPa)"


print(pressure_report(450, "Pump Station A"))
print(pressure_report(250))
print(pressure_report(-10, "Reservoir 3"))

