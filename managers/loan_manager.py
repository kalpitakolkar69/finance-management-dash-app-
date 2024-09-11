class LoanManager:
    def __init__(self):
        self.loans = []

    def add_loan(self, loan: Loan):
        self.loans.append(loan)

    def get_loan_by_name(self, loan_name: str):
        for loan in self.loans:
            if loan.loan_name == loan_name:
                return loan
        return None

    def get_total_outstanding_loans(self):
        """Get the total outstanding loan balance across all loans."""
        return sum(loan.calculate_remaining_balance() for loan in self.loans)

    def get_loan_payments(self, loan_name: str):
        """Get all payments made towards a specific loan."""
        loan = self.get_loan_by_name(loan_name)
        if loan:
            return loan.payments
        return []

    def get_next_payment_due_for_loan(self, loan_name: str):
        """Get the next payment due date for a specific loan."""
        loan = self.get_loan_by_name(loan_name)
        if loan:
            return loan.get_next_payment_due_date()
        return None