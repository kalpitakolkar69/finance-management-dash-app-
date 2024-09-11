class SIPType(Enum):
    MUTUAL_FUND = 'mutual_fund'
    STOCK = 'stock'
    ETF = 'etf'
    OTHER = 'other'

class SIP:
    def __init__(self, 
                 sip_name: str, 
                 investment_amount: float, 
                 sip_type: SIPType,  # Type of investment (e.g., mutual fund, stock)
                 start_date: datetime, 
                 frequency: RecurringPeriod,  # SIP frequency (e.g., monthly)
                 account: Account,  # Linked account for the SIP
                 expected_return_rate: float):  # Expected annual return rate in percentage
        self.sip_name = sip_name
        self.investment_amount = investment_amount
        self.sip_type = sip_type
        self.start_date = start_date
        self.frequency = frequency
        self.account = account
        self.expected_return_rate = expected_return_rate
        self.investments = []  # Track all payments made towards the SIP

    def make_investment(self, investment_date: datetime):
        """Make a recurring investment towards the SIP."""
        self.investments.append({"amount": self.investment_amount, "date": investment_date})
        self.account.add_transaction(-self.investment_amount)  # Deduct from the linked account

    def calculate_expected_returns(self):
        """Calculate the expected returns based on the investments made."""
        total_invested = sum(investment["amount"] for investment in self.investments)
        annual_return = total_invested * (self.expected_return_rate / 100)
        return round(annual_return, 2)

    def get_next_investment_date(self):
        """Calculate the next due date for the SIP investment."""
        last_investment_date = self.start_date if not self.investments else self.investments[-1]["date"]
        if self.frequency == RecurringPeriod.MONTHLY:
            next_date = last_investment_date.replace(month=last_investment_date.month % 12 + 1)
        elif self.frequency == RecurringPeriod.WEEKLY:
            next_date = last_investment_date + timedelta(weeks=1)
        elif self.frequency == RecurringPeriod.YEARLY:
            next_date = last_investment_date.replace(year=last_investment_date.year + 1)
        else:
            next_date = None
        return next_date

    def __repr__(self):
        return f"<SIP: {self.sip_name}, Investment Amount: {self.investment_amount}, Expected Returns: {self.calculate_expected_returns()}>"