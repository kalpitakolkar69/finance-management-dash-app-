class FinancialManager:
    def __init__(self, 
                 expense_manager: ExpenseManager, 
                 income_manager: IncomeManager, 
                 account_manager: AccountManager, 
                 loan_manager: LoanManager, 
                 sip_manager: SIPManager):
        self.expense_manager = expense_manager
        self.income_manager = income_manager
        self.account_manager = account_manager
        self.loan_manager = loan_manager
        self.sip_manager = sip_manager

    def calculate_net_savings(self):
        """Calculate net savings (total income - total expenses) considering loans and SIPs."""
        total_income = self.income_manager.get_total_income()
        total_expense = self.expense_manager.get_total_expense()
        total_loans = self.loan_manager.get_total_outstanding_loans()
        total_investments = self.sip_manager.get_total_investments()
        return total_income - total_expense - total_loans - total_investments

    def calculate_total_expected_returns(self):
        """Calculate the total expected returns from all SIPs."""
        return self.sip_manager.get_total_expected_returns()

    def get_account_balance(self, account_name: str):
        account = self.account_manager.get_account_by_name(account_name)
        if account:
            return account.balance
        return None