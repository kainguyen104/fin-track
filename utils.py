from core import FinTrack
import os

def greetings(wallet:FinTrack):
    if __is_new_user():
        user = __user_info()
        wallet.set_user_name(user[0])
        wallet.set_user_age(user[1])
        print(f"Welcome to FinTrack, {wallet.get_user_name()}!")
        wallet.set_initial_balance()
        wallet.save_to_file()
    else:
        wallet.load_current_user()
        print(f"Welcome back to FinTrack, {wallet.get_user_name()}!")
    
def __user_info():
    while True:
        name = input("Enter your name: ")
        if len(name) == 0:
            print("Name must not be empty. Please enter your name again.\n")
            continue
        while True:
            try:
                age = int(input("Enter your age: "))
                if age <= 0:
                    raise ValueError("Age must be positive.")
            except ValueError as e:
                print(f"{e}\n")
                continue
            return name, age

def __is_new_user():
    return not os.path.exists("final-project-kainguyen104/user_data.json")

def delete_user_data():
    """Deletes the specified file."""
    if os.path.exists("final-project-kainguyen104/user_data.json"):
        os.remove("final-project-kainguyen104/user_data.json")
        print(f"\nUser has been successfully deleted.")
        return True
    else:
        print(f"Failed to delete user.")
        return False
        