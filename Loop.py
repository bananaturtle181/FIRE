# Defining counting function 
def ticket_counter(scans):
    
    valid_count = 0

    for ticket in scans:
        # if ticket != 1 or ticket != 0:

        if ticket == 1:
            valid_count += 1

    return valid_count 

scans = [1, 0, 1, 1, 0, 2, 4, 1, 0, 0, 1]

print(ticket_counter(scans))