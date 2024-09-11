# Define a category for salary income
salary_category = Category(name="Salary")

# Create a recurring monthly salary income
salary_income = Income(
    amount=3000.0,
    category=salary_category,
    date=datetime(2024, 9, 1),  # Example date
    description="Monthly salary",
    is_recurring=True,
    recurring_period=RecurringPeriod.MONTHLY
)

# Add this income to the IncomeManager
income_manager = IncomeManager()
income_manager.add_income(salary_income)

# Check total income
total_income = income_manager.get_total_income()
print(f"Total Income: {total_income}")

# Check upcoming recurring income
upcoming_incomes = income_manager.get_upcoming_recurring_income(future_days=30)
for inc in upcoming_incomes:
    print(f"Upcoming recurring income: {inc.description} on {inc.get_next_income_date()}")