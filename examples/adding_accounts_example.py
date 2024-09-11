# Create accounts
savings_account = Account(name="My Savings", account_type=AccountType.SAVINGS, balance=5000.0)
credit_card = Account(name="Credit Card", account_type=AccountType.CREDIT, balance=-1000.0)

# Add accounts to account manager
account_manager = AccountManager()
account_manager.add_account(savings_account)
account_manager.add_account(credit_card)

# Create a category
food_category = Category(name="Food")

# Add an expense (deducts from account balance)
grocery_expense = Expense(
    amount=150.0,
    category=food_category,
    date=datetime(2024, 9, 2),
    account=savings_account,  # Link to savings account
    description="Groceries"
)

# Add a recurring salary income (adds to account balance)
salary_income = Income(
    amount=3000.0,
    category=Category(name="Salary"),
    date=datetime(2024, 9, 1),
    account=savings_account,  # Link to savings account
    description="Monthly salary",
    is_recurring=True,
    recurring_period=RecurringPeriod.MONTHLY
)

# Check total balance across accounts
total_balance = account_manager.get_total_balance()
print(f"Total Balance Across Accounts: {total_balance}")

# Check transactions for the savings account
savings_transactions = account_manager.get_account_transactions("My Savings")
print(f"Transactions in Savings Account: {savings_transactions}")