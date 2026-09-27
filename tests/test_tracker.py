import unittest
import os
from models.expense import Expense
from services.storage_service import StorageService
from services.expense_service import ExpenseService
from services.analytics_service import AnalyticsService

class TestExpenseTracker(unittest.TestCase):
    def setUp(self):
        self.test_file = "data/test_expenses.json"
        self.storage = StorageService(self.test_file)
        self.service = ExpenseService(self.storage)
        self.service.expenses = []

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_add_expense(self):
        item = self.service.add_expense("Books", 450.0, "Education")
        self.assertEqual(len(self.service.get_all()), 1)
        self.assertEqual(item.title, "Books")

    def test_analytics_calculation(self):
        self.service.add_expense("Meal", 200.0, "Food")
        self.service.add_expense("Coffee", 100.0, "Food")
        analytics = AnalyticsService(self.service)
        self.assertEqual(analytics.get_total_expenditure(), 300.0)

if __name__ == "__main__":
    unittest.main()