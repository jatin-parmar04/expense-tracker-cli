from datetime import datetime
from models.expense import Expense

class ExpenseService:
    """Handles CRUD operations on expense records."""
    def __init__(self, storage_service):
        self.storage = storage_service
        self.expenses = [Expense.from_dict(item) for item in self.storage.load_records()]

    def add_expense(self, title, amount, category):
        next_id = self.expenses[-1].id + 1 if self.expenses else 1
        date_str = datetime.now().strftime("%Y-%m-%d %H:%M")
        expense = Expense(next_id, title, amount, category, date_str)
        self.expenses.append(expense)
        self.storage.save_records([e.to_dict() for e in self.expenses])
        return expense

    def get_all(self):
        return self.expenses

    def delete_expense(self, expense_id):
        item = next((e for e in self.expenses if e.id == expense_id), None)
        if item:
            self.expenses.remove(item)
            self.storage.save_records([e.to_dict() for e in self.expenses])
            return True
        return False