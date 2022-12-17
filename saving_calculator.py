# calculate how much a person can save in a year
# Based on hourly_income,hours_worked,Weekly_cost

# program version
Version = "0.0.0.3"

# ---- Greetings the user ----
print("Welcome on this saving calculator.")
print("Version: " + Version)
name = input("What is your name? ")

# Add your value here for the calcul
hourly_wage = 0  # add here your own value
weekly_wage = 0  # add here your own value
hours_per_week = 0  # add here your own value
dispense_per_week = 0  # add here your own value
saving_per_week = 0  # add here your own value
dispense_per_month = 0  # add here your own value
saving_per_month = 0  # add here your own value
dispense_per_year = 0  # add here your own value
saving_per_year = 0  # add here your own value
Tax_Income = 0 # let this to 0 by default ( Not fixed )

# add overtime ( Working )
if hours_per_week in range(40,60):  # Overtime ( Time and half  only )
    hourly_wage *= 1.5
elif hours_per_week >= 60: # Overtime Double time
    hourly_wage *= 2.0

# Add salary info
print("Salary: ", hourly_wage, "$")

# ---- Calculate Weekly income ----
income_per_week = hourly_wage * hours_per_week

print(name + "'s weekly earning is:")
print(income_per_week, "$")

# ---- Calculate income monthly ----
income_per_month = weekly_wage,income_per_week * 4
# print(name + "'s monthly earning is:")
# print(income_per_month, "$")

# ---- Calculate monthly dispense ----
dispense_per_month = dispense_per_week * 4
# print disabled print(name + + "'s monthly dispense is:")
# print disabled print(dispense_per_month, "$")

# ---- Calculate Yearly income ----
income_per_year = income_per_week * 52
print(name + "'s yearly earning is:")
print(income_per_year, "$")

# ---- Calculate Yearly dispense ----
dispense_per_year = dispense_per_month * 12
print(name + "'s yearly dispense is:")
print(dispense_per_year)

# ---- Calculate Yearly Savings ----
saving_per_year = income_per_year - dispense_per_year
print(name + "'s yearly saving:")
print(saving_per_year, "$")

# Next Update: Income Tax ( 15% = 2022 income Tax )
# Next update: Coming Soon
