from core import FinTrack
from transaction import Transaction
from utils import greetings, delete_user_data

def display_menu():
    print("\n === What do you want to do? ===")
    print("1. Set budget target.")
    print("2. Set savings.")
    print("3. Add transactions.")
    print("4. View transactions.")
    print("5. View expenses analysis.")
    print("6. View income analysis.")
    print("7. View remaining balance.")
    print("8. View total income.")
    print("9. View total expenses.")
    print("10. Delete user data.")
    print("11. Exit.")
    return input("Choose an option (1-11): ")

wallet = FinTrack()

def main():
    greetings(wallet)
    while True:
        choice = display_menu()
        if choice == "1":
            while True:
                try:
                    budget_target = float(input("\nEnter your budget target 🎯: $"))
                    wallet.set_budget(budget_target)
                    wallet.add_alert_option("budget")
                    print("\nBudget target set successfully!\n")
                    break
                except ValueError as e:
                    print(f"⚠️ Invalid input: {e}. Please try again.\n")

        elif choice == "2":
            while True:
                try:
                    set_savings = float(input("\nEnter your savings goal 💰: $"))
                    wallet.set_savings(set_savings)
                    wallet.add_alert_option("savings")
                    print("\nSavings goal set successfully!\n")
                    break
                except ValueError as e:
                    print(f"⚠️ Invalid input: {e}. Please try again.\n")

        elif choice == "3":
            print("\nYou chose to add transactions ➕\n")
            while True:
                try:
                    transaction_amount = float(input("How much money is for this item? $"))
                    if transaction_amount < 0:
                        raise ValueError("Money spent cannot be negative.")
                except ValueError as e:
                    print(f"⚠️ Invalid input: {e}. Please try again.\n")
                    continue
                transaction_name = input("What is the name of this item? ")
                transaction_category = input("What kind of item did you spend on? ")
                transaction_description = input("More details about this transaction: ")
                while True:
                    transaction_type = input("Is it an income or an expense? I(ncome) or e(xpense): ").lower()
                    if transaction_type not in ['i', 'income', 'e', 'expense']:
                        print("⚠️ Invalid input. Please enter 'I(ncome)' or 'e(xpense)'.\n")
                        continue
                    transaction_type = "income" if transaction_type in ['i', 'income'] else "expense"
                    break
                wallet.add_transaction(transaction_amount, transaction_name, transaction_category, transaction_description, transaction_type)

                add_new_transaction_decision = input("\nDo you want to add another transaction? Y(es) or N(o): ").lower()
                if add_new_transaction_decision not in ['y', 'yes']:
                    print("\nYou chose not to add a new transaction.\n")
                    break

        elif choice == "4":
            print("\nYou chose to view the transactions list 📋\n")
            while True:
                print("How do you want to view transactions?")
                print("1. Default (sorted by date - ascending order)")
                print("2. Sorted by ...")
                print("3. Search transactions ...")
                print("4. Enter any other key to cancel\n")
                view_transaction_choice = input("Enter 1, 2, or 3: ")

                if view_transaction_choice == "1":
                    wallet.view_transactions("sort", "date")
                elif view_transaction_choice == "2":
                    while True:
                        print("\n1. Sorted by amount")
                        print("2. Sorted by name")
                        print("3. Sorted by category")
                        print("4. Sorted by date")
                        print("5. Enter any other key to cancel\n")
                        sorted_by_option = input("Enter 1, 2, 3, or 4: ")
                        if sorted_by_option == "1":
                            wallet.view_transactions("sort", "amount")
                        elif sorted_by_option == "2":
                            wallet.view_transactions("sort", "name")
                        elif sorted_by_option == "3":
                            wallet.view_transactions("sort", "category")
                        elif sorted_by_option == "4":
                            wallet.view_transactions("sort", "date")
                        else:
                            break
                        if input("\nView sorted by another option? Y(es) or any other key to exit: ").lower() not in ["y", "yes"]:
                            break
                elif view_transaction_choice == "3":
                    while True:
                        print("\n1. Filter by name")
                        print("2. Filter by category")
                        print("3. Filter by type")
                        print("4. Enter any other key to cancel\n")
                        search_by_option = input("Enter 1, 2, or 3: ")
                        keyword = input("Enter a keyword: ")
                        if search_by_option == "1":
                            wallet.view_transactions("search", {"key": "name", "value": keyword})
                        elif search_by_option == "2":
                            wallet.view_transactions("search", {"key": "category", "value": keyword})
                        elif search_by_option == "3":
                            wallet.view_transactions("search", {"key": "type", "value": keyword})
                        else:
                            break
                        if input("\nSearch by another filter? Y(es) or any other key to exit: ").lower() not in ["y", "yes"]:
                            break
                else:
                    break

        elif choice == "5":
            print("\nHere is your expenses analysis 📈\n")
            print(f"Your total expenses: {wallet.total_expenses}")
            wallet.view_expenses_analysis()

        elif choice == "6":
            print("\nHere is your income analysis 📈\n")
            print(f"Your total income: {wallet.total_income}")
            wallet.view_income_analysis()

        elif choice == "7":
            print("\nYou chose to view the remaining balance:\n")
            wallet.get_remaining_balance()

        elif choice == "8":
            print("\nYou chose to view total income:\n")
            print(f"Total income: ${wallet.get_total_income()}\n")

        elif choice == "9":
            print("\nYou chose to view total expenses:\n")
            print(f"Total expenses: ${wallet.get_total_expenses()}\n")

        elif choice == "10":
            print("You are going to make a very critical decision ⚠️ ⚠️ ⚠️")
            delete_decision = input("Are you sure you want to delete your data? Y(es) or any key to go back ").lower()
            if delete_decision in ["y", "yes"]:
                confirm_name = input("Please confirm your name: ").lower()
                if confirm_name == wallet.get_user_name().lower():
                    if delete_user_data():
                        print(f"\nThank you for using FinTrack. We hope to see you in the future! 👋👋")
                        break
                    else:
                        print("Something went wrong when trying to delete the data. Try again!")
                else:
                    print("Check your name again!")
            continue

        elif choice == "11":
            wallet.save_to_file()
            print("\nThank you for choosing FinTrack. Have a good day! 👋👋\n")
            break

        else:
            print("\n⚠️ Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
