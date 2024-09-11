class Budget:
    def __init__(self, category: Category, monthly_limit: float):
        self.category = category
        self.monthly_limit = monthly_limit
        self.expenses = []  # List of expenses tied to this budget

    def add_expense(self, expense: Expense):
        if expense.category == self.category:
            self.expenses.append(expense)

    def calculate_total_expense(self):
        return sum(exp.amount for exp in self.expenses)

    def is_over_limit(self):
        return self.calculate_total_expense() > self.monthly_limit

    def __repr__(self):
        return f"<Budget: {self.monthly_limit} for {self.category.name}>"
        
