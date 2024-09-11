from enum import Enum
from datetime import datetime, timedelta

# Enum for Recurring Period
class RecurringPeriod(Enum):
    DAILY = 'daily'
    WEEKLY = 'weekly'
    MONTHLY = 'monthly'
    YEARLY = 'yearly'

class Expense:
    def __init__(self, 
                 amount: float, 
                 category: Category, 
                 date: datetime,
                 account: Account,
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
        
    self.account.add_transaction(-self.amount)

    def __repr__(self):
        return f"<Expense: {self.amount} in {self.category.name} on {self.date.strftime('%Y-%m-%d')} (Account: {self.account.name})>"

    def get_next_due_date(self):
        """Calculate the next due date if the expense is recurring"""
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