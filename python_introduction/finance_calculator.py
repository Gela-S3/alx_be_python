income = int(input("Enter your monthly income : "))
expense = int(input("Enter your monthly expenses : "))
saving = income - expense
Projected_saving = int((saving * 12) + (saving * 12 * 0.05))
print("Your monthly savings are", f"${saving}.")
print("Projected savings after one year, with interest, is :",
      f"${Projected_saving}.")
