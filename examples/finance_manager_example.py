# Assuming you have already added incomes and expenses
financial_manager = FinancialManager(expense_manager, income_manager)

# Calculate net savings
net_savings = financial_manager.calculate_net_savings()
print(f"Net Savings: {net_savings}")