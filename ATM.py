"""  Hello I am Imanuel Moiseev, I hope you will like my code :)  """

import time
from colorama import Fore, Style

# Initialize colorama
Fore.GREEN, Fore.RED, Fore.BLUE, Style.RESET_ALL

users = {
    "imanuel": {
        "password": "imaouem",  # password before encryption: imanuel
        "balance": 45000
    },
    "oran": {
        "password": "osao",  # password before encryption: oran
        "balance": 30000
    },
}


def login():
    while True:
        print("1. Login")
        print("2. Register")
        choice = input("Choice: ")

        if choice == "1":
            username = input("Username: ")
            password = input("Password: ")

            if username in users and encode_password(password) == users[username]["password"]:
                return username
            else:
                print("Invalid username or password. Please try again.")

        elif choice == "2":
            new_username = input("Choose a username: ")
            if new_username in users:
                print("Username already exists. Please choose a different username.")
                continue

            while True:
                new_password = input("Choose a password: ")
                if len(new_password) < 8 or new_password.isdigit() or new_password.isalpha():
                    print(Fore.RED + "Weak password detected! Proceeding with a weak password increases the risk of your account being hacked." + Style.RESET_ALL)
                    strength_choice = input("Do you still want to proceed? (Y/N): ")
                    if strength_choice.upper() != "Y":
                        break
                users[new_username] = {
                    "password": encode_password(new_password),
                    "balance": 0
                }
                print(Fore.BLUE + "Registration successful. Please log in." + Style.RESET_ALL)
                break

        else:
            print("Invalid choice. Please try again.")


def withdraw(username):
    while True:
        try:
            amount = float(input("Withdrawal amount: "))
            if amount < 0:
                print(Fore.RED + "Invalid amount. Please enter a not negative value." + Style.RESET_ALL)
            elif amount > users[username]["balance"]:
                print(Fore.RED + "Insufficient funds. Withdrawal cannot be processed." + Style.RESET_ALL)
            else:
                print("Processing your request...")
                time.sleep(2)  # Simulating processing time
                users[username]["balance"] -= amount
                print(Fore.RED + f"Withdrawal of {amount} completed successfully." + Style.RESET_ALL)
                break
        except ValueError:
            print(Fore.RED + "Invalid amount. Please enter a valid number." + Style.RESET_ALL)


def deposit(username):
    while True:
        try:
            amount = float(input("Deposit amount: "))
            if amount <= 0:
                print(Fore.RED + "Invalid amount. Please enter a positive value." + Style.RESET_ALL)
            else:
                print("Processing your request...")
                time.sleep(2)  # Simulating processing time
                users[username]["balance"] += amount
                print(Fore.GREEN + f"Deposit of {amount} completed successfully." + Style.RESET_ALL)
                break
        except ValueError:
            print(Fore.RED + "Invalid amount. Please enter a valid number." + Style.RESET_ALL)


def check_balance(username):
    print("Processing your request...")
    time.sleep(2)  # Simulating processing time
    balance = users[username]["balance"]
    print(f"Your current balance is: {balance}")


def main():
    username = login()
    print(f"Welcome back, {username}!")
    while True:
        print("\nPlease select an option:")
        print("1. Withdraw funds")
        print("2. Deposit funds")
        print("3. Check balance")
        print("4. Logout")

        choice = input("Choice: ")

        if choice == "1":
            print("You have selected 'Withdraw funds'.")
            withdraw(username)
            print("Loading...")
            time.sleep(1)

        elif choice == "2":
            print("You have selected 'Deposit funds'.")
            deposit(username)
            print("Loading...")
            time.sleep(1)

        elif choice == "3":
            print("You have selected 'Check balance'.")
            check_balance(username)
            print("Loading...")
            time.sleep(1)

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


def encode_password(password):
    encoded_password = ""
    for char in password:
        ascii_value = ord(char)
        if ascii_value % 2 == 1:
            encoded_password += char
        else:
            encoded_password += chr(ascii_value + 1)
    return encoded_password


main()
