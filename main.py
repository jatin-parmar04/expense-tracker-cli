import sys
from services.storage_service import StorageService
from services.expense_service import ExpenseService
from services.analytics_service import AnalyticsService
from services.export_service import ExportService

def display_menu():
    print("\n==========================================")
    print("   PERSONAL EXPENSE TRACKER (MODULAR CLI) ")
    print("==========================================")
    print("1. Add New Expense")
    print("2. View All Expenses")
    print("3. Filter Expenses by Category")
    print("4. Delete Expense by ID")
    print("5. View Analytics & Summary")
    print("6. Export to CSV")
    print("7. Exit")

def main():
    storage = StorageService()
    expense_svc = ExpenseService(storage)
    analytics_svc = AnalyticsService(expense_svc)
    export_svc = ExportService(expense_svc)

    while True:
        display_menu()
        choice = input("Enter choice (1-7): ").strip()

        if choice == "1":
            title = input("Enter description/title: ").strip()
            if not title:
                print("Title cannot be blank.")
                continue
            try:
                amount = float(input("Enter amount (INR): "))
                if amount <= 0:
                    print("Amount must be positive.")
                    continue
            except ValueError:
                print("Invalid amount entered.")
                continue
            cat = input("Enter category (Food, Travel, Books, etc.): ").strip()
            expense_svc.add_expense(title, amount, cat or "General")
            print("Expense recorded successfully.")

        elif choice == "2":
            records = expense_svc.get_all()
            if not records:
                print("No records found.")
                continue
            print(f"\n{'ID':<5} | {'Date':<17} | {'Category':<15} | {'Amount':<10} | {'Title'}")
            print("-" * 65)
            for r in records:
                print(f"{r.id:<5} | {r.date:<17} | {r.category:<15} | {r.amount:<10.2f} | {r.title}")

        elif choice == "3":
            cat = input("Enter category to filter: ").strip()
            results = analytics_svc.filter_by_category(cat)
            if not results:
                print(f"No records found for category '{cat}'.")
                continue
            print(f"\n{'ID':<5} | {'Date':<17} | {'Amount':<10} | {'Title'}")
            print("-" * 50)
            for r in results:
                print(f"{r.id:<5} | {r.date:<17} | {r.amount:<10.2f} | {r.title}")

        elif choice == "4":
            try:
                del_id = int(input("Enter expense ID to delete: "))
                if expense_svc.delete_expense(del_id):
                    print("Record removed successfully.")
                else:
                    print("ID not found.")
            except ValueError:
                print("Please enter a valid numeric ID.")

        elif choice == "5":
            total = analytics_svc.get_total_expenditure()
            breakdown = analytics_svc.get_category_breakdown()
            print(f"\nTotal Expenditure: INR {total:.2f}\n")
            print(f"{'Category':<18} | {'Spent (INR)':<12} | {'Share'}")
            print("-" * 45)
            for c, amt in breakdown.items():
                pct = (amt / total * 100) if total > 0 else 0
                print(f"{c:<18} | {amt:<12.2f} | {pct:.1f}%")

        elif choice == "6":
            if export_svc.export_csv():
                print("Data exported successfully to expenses_export.csv")
            else:
                print("Export failed.")

        elif choice == "7":
            print("Exiting application. Goodbye.")
            sys.exit(0)
        else:
            print("Invalid selection. Choose between 1 and 7.")

if __name__ == "__main__":
    main()