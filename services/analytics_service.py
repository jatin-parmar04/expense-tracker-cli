class AnalyticsService:
    """Performs aggregations, category breakdowns, and budget validation."""
    def __init__(self, expense_service):
        self.expense_service = expense_service

    def get_total_expenditure(self):
        return sum(e.amount for e in self.expense_service.get_all())

    def get_category_breakdown(self):
        breakdown = {}
        for e in self.expense_service.get_all():
            breakdown[e.category] = breakdown.get(e.category, 0.0) + e.amount
        return breakdown

    def filter_by_category(self, category_name):
        return [e for e in self.expense_service.get_all() if e.category.lower() == category_name.lower()]