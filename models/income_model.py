from datetime import datetime

class Income:
    def __init__(self, 
                 amount: float, 
                 category: Category, 
                 date: datetime,
                 account: Account
                 description: str = '', 
                 is_recurring: bool = False, 
                 recurring_period: RecurringPeriod = None):
        self.amount = amount
        self.category = category
        self.date = date
        self.account = account
        self.description = description
        self.is_recurring = is_recurring
        self.recurring_period = recurring_period
        
    self.account.add_transaction(self.amount)

    def __repr__(self):
      return f"<Income: {self.amount} from {self.category.name} on {self.date.strftime('%Y-%m-%d')} (Account: {self.account.name})>"

    def get_next_income_date(self):
        """Calculate the next due date if the income is recurring"""
        if not self.is_recurring or not self.recurring_period:
            return None
        
        if self.recurring_period == RecurringPeriod.DAILY:
            return self.date + timedelta(days=1)
        elif self.recurring_period == RecurringPeriod.WEEKLY:
            return self.date + timedelta(weeks=1)
        elif self.recurring_period == RecurringPeriod.MONTHLY:
            return self.date.replace(month=self.date.month % 12 + 1)
        elif self.recurring_period == RecurringPeriod.YEARLY:
            return self.date.replace(year=self.date.year + 1)
        return None