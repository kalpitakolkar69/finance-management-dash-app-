class IncomeManager:
    def __init__(self):
        self.categories = []
        self.incomes = []

    def add_category(self, category: Category):
        self.categories.append(category)

    def add_income(self, income: Income):
        self.incomes.append(income)

    def get_total_income(self):
        """Calculate total income"""
        return sum(inc.amount for inc in self.incomes)

    def get_income_by_category(self, category: Category):
        """Retrieve income entries for a specific category"""
        return [inc for inc in self.incomes if inc.category == category]

    def get_upcoming_recurring_income(self, future_days: int):
        """Get a list of recurring income due in the next `future_days` days"""
        upcoming_incomes = []
        current_date = datetime.now()
        for inc in self.incomes:
            if inc.is_recurring:
                next_income_date = inc.get_next_income_date()
                if next_income_date and (current_date <= next_income_date <= current_date + timedelta(days=future_days)):
                    upcoming_incomes.append(inc)
        return upcoming_incomes