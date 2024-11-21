from datetime import datetime

class Transaction:
    def __init__(self, amount, category, description):
        """Represents a single transaction."""
        self.amount = amount
        self.category = category
        self.description = description
        self.date = datetime.now()

class FinTrack:
    def __init__(self):
        """Initializes a financial tracker with an empty list of transactions."""
        self.transactions = []

    def add_transaction(self, amount, category, description):
        """Add a new transaction (income or expense)."""
        transaction = Transaction(amount, category, description)
        self.transactions.append(transaction)

    def view_transactions(self):
        """Print all transactions."""
        for i in self.transactions:
            print(f"{i.date} | {i.category} | {i.amount} | {i.description}")

    def calculate_balance(self):
        """Return the total balance."""
        total = 0
        for i in self.transactions:
                total += i.amount
        return total

    def calculate_expenses(self):
        """Return the total expenses (negative amounts)."""
        total = 0
        for i in self.transactions:
            if i.amount < 0:
                total += i.amount
        return total

    def calculate_income(self):
        """Return the total income (positive amounts)."""
        total = 0
        for i in self.transactions:
            if i.amount > 0:
                total += i.amount
        return total