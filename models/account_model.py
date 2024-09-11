class AccountType(Enum):
    SAVINGS = 'savings'
    CREDIT = 'credit'

class Account:
    def __init__(self, name: str, account_type: AccountType, balance: float = 0.0):
        self.name = name
        self.account_type = account_type
        self.balance = balance
        self.transactions = []  # Track all expenses and incomes linked to this account

    def add_transaction(self, amount: float):
        self.balance += amount
        self.transactions.append(amount)

    def __repr__(self):
        return f"<Account: {self.name} ({self.account_type.value}) - Balance: {self.balance}>"