class ExpenseManager:
    def __init__(self):
        self.categories = []
        self.expenses = []
        self.budgets = []

    def add_category(self, category: Category):
        self.categories.append(category)

    def add_expense(self, expense: Expense):
        self.expenses.append(expense)
        # Automatically add expense to relevant budget
        for budget in self.budgets:
            if budget.category == expense.category:
                budget.add_expense(expense)

    def add_budget(self, budget: Budget):
        self.budgets.append(budget)

    def get_expenses_by_category(self, category: Category):
        return [exp for exp in self.expenses if exp.category == category]

    def get_total_expense(self):
        return sum(exp.amount for exp in self.expenses)

    def get_budget_status(self):
        return {budget.category.name: budget.is_over_limit() for budget in self.budgets}

    def get_monthly_expenses(self, month: int, year: int):