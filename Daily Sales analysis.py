def store_data(store_input):

    results_dict = {}

    # looping through keys in dict 
    for store in store_input:
        total_sale = 0
        count = 0
        high_sales_streak = False
            # looping through values in keys 
        for sale in store_input[store]:
            
            if sale >= 0: 
            # accumulating total sales for each store 
                total_sale += sale
        
            # determining streak 
            if sale >= 5: count += 1

            elif sale <5: count = 0

            if count >= 3: high_sales_streak = True    
    
        results_dict[store] = {"Total sales": total_sale,
                               "Sale streak": high_sales_streak
        }
        
    return results_dict

store_input = {
                    "Store A": [3, 5, -1, 7, 10],
                    "Store B": [0, 0, 2, 3, 1],
                    "Store C": [5, 5, 5, 5, 5]
}

results = store_data(store_input)
print(results)