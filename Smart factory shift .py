def machine_output(machines):
    result = {}
    
    # defining outer loop which loops over the different machines 
    for machine in machines:
        high_average_output = 0
        high_output_streak = False
        total_output_machine = 0
       

        #defining middle loop which loops over each shift (or row) of the list 
        for row in machines[machine]:
            high_output_count = 0
            total_output_shift = 0 # moved here so averages can be calculated per shift(row)
            total_output_machine += total_output_shift

            #defining inner loop which loops over each output value of each row 
            for output in row:
                
                if output < 0: break

                total_output_shift += output

                if output >= 8:
                    high_output_count += 1

                else: high_output_count = 0

                if high_output_count >= 3: high_output_streak = True

            if total_output_shift / len(row) >= 5:    # I think this fixes issue 1 as now the full shift values can be included in the average calculations
                high_average_output += 1
            
        result[machine] = {"Total output per machine": total_output_machine,
                            "High output streak": high_output_streak,
                            "High average shifts": high_average_output
        }
            
    return result

machines = {
    "Machine A": [
        [5, 7, 6, 8],     # Shift 1
        [2, 3, 1, 0],     # Shift 2
        [9, 10, 11, 12]   # Shift 3
    ],
    "Machine B": [
        [0, 0, 1, 2],
        [4, 5, 6, 7]
    ]
}

final_output = machine_output(machines)
print(final_output)