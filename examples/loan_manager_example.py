# Define an account to link the loan payments
savings_account = Account(name="My Savings", account_type=AccountType.SAVINGS, balance=5000.0)

# Create a loan
home_loan = Loan(
    loan_name="Home Loan",
    principal=200000,  # Loan amount
    interest_rate=5.0,  # 5% annual interest
    loan_term=360,  # 30-year loan (360 months)
    start_date=datetime(2024, 1, 1),
    account=savings_account  # Linked to a savings account
)

# Add loan to LoanManager
loan_manager = LoanManager()
loan_manager.add_loan(home_loan)

# Calculate monthly payment
monthly_payment = home_loan.calculate_monthly_payment()
print(f"Monthly Payment for {home_loan.loan_name}: ${monthly_payment}")

# Make a payment
payment_date = datetime(2024, 2, 1)
home_loan.make_payment(monthly_payment, payment_date)

# Check remaining balance
remaining_balance = home_loan.calculate_remaining_balance()
print(f"Remaining Balance: ${remaining_balance}")

# Get next payment due date
next_payment_due = home_loan.get_next_payment_due_date()
print(f"Next Payment Due: {next_payment_due}")