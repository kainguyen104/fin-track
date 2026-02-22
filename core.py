from transaction import Transaction
from datetime import datetime
import json
import os


class FinTrack:
    def __init__(self):
        """Initializes a financial tracker with an empty list of transactions."""
        self.name = ""
        self.age = 0
        self.transactions = []
        self.balance = 0
        self.budget = 0
        self.savings = 0
        self.total_expenses = 0
        self.total_income = 0
        self.budget_alert_point = 0
        self.alert_options = []
        self.expenses_by_category = {}
        self.income_by_category = {}
    
    def set_user_name(self, name):
        self.name = name
    
    def set_user_age(self,age):
        self.age = age

    def get_user_name(self):
        return self.name

    def set_initial_balance(self):
        """Prompt the user to input an initial balance."""
        while True:
            try:
                balance = float(input("Enter your initial balance👛: $"))
                if balance < 0:
                    raise ValueError("❗Balance cannot be negative.")
                self.balance = balance
                print(f"Balance set to👛: ${self.balance}")
                break
            except ValueError as e:
                print(f"⚠️ Invalid input: {e}. Please try again.")

    def set_budget(self, budget):
        """Set the user's budget with checks."""
        if budget > self.balance:
            raise ValueError(f"❗Budget must be lower than your balance. Remaining balance: ${self.balance}.")
        if (budget + self.savings) > self.balance:
            raise ValueError(f"Savings is ${self.savings}, and balance is ${self.balance}, so budget must be lower than or equal to {self.balance - self.savings}")
        if budget < 0:
            raise ValueError("❗Budget must be positive.")
        if self.budget != 0:
            print(f"Current budget is set to ${self.budget}. Do you want to set a new budget?")
            while True:
                new_budget_decision = input("Y(es) or n(o)? ").lower()
                if new_budget_decision in ["n", "no"]:
                    print("Keeping old budget.")
                    return
                elif new_budget_decision in ["y", "yes"]:
                    break
                else:
                    print("⚠️ Invalid input. Please enter 'Y(es)' or 'n(o)'.")
        self.budget = budget
        self.budget_alert_point = budget / 2
        print(f"🔃 Setting budget to ${budget}")
        return budget

    def set_savings(self, savings):
        """Set the user's savings with checks."""
        if savings < 0:
            raise ValueError("❗Savings must be positive.")
        if self.savings != 0:
            print(f"Current savings is set to ${self.savings}. Do you want to set a new savings?")
            while True:
                new_savings_decision = input("Y(es) or n(o)? ").lower()
                if new_savings_decision in ["n", "no"]:
                    print("Keeping old savings.")
                    return
                elif new_savings_decision in ["y", "yes"]:
                    break
                else:
                    print("⚠️ Invalid input. Please enter 'Y(es)' or 'n(o)'.")
        self.savings = savings
        print(f"🔃 Setting savings to ${savings}")
        return savings
    
    def add_transaction(self, amount, name, category, description, type):
        """Add a new transaction (income or expense)."""
        transaction = Transaction(amount, name, category, description, type)
        self.transactions.append(transaction)
        if type in ['e', 'expense']:
            self.total_expenses += amount
            self.balance -= amount
        if type in ['i', 'income']:
            self.total_income += amount
            self.balance += amount
        if "budget" in self.alert_options:   
            self.alert_near_budget()
        if "savings" in self.alert_options:
            self.alert_near_savings(type)
        self.alert_low_balance()
    
    def __build_transactions_list(self, transactions, choice, argument):
        """Build a list of transactions based on choice and argument."""
        if choice == "sort":
            if argument in ["date", "name", "amount", "category"]:
                # Sort by the argument key
                return sorted(
                    transactions,
                    key=lambda t: getattr(t, argument)
                )
            else:
                raise ValueError("Invalid sort argument. Use 'date', 'name', 'amount', or 'category'.")

        elif choice == "search":
            if argument["key"] in ["name", "category", "type"]:
                key = argument["key"]
                value = argument["value"]
                if key == "type":
                    # Exact match for type
                    return [t for t in transactions if t.type == value]
                else:
                    # Partial match for name or category
                    return [t for t in transactions if value.lower() in getattr(t, key).lower()]
            else:
                raise ValueError("Invalid search argument. Use 'name', 'category', or 'type'.")

        else:
            raise ValueError("Invalid choice. Use 'sort' or 'search'.")

    def view_transactions(self, choice, argument):
        """Print all transactions."""
        result_transactions = self.__build_transactions_list(self.transactions, choice, argument)

        print("Transactions Overview".center(100, "="))
        print(f"{'Date':<20} {'Name':<22} {'Category':<22} {'Amount':<20} {'Type':<20}")
        print("-" * 100)     
        for transaction in result_transactions:
            formatted_transaction_time = transaction.date.strftime("%Y-%m-%d %H:%M:%S")
            print(f"{formatted_transaction_time} | {transaction.name:<20} | {transaction.category:<20} | ${transaction.amount:<17} | {transaction.type:20}\n") 
        print("=" * 100)

    def view_expenses_analysis(self):
        """Analyze and display expenses by category."""
        self.total_expenses = 0

        for transaction in self.transactions:
            if transaction.type.lower() == "expense":
                self.total_expenses += transaction.amount
                if transaction.category in self.expenses_by_category:
                    self.expenses_by_category[transaction.category] += transaction.amount
                else:
                    self.expenses_by_category[transaction.category] = transaction.amount

        print("Expenses Analysis".center(50, "="))
        print(f"{'Category':<20} {'Amount':<15} {'Percentage':<10}")
        print("-" * 50)

        for category in self.expenses_by_category:
            amount = self.expenses_by_category[category]
            percentage = (amount / self.total_expenses) * 100
            print(f"{category:<20} ${amount:<14.2f} {percentage:<9.2f}%")

    def view_income_analysis(self):
        """Analyze and display income by category."""
        self.total_income = 0

        for transaction in self.transactions:
            if transaction.type.lower() == "income":
                self.total_income += transaction.amount
                if transaction.category in self.income_by_category:
                    self.income_by_category[transaction.category] += transaction.amount
                else:
                    self.income_by_category[transaction.category] = transaction.amount

        print("Income Analysis".center(50, "="))
        print(f"{'Category':<20} {'Amount':<15} {'Percentage':<10}")
        print("-" * 50)

        for category in self.income_by_category:
            amount = self.income_by_category[category]
            percentage = (amount / self.total_income) * 100
            print(f"{category:<20} ${amount:<14.2f} {percentage:<9.2f}%")

    def calculate_balance(self):
        """Return the total balance."""
        return self.balance

    def get_total_expenses(self):
        """Return the total expenses (negative amounts)."""
        return self.total_expenses
            
    def get_total_income(self):
        """Return the total income (positive amounts)."""
        return self.total_income

    def get_remaining_balance(self):
        print(f"Remaining balance: ${self.balance}")
        
    def alert_near_budget(self):
        if self.total_expenses > self.budget_alert_point:
            print(f"🚨 Exceeding budget target! Over by ${(self.total_expenses - self.budget_alert_point):.2f}.")
        else:
            print(f"💡 You are ${(self.budget_alert_point - self.total_expenses):.2f} away from reaching the budget target.")

    def alert_low_balance(self):
        if self.balance <= 0: 
            print(f"Alert! Low remaining balance: ${self.balance}")

    def alert_near_savings(self, transaction_type):
        if transaction_type == "income":
            if self.balance >= self.savings:
                print(f"🎯 Savings goal reached! Current balance: ${self.balance:.2f}. Savings goal: ${self.savings:.2f}")
            else:
                print(f"💰 Keep going! You are ${(self.savings - self.balance):.2f} away from reaching your savings goal of ${self.savings:.2f}.")

        elif transaction_type == "expense":
            if self.balance <= self.savings:
                print(f"⚠️ Remaining balance has fallen below the savings goal. Current balance: ${self.balance:.2f}. Savings goal: ${self.savings:.2f}")
            else:
                print(f"💸 Spending recorded. Current balance: ${self.balance:.2f}. Savings goal: ${self.savings:.2f}")


    def add_alert_option(self, option):
        self.alert_options.append(option)
    

    def save_to_file(self):
        """Save data to JSON file."""
        data = {
            'name': self.name,
            'age': self.age,
            'transactions': [transaction.to_json() for transaction in self.transactions],
            'balance': self.balance,
            'budget': self.budget,
            'savings': self.savings,
            'total_expenses': self.total_expenses,
            'total_income': self.total_income,
            'budget_alert_point': self.budget_alert_point,
            'alert_options': self.alert_options,
            'expenses_by_category': self.expenses_by_category,
            'income_by_category': self.income_by_category,
        }  

        with open("user_data.json", 'w') as f:
            json.dump(data, f, indent=4)
    
    def load_current_user(self):
        """Load entries from a JSON file"""

        try:
            with open("user_data.json", 'r') as f:
                d = json.load(f)
        
            self.transactions = [Transaction(t["amount"], t["name"], t["category"], t["description"], t["type"], datetime.fromisoformat(t["date"])) for t in d["transactions"]]
            self.balance = d["balance"]
            self.budget = d["budget"]
            self.savings = d["savings"]
            self.total_expenses = d["total_expenses"]
            self.total_income = d["total_income"]
            self.budget_alert_point = d["budget_alert_point"]
            self.alert_options = d["alert_options"]
            self.expenses_by_category = d["expenses_by_category"]
            self.income_by_category = d["income_by_category"]
            self.name = d["name"]
            self.age = d["age"]

        except FileNotFoundError:
            print(f"File not found.")
