import sys
# import statistics
import pandas as pd

#Defining main function
def main():

    #Running currently function to get user inputs (already validated)
    inputs, inclusive, mortgage_repay = currently()

    #Running fire_number to see what the goal is
    fire = fire_number(inputs["expenses"])

    #Checking inclusive flag to see if inc_super function needs to be ran
    if inclusive:
        salary = inc_super(inputs["salary"])
    else: salary = inputs["salary"]
    
    #Running HECS function to calculate repayments
    hecs_repay = HECS(salary)

    #Running after-tax function on salary after removing super (if inclusive)
    net_pay = after_tax(salary) - hecs_repay
    
    #Running investments function to get expected investment returns rate and initial amount invested
    invested, growth_rate, yearly_contributions = investments()

    #Setting up the dataframe
    df = pd.DataFrame([{
        key: inputs[key]
        for key in ["age", "savings", "expenses", "hecs", "property", "mortgage", "other_debt"]
    }])
    
    #Preparing unpacked columns not from inputs
    df["net_salary"] = net_pay
    df["fire"] = fire
    df["investments"] = invested
    df["year"] = 1
    df["net_worth"] = net_worth(inputs["savings"],invested ,inputs["property"],inputs["hecs"],inputs["mortgage"])

    #Rearranging df with year as the first column 
    #We first name variable cols and rearrange by prepending age to the start, then loop through other cols if not age 
    cols = ["age"] + [c for c in df.columns if c != "age"]
    df = df[cols]

    #Setting up year 2
    

    return df

def currently():
    inclusive = False
    #Prompt user for their current situation eg. Age, Salary and validating the values
    try:
        age = int(input("How old are you?"))
        salary = int(input("What is your current salary?"))
        savings = int(input("How much do you have in savings?"))
        expenses = int(input("How much is your annual expenses?"))
        hecs = int(input("How much is your HECS? (If you have none, put zero)"))
        property_value = int(input("How much is your property worth? (If you don't have one, put zero)"))
        other_debts = int(input("Do you have any other debts? eg.credit card loans (If none, put zero)"))
        
    except ValueError:
        sys.exit("Inputs need to be integers. Please round to the nearest whole number")

    if age <= 12:
        sys.exit("You're a bit young to be thinking about this no?")
    if savings < 0:
        sys.exit("Savings cannot be negative")
    if salary <= 0:
        sys.exit("Please provide your salary")
    else:
        temp = (input("Is your salary inclusive of super (y/n)")).lower()
        if temp == "y":
            inclusive = True
    if hecs < 0:
        sys.exit("HECS cannot be negative")

    if property_value < 0:
        sys.exit("Property value cannot be negative")
    elif property_value == 0:
        mortgage = 0
        mortgage_repay = 0
    else:
        try:
            mortgage = int(input("How much do you still owe on this property?"))
            mortgage_repay = int(input("How much do you pay for mortgage per year?"))
        except ValueError:
            sys.exit("Please enter a positive integer value")
    if other_debts < 0:
        sys.exit("Other debt cannot be negative")

    inputs = {"age": age, 
              "salary": salary,
              "savings": savings,
              "expenses": expenses,
              "hecs": hecs,
              "property": property_value,
              "mortgage": mortgage, 
              "other_debt":other_debts
    }
    return inputs, inclusive, mortgage_repay

def after_tax(salary):
   
    brackets = [(0, 18200, 0),
                (18201, 45000, 0.16),
                (45001, 135000, 0.3),
                (135001, 190000, 0.37),
                (190001, float("inf"), 0.45)
    ]
    tax_amount = 0
    medicare = 0.02

    for lower, upper, rate in brackets:
        
        if salary > lower:
            tax_amount += (min(salary, upper) - lower) * rate

    salary_post_tax = salary - tax_amount - (salary * medicare)
 
    return salary_post_tax

def inc_super(salary_inc,super_pc=0.115):

    salary_take_home = round(salary_inc / (1 + super_pc))
    
    return salary_take_home

def investments():

    start = input("Do you have any shares/stocks? (y/n)")
    if start == "y":
        try:
            initial_investment = int(input("How much do you have?"))
            contributions = int(input("How much will you contribute to investments annually?"))
        except ValueError:
            sys.exit("Please provide a postive integer")
        if initial_investment <= 0 or contributions < 0:
            sys.exit("Please provide a positive investment amount that's more than 0.")
    else:
        initial_investment = 0

    try:
        investment_returns = float(input(("What investment return rate do you expect? (Please return a decimal value)")))
    except ValueError:
        sys.exit("Please provide a positive decimal value")

    return initial_investment, investment_returns, contributions

def HECS(salary_exc_super):

    if salary_exc_super < 67000:
        hecs_repay = 0
    elif salary_exc_super < 125000:
        hecs_repay = (salary_exc_super - 67000) * 0.15
    elif salary_exc_super < 179285:
        hecs_repay = 8700 + ((salary_exc_super - 125000) * 0.17)
    else:
        hecs_repay = salary_exc_super * 0.1

    return hecs_repay

def fire_number(expenses):
    
    fire = round(expenses * 25)

    return fire

def net_worth(savings, investments, property_value, hecs, mortgage):

    networth = savings + investments + property_value - hecs - mortgage

    return networth

def update_investments(initial, contributions, growth_rate):
    return (initial + contributions) * (1 + growth_rate)

def FIRE_check(net_worth_val, fire_number, age, year, savings, invested, expenses, property_value, yearly_contributions, growth_rate, hecs_balance, salary, mortgage, mortgage_repayment):

    results = {"age": [],
                   "year": [],
                   "invested_amount": [],
                   "hecs_remaining": [],
                   "salary": [],
                   "mortgage_remaining": [],
                   "net_worth": []
        }
    
    while net_worth_val < fire_number and age < 100:
        age += 1
        year += 1
        invested = update_investments(invested, yearly_contributions, growth_rate)
        hecs_repayments = HECS(salary)
        hecs_balance = max(0, hecs_balance - hecs_repayments)
        mortgage = max(0, mortgage - mortgage_repayment)
        savings = savings + salary - expenses - yearly_contributions - hecs_repayments - mortgage_repayment

        #Updating salary and net worth
        salary = salary * (1 + 0.02)        #Adjusting salary based on cost of living adjustment only
        net_worth_val = net_worth(savings, invested, property_value, hecs_balance, mortgage)

        results["age"].append(age)
        results["year"].append(year)
        results["invested_amount"].append(invested)
        results["hecs_remaining"].append(hecs_balance)
        results["salary"].append(salary)
        results["mortgage_remaining"].append(mortgage)
        results["net_worth"].append(net_worth_val)

    df = pd.DataFrame(results)
    # return age, year, invested, hecs_balance, salary, mortgage, net_worth_val
    return df

if __name__ == "__main__":
    print(main())
