monthly_income = input("Enter your monthly income : ")
monthly_expenses = input("Enter your monthly expenses : ")
monthly_savings = monthly_income - monthly_expenses
Projected_saving = float((monthly_savings * 12)) + float((monthly_savings * 12 * 0.05))
print("Your monthly savings are", f"${monthly_savings}.")
print("Projected savings after one year, with interest, is :",
      f"${Projected_saving}.")
