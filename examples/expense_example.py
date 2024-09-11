# Define a category
food_category = Category(name="Food")

# Create a recurring monthly expense
rent_expense = Expense(
    amount=1000.0,
    category=food_category,
    date=datetime(2024, 9, 1),  # Example date
    description="Monthly rent",
    is_recurring=True,
    recurring_period=RecurringPeriod.MONTHLY
)

# Check the next due date for the rent expense
next_rent_due_date = rent_expense.get_next_due_date()
print(f"Next rent payment is due on: {next_rent_due_date}")