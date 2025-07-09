monthly_income = input("Enter your monthly income : ")
monthly_expenses = input("Enter your monthly expenses : ")
Monthly_saving = monthly_income - monthly_expenses
Projected_saving = int((Monthly_saving * 12) + (Monthly_saving * 12 * 0.05))
print("Your monthly savings are", f"${Monthly_saving}.")
print("Projected savings after one year, with interest, is :",
      f"${Projected_saving}.")
