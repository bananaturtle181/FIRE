# # Defining function that takes one number in and returns one number out 
# def liters_per_s_to_m3_per_d(flow_lps):
#     if flow_lps <= 0:
#         return None

#     flow_m3 = flow_lps * 86.4

#     return flow_m3

# flow_lps = 2.5

# converted = liters_per_s_to_m3_per_d(flow_lps)
# print(converted)


# # Discount price task 
# # Defining function 
# def final_price(price, discount_percent):
#     discount_dec = discount_percent / 100
#     if discount_dec < 0 or discount_dec >1 :
#         return None 
    
#     else:
#         discount = price * discount_dec
#         discount_price = price - discount

#     return discount_price

# price = 120
# discount_percent = 15

# calculated_price = final_price(price,discount_percent)
# print(calculated_price)

# #Tax calculator task 
# def calculate_tax(amount, tax_rate=0.1):
#     if amount <= 0:
#         return None
#     tax_amount = amount * tax_rate
#     return tax_amount


# def final_price_with_tax(amount, tax_rate=0.1):
#     tax = calculate_tax(amount,tax_rate)
#     if tax is None:
#         return None
#     return amount + tax
    

# print(final_price_with_tax(100,0.15))