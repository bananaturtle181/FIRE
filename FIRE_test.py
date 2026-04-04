from FIRE_calc import FIRE_check
from FIRE_calc import update_investments
from FIRE_calc import net_worth

# --- Define inputs using the new dictionaries ---

person = {
    "age": 26,
    "salary": 70000,
    "expenses": 45000,
    "savings": 10000
}

investment_vals = {
    "invested": 40000,
    "yearly contributions": 12000,
    "growth rate": 0.1,
    "property": 90000
}

debts = {
    "hecs balance": 50000,
    "mortgage": 0,
    "mortgage repayment": 0
}

# Starting net worth and FIRE target
net_worth_val = 100000
fire_number = 1000000

# --- Run FIRE_check ---
df = FIRE_check(person, investment_vals, debts, net_worth_val, fire_number)

# --- Inspect output ---
print(df)
print(f"You will hit FIRE at {df['age'].iloc[-1]} years of age")
