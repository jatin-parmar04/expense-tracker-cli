class Expense:
    """Represents a single expense entity."""
    def __init__(self, expense_id, title, amount, catagory, date_str):
        self.id = expense_id
        self.title = title
        self.amount = round(float(amount), 2)
        self.catagory = catagory.capitalize()
        self.date = date_str

    def to_dict(self):
        return{
            "id": self.id,
            "title": self.title,
            "amount": self.amount,
            "catagory": self.catagory,
            "date": self.date
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["id"], data["title"], data["amount"], data["catagory"], data["date"])