def machine_output(machines):
    threshold = int(input("What is the threhold units produced? "))
    results = {}

    # defining outer loop to loop through keys 
    for key in machines:

        #initialising variables for each machine 
        total_output = 0
        high_output_streak = False 
        high_output_streak_count = 0  
        high_output_day = 0     

        # defining inner loop to loop through units produced 
        for units in machines[key]:
            total_output += units

            if units >= threshold: 
                high_output_streak_count += 1
                high_output_day += 1
               

                if high_output_streak_count >= 3: high_output_streak = True 

            elif units < threshold:
                
                high_output_streak_count = 0
        
        results[key] = {"Total units": total_output,
            "Streak achieved": high_output_streak,
            "High output days": high_output_day
        }
    return results
                

machines = {
    "Machine 1": [30, 60, 55, 20, 50, 70, 10],
    "Machine 2": [0, 0, 40, 45, 60, 65, 80],
    "Machine 3": [50, 50, 50, 50, 50, 50, 50]
}

final_results = machine_output(machines)
print(final_results)