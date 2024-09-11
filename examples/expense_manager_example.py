expense_manager = ExpenseManager()

# Add a recurring monthly rent expense
expense_manager.add_expense(rent_expense)

# Get upcoming recurring expenses within the next 30 days
upcoming_expenses = expense_manager.get_upcoming_recurring_expenses(future_days=30)
for exp in upcoming_expenses:
    print(f"Upcoming recurring expense: {exp.description} on {exp.get_next_due_date()}")