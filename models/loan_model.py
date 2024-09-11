from datetime import datetime, timedelta

class Loan:
    def __init__(self, 
                 loan_name: str, 
                 principal: float, 
                 interest_rate: float,  # Annual interest rate in percentage
                 loan_term: int,  # Loan term in months
                 start_date: datetime, 
                 account: Account):
        self.loan_name = loan_name
        self.principal = principal
        self.interest_rate = interest_rate
        self.loan_term = loan_term
        self.start_date = start_date
        self.account = account
        self.balance = principal  # Initial loan balance is the principal
        self.payments = []  # Track payments made towards the loan

    def calculate_monthly_payment(self):
        """Calculate the fixed monthly payment using the loan amortization formula."""
        monthly_rate = self.interest_rate / 100 / 12
        payment = self.principal * monthly_rate / (1 - (1 + monthly_rate) ** -self.loan_term)
        return round(payment, 2)

    def make_payment(self, amount: float, payment_date: datetime):
        """Apply a payment towards the loan and reduce the balance."""
        self.balance -= amount
        self.payments.append({"amount": amount, "date": payment_date})
        self.account.add_transaction(-amount)  # Deduct payment from linked account

    def calculate_remaining_balance(self):
        """Calculate the remaining balance on the loan after payments."""
        return round(self.balance, 2)

    def get_next_payment_due_date(self):
        """Calculate the next payment due date based on the loan's start date and payments made."""
        last_payment_date = self.start_date if not self.payments else self.payments[-1]["date"]
        return last_payment_date + timedelta(weeks=4)

    def __repr__(self):
        return f"<Loan: {self.loan_name}, Balance: {self.balance}, Interest Rate: {self.interest_rate}%>"