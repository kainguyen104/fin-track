from datetime import datetime

class Transaction:
    def __init__(self, amount, name, category, description, type, date=None):
        """Represents a single transaction."""
        self.amount = amount
        self.name = name
        self.category = category
        self.description = description
        if date is None:
            self.date = datetime.now()
        else:
            self.date = date
        self.type = type
        
    def to_json(self):
        return {
            "amount": self.amount,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "date": self.date.isoformat(),
            "type": self.type
        }