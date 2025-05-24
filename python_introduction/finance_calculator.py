monthlyIncome = int(input("Enter your monthly income: "))

monthlyExpense = int(input("Enter your total monthly expenses: "))

monthlySaving = monthlyIncome - monthlyExpense

print(f"Your monthly savings are ${monthlySaving}.")

print(f"Projected savings after one year, with interest, is: ${monthlySaving * 12 + (monthlySaving * 12 * 0.05)}.")
