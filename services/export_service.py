import csv

class ExportService:
    """Exports transaction history into standard tabular formats."""
    def __init__(self, expense_service):
        self.expense_service = expense_service

    def export_csv(self, filename="expenses_export.csv"):
        expenses = self.expense_service.get_all()
        try:
            with open(filename, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["ID", "Date", "Title", "Category", "Amount"])
                for e in expenses:
                    writer.writerow([e.id, e.date, e.title, e.category, e.amount])
            return True
        except IOError:
            return False