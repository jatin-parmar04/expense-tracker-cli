import json
import os

class StorageService:
    """Handles persistent data read and write operations."""
    def __init__(self, filepath="data/expenses.json"):
        self.filepath = filepath
        os.makedirs(os.path.dirname(self.filepath), exist_ok=True)

    def load_records(self):
        if not os.path.exists(self.filepath):
            return []
        try:
            with open(self.filepath, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return []

    def save_records(self, records):
        try:
            with open(self.filepath, "w", encoding="utf-8") as f:
                json.dump(records, f, indent=4)
            return True
        except IOError:
            return False