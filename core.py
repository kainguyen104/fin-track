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
        self.initial_balance = 0
        self.budget = 0
        self.savings = 0

    def set_initial_balance(self):
        """Prompt the user to input an initial balance."""
        while True:
            try:
                balance = float(input("Enter your initial balance👛: $"))
                if balance < 0:
                    raise ValueError("❗Initial balance cannot be negative.")
                self.initial_balance = balance
                print(f"Initial balance set to👛: ${self.initial_balance}")
                break
            except ValueError as e:
                print(f"⚠ Invalid input: {e}. Please try again.")

    def set_budget(self, budget):
        if (budget + self.savings) > self.initial_balance:
            raise ValueError(f"Savings is ${self.savings},and balance is ${self.initial_balance}, so budget must be lower than/ equal to {self.initial_balance - self.budget}")
        if budget > self.initial_balance:
            raise ValueError("❗Budget must be lower than your balance.")
        if budget < 0:
            raise ValueError("❗Budget must be positive.")
        if self.budget != 0:
            print(f"Current budget is set to ${self.budget}. Do you want to set a new budget? ")
            new_budget_decision = input("Y(es) or n(o)? ")
            if new_budget_decision.lower() == "n" or new_budget_decision.lower() == "no":
                print("Keeping old budget.")
                return
        self.budget = budget
        print(f"🔃 Setting budget to ${budget}")
        return budget

    def set_savings(self, savings):
        if (savings + self.budget) > self.initial_balance:
            raise ValueError(f"❗Budget is ${self.budget},and balance is ${self.initial_balance}, so savings must be lower than/ equal to {self.initial_balance - self.budget}")
        if savings < 0: 
            raise ValueError("❗Savings must be positive.")
        if self.savings != 0: 
            print(f"Current savings is set to ${self.savings}. Do you want to set a new savings? ")
            new_savings_decision = input("Y(es) or n(o)? ")
            if new_savings_decision.lower() == "n" or new_savings_decision.lower() == "no":
                print("Keeping old savings.")
                return
        self.savings = savings
        print(f"🔃 Setting savings to ${savings}")
        return savings
    
    def add_transaction(self, amount, category, description):
        """Add a new transaction (income or expense)."""
        transaction = Transaction(amount, category, description)
        self.transactions.append(transaction)

    def view_transactions(self):
        """Print all transactions."""
        for i in self.transactions:
            print(f"{i.date} | {i.category} | {i.amount} | {i.description}")

    def view_expenses_analysis(self):
        
        return #tinh % by category
    
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
    
    def alert_near_budget(self):
        return
    
    def alert_near_savings(self):
        return