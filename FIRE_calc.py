import sys
# import statistics
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

def main():
    #Running currently function to get user inputs (already validated)
    person, debts, test = currently()

    #Running fire_number to see what the goal is
    fire = fire_number(person["expenses"])

    #Adding fire_number to person dict
    person["fire goal"] = fire

    #Running HECS function to calculate repayments
    hecs_repay = HECS(person["salary"])

    #Unpack after tax values 
    after_tax_salary, tax_amount = after_tax(person["salary"])

    #Checking inclusive flag to see if inc_super function needs to be ran. If inclusive, overwrite person with excluding super pay
    if person["including super"]:
        person["net_pay"] = inc_super(person["salary"]) - tax_amount - hecs_repay
    else: person["net_pay"] = after_tax_salary - hecs_repay
    
    #Running investments function to get expected investment returns rate and initial amount invested
    invested, growth_rate, yearly_contributions = investments(test)

    #Storing investment values into dict for input into FIRE_check()
    investment_vals = {"invested": invested,
                       "yearly contributions": yearly_contributions,
                       "growth rate": growth_rate,
                       "property_value": person["property value"]
    }
    #Calculating networth at year 1
    net_worth_val = net_worth(person["savings"], invested, investment_vals["property_value"], debts["hecs balance"], debts["mortgage"])

    #Running Fire_check function to calculate year of retirement
    retirement = FIRE_check(person, investment_vals, debts, net_worth_val, fire)

    #Plotting graphs
    fig_px = px.line(retirement, x = "year", y = "net_worth")
    retirement.plot(x = "year", y = "net_worth")
    fig_px.show()
    plt.show()
    
    return retirement

def currently():
    inclusive = False
    #Prompt user for test mode for debuggng 
    test = input("Do you wish to enter test mode? (y/n)")

    if test == "y":
        age = 26
        salary = 85000
        savings = 67000
        expenses = 60000
        hecs = 40000
        property_value = 0
        other_debts = 0
        mortgage = 800000
        mortgage_repay = 30000

    else:
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

    person = {"age": age,
              "salary": salary,
              "expenses": expenses,
              "savings": savings,
              "property value": property_value,
              "including super": inclusive
    }

    debts = {"hecs balance": hecs,
             "mortgage": mortgage,
             "mortgage repayment": mortgage_repay,
             "other debts": other_debts
    }

    return person, debts, test

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
 
    return salary_post_tax, tax_amount

def inc_super(salary_inc,super_pc=0.115):

    salary_take_home = round(salary_inc / (1 + super_pc))
    
    return salary_take_home

def investments(test):
    if test == "y":
        initial_investment = 44000
        investment_returns = 0.08
        contributions = 12000
    else:
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

def FIRE_check(person, investment_vals, debts, net_worth_val, fire_number):

    #Make copy of input dictionary to avoid changes to inputs
    person_copy = person.copy()
    investment_vals_copy = investment_vals.copy()
    debts_copy = debts.copy()

    #Initialise year, age and savings and results dictionary
    year = 0
    age = person["age"]
    savings = person["savings"]
    salary_growth = (1 + 0.02)
    results = {"age": [person["age"]],
                   "year": [0],
                   "invested_amount": [investment_vals["invested"]],
                   "hecs_remaining": [debts["hecs balance"]],
                   "salary": [person["salary"]],
                   "mortgage_remaining": [debts["mortgage"]],
                   "net_worth": [net_worth_val],
                   "net_income": [person["net_pay"]]
        }
    
    while net_worth_val < fire_number and age < 100:  #Setting up while loop and limiting age to 100 so loop will always end

        #Initialise age and year counters
        age += 1
        year += 1

        #Calling after tax function to get initial tax values
        after_tax_salary, tax_amount = after_tax(person_copy["salary"])

        #Setting up changing results
        invested = update_investments(investment_vals_copy["invested"], investment_vals_copy["yearly contributions"], investment_vals_copy["growth rate"])
        hecs_repayments = HECS(person_copy["salary"])
        hecs_bal = max(0, debts_copy["hecs balance"] - hecs_repayments)
        mortgage = max(0, debts_copy["mortgage"] - debts_copy["mortgage repayment"])
        savings += (person_copy["salary"]
                    - person_copy["expenses"]
                    - investment_vals_copy["yearly contributions"]
                    - hecs_repayments
                    - debts_copy["mortgage repayment"]
                    )
        
        #Updating input dictionaries with newly calculated values
        investment_vals_copy["invested"] = invested  #Update investment amount
        investment_vals_copy["yearly contributions"] *= salary_growth  #Aggregate yearly contributions while updating with salary growth
        debts_copy["hecs balance"] = hecs_bal    #Update hecs balance
        debts_copy["mortgage"] = mortgage    #Update mortgage balance
        

        #Updating salary and net worth
        person_copy["salary"] *= salary_growth       #Adjusting salary based on cost of living adjustment only

        #Updating net pay based on new salary
        if person_copy["including super"]:
            person_copy["net_pay"] = inc_super(person_copy["salary"]) - tax_amount - hecs_repayments
        else: person_copy["net_pay"] = after_tax_salary - hecs_repayments

        #Updating net worth
        net_worth_val = net_worth(savings, invested, investment_vals["property_value"], hecs_bal, mortgage)

        #Storing results into dictionary
        results["age"].append(age)
        results["year"].append(year)
        results["invested_amount"].append(invested)
        results["hecs_remaining"].append(hecs_bal)
        results["salary"].append(person_copy["salary"])
        results["net_income"].append(person_copy["net_pay"])
        results["mortgage_remaining"].append(mortgage)
        results["net_worth"].append(net_worth_val)

    df = pd.DataFrame(results)
    print(f"You will hit FIRE at {df['age'].iloc[-1]} years of age")

    return df

if __name__ == "__main__":
    print(main())
