def process_transfers(transfers):
    results = {}


    for users in transfers: 
        status = "Processed"
        transfer_per_user = 0

        for values in transfers[users]:

            try: 
                amount = int(values)

            except ValueError:
                status = "Invalid transfer"
                break
            
            if amount <= 0 or amount > 10000:
                status = "Invalid transfer"
                break 

            transfer_per_user += amount
            
        if status == "Invalid transfer": 
            results[users] = {"Status": "Invalid transfer"
            }
        else:
            results[users] = {"Total transferred": transfer_per_user,
                            "Status": status
            }

    return results


transfers = {
    "Alice": [200, 300, 700],
    "Bob": [100, -50, 200],
    "Charlie": [500, "oops", 300],
    "Diana": [1000, 2000]
}


results = process_transfers(transfers)
print(results)