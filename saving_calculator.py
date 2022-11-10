# calculate how much a person can save in a year
# Based on hourly_income,hours_worked,Weekly_cost

# ---- Greetings the user ----
name = input("What is your name? ")

# Add your value here for the calcul
hourly_wage = 20  # add here your own value
weekly_wage = 0  # add here your own value
hours_per_week = 40  # add here your own value
rent_per_month = 845  # add here your own value
dispense_per_week = 0  # add here your own value
saving_per_week = 100  # add here your own value
dispense_per_month = 0  # add here your own value
saving_per_month = 0  # add here your own value
dispense_per_year = 0  # add here your own value
saving_per_year = 0  # add hee your own value
# ---- Calculate Weekly income ----
income_per_week = hourly_wage * hours_per_week

print(name + "'s weekly earning is:")
print(income_per_week, "$")

# ---- Calculate income monthly ----
income_per_month = weekly_wage * 4
income_per_month = income_per_week * 4
print(name + "'s monthly earning is:")
print(income_per_month, "$")
print("Monthly Saving:")
print(saving_per_month)
# ---- Calculate Yearly income ----
income_per_year = income_per_week * 52
print(name + "'s yearly earning is:")
print(income_per_year, "$")

# ---- Calculate money left after the rent + saving_per_week ----
total_left_monthly = income_per_month - rent_per_month - saving_per_week * 4
print(name + "'s monthly money left is:")
print(total_left_monthly, "$")
# ---- Calculate monthly dispense ----
dispense_per_month = dispense_per_week * 4
# print disabled print(name + + "'s monthly dispense is:")
# print disabled print(dispense_per_month, "$")

# ---- Calculate Weekly dispense ----
# Coming soon

# ---- Calculate Yearly dispense ----
dispense_per_year = dispense_per_month * 12
saving_per_year = income_per_year - dispense_per_year
print(name + "'s yearly saving:")
print(saving_per_year, "$")
