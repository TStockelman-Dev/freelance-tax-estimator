"""
Create the logic for a calculator that will determine how much money should be
set aside for self-employment taxes. Plans are in place to add calculators for
State and Federal taxes in the future. For now, this calculator's primary function
is to help advise self-employed individuals with an estimate of how much money
they should set aside to pay their self-employment taxes.
"""

gross_income = float(input("What is your income? "))

def self_employment_tax_calculation(gross_income):
    taxable_income = round(gross_income * 0.9235, 2)
    self_employment_tax = round(taxable_income * 0.153, 2)
    remaining_income = gross_income - self_employment_tax
    return self_employment_tax, remaining_income

self_employment_tax, remaining_income = self_employment_tax_calculation(gross_income)

print(f"You should set aside {self_employment_tax} for self-employment taxes")
print(f"After self-employment taxes, you have {remaining_income} remaining.")