class AccountManager:
    def __init__(self):
        self.accounts = []

    def add_account(self, account: Account):
        self.accounts.append(account)

    def get_account_by_name(self, name: str):
        for account in self.accounts:
            if account.name == name:
                return account
        return None

    def get_total_balance(self):
        """Calculate the total balance across all accounts"""
        return sum(acc.balance for acc in self.accounts)

    def get_account_transactions(self, account_name: str):
        """Retrieve all transactions for a specific account"""
        account = self.get_account_by_name(account_name)
        if account:
            return account.transactions
        return []