# ATM terminal Python program

# code logic:

# 1. customers should be able to create ATM pins 
#     the pins should be of 4 digits and digits only
# 2. customers should be able to login only with their created pin and nothing else 

# 3. customers should be able to: 

#     * see their balances
#     * withdraw
#     * deposit
#     *exit

# 4. we should use functions to make our code more readable
def create_pin():
    while True:
        print("*******************************")
        pin = input("Create a 4-digit PIN: ")
        print("*******************************")
        #@dev python doesn't support ||
        if pin.isdigit() and len(pin) == 4:
            print("*******************************")
            print("PIN successfully created!")
            print("*******************************")
            return pin
        print("*******************************")
        print("Invalid PIN; enter exactly 4 digits.")
        print("*******************************")

def login(pin):
    password_inputing_chances = 3
    while password_inputing_chances != 0:
        print("*******************************")
        entered_pin = input("Enter your 4-digit PIN: ")
        print("*******************************")
        if entered_pin == pin:
            print("Login successful!")
            return True
        # upon every attempt, there is one reduction
        password_inputing_chances -= 1
        print(f"{password_inputing_chances} attempts left")
    print("Account locked due to too many failed attempts.")
    return False

def show_user_balance(balance):
    print(f"Your balance is ${balance}")

def deposit():
    amount = float(input("Input the amount you want to deposit: $"))
    if amount <= 0:
        print("No, you can't deposit an insignificant amount.")
        return 0
    return amount

def withdraw_money(balance):
    amount = float(input("Enter the amount of money you want to withdraw: $"))
    if amount > balance:
        print("You don't have sufficient funds for this.")
        return 0
    elif amount <= 0:
        print("You can only withdraw more than $0.")
        return 0
    return amount

def main():
    print("Welcome to Jubilee Bank!")
    pin = create_pin()

    if not login(pin):
        return

    balance = 0
    customer_engagement_is_running = True 

    while customer_engagement_is_running:
        print("\n****************************")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("****************************")

        choice = input("Please enter your choice between 1 and 4: ")

        if choice == "1":
            show_user_balance(balance)
        elif choice == "2":
            balance += deposit()
            print("Deposit successful.")
        elif choice == "3":
            balance -= withdraw_money(balance)
            print("Withdrawal successful.")
        elif choice == "4":
            customer_engagement_is_running = False
        else:
            print("Invalid choice, please pick between 1 and 4.")

    print("Thank you for banking with us!")

# this makes our script run as the "main" program
if __name__ == "__main__":
    main()
