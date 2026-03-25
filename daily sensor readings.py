# defining function 
def sensor_readings(sensors):

    #Initialising variables for whole function
    results = {}
    
    for sensor_number in sensors:
        #Initialising variables for sensors loop 
        total_readings_sensor = 0
        alert_hours = 0
        status = "Processed"

        try: 
        #Inner loop for sensor values 
            for values in sensors[sensor_number]:
            
                if values < 0:
                    raise ValueError("Sensor has detected a negative value. Rest of the readings for this sensor will be skipped")
                
                elif values > 100: 
                    alert_hours += 1
             
                total_readings_sensor += values

            results[sensor_number] = {"Total readings": total_readings_sensor, 
                                      "Alert hours": alert_hours,
                                      "Sensor status": status

            }
        except ValueError:
            results[sensor_number] = {"Total readings": None, 
                                      "Alert hours": None,
                                      "Sensor status": "Invalid sensor"
            } 

    return results

sensors = {
    "Sensor 1": [23, 45, 110, 55],
    "Sensor 2": [10, -5, 20],
    "Sensor 3": [50, 60, 70, 80, 90]
}

results = sensor_readings(sensors)
print(results)