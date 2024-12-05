from core import Transaction, FinTrack

def display_menu():
    print("\n === What you want to do ===")
    print("1. Set budget target")
    print("2. Set savings")
    print("3. Add transactions")
    print("4. View transactions")
    print("5. View expenses analysis")
    print("6. Exit")
    return input("Choose an option (1-6): ")
def user_info():
    while True:
        name = input("Enter your name: ")
        if len(name) == 0:
            print("Name must not be empty. Please enter your name again.")
            continue
        while True:
            try:
                age = int(input("Enter your age: "))
                if age <= 0:
                    raise ValueError("Age must be positive.")
            except ValueError as e:
                print(e)
                continue
            return name, age

wallet = FinTrack()

def main():
    print("Welcome to FinTrack !")
    # user = user_info()
    wallet.set_initial_balance()
    while True:
        choice = display_menu()
        if choice == "1":
            while True:
                try:
                    budget_target = float(input("Enter your budget target🎯: $"))
                    wallet.set_budget(budget_target)
                    break
                except ValueError as e:
                    print(f"⚠ Invalid input: {e}. Please try again.")
           
        elif choice == "2":
            while True:
                try:
                    set_savings = float(input("Enter your savings goal💰: $"))
                    wallet.set_savings(set_savings)
                    break
                except ValueError as e:
                    print(f"⚠ Invalid input: {e}. Please try again.")
        
        elif choice == "3":
            print("You chose adding transitions.")
            transaction_category = input("What's kind of item you spend on? ")
            transaction_amount = int(input("How much money you spend on this item"))
            add_transactions = input("Add you transactions➕: ")
            return add_transactions
        
        elif choice == "4":
            for i in add_transactions:
                print(f"\n  Here are your transactions list📋 \n {i}")
        
        elif choice == "5":
            print(f"\n Here is your expenses analysis📈 \n")

        elif choice == "6":
            print(f"Thank you for choosing FinTrack. Have a good day!👋👋")
            break
        
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()