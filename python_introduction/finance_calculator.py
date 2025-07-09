income = input("Enter your monthly income : ")
expense = input("Enter your monthly expenses : ")
Monthly_saving = income - expense
Projected_saving = int((Monthly_saving * 12) + (Monthly_saving * 12 * 0.05))
print("Your monthly savings are", f"${Monthly_saving}.")
print("Projected savings after one year, with interest, is :",
      f"${Projected_saving}.")
