# Function 1 - calcaulting usage costs 
def calculate_usage_cost(usage_kwh, rate_per_kwh=0.3):
    if usage_kwh <= 0:
        return None 
    cost_usage = usage_kwh * rate_per_kwh
    return cost_usage 

# Function 2 - fixed charge calculations
def calculate_fixed_charge(days, daily_charge=1.2):
    if days <= 0:
        return None 
    cost_fixed = days * daily_charge
    return cost_fixed

# Function 3 - total bill calculations
def total_bill(usage_kwh, days, rate_per_kwh=0.3, daily_charge=1.2):
    usage = calculate_usage_cost(usage_kwh,rate_per_kwh)
    fixed = calculate_fixed_charge(days, daily_charge)

    if usage is None or fixed is None:
        return None 
    bill_total = usage + fixed
    return bill_total 

print(total_bill(100, 30))
print(total_bill(100, 30, 0.35))
print(total_bill(100, 30, 0.35, 1.50))