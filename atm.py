class User:
    user_list = []

    def __init__(self, user_name, account_number, balance_amount, pin):
        self.user_name = user_name
        self.account_number = account_number
        self.balance_amount = balance_amount
        self.pin = pin
        User.user_list.append(self)

    def withdraw(self, amount):
        if amount > self.balance_amount:
            print("Insufficient funds!")
        else:
            self.balance_amount -= amount
            print("Updated Balance:", self.balance_amount)
            self.display_balance_info()

    def display_balance_info(self):
        print("Balance Info:", [self.user_name, self.account_number, self.balance_amount])

    def change_pin(self):
        new_pin = input("Enter the New Pin: ")
        re_enter = input("Re-Enter your new Pin: ")
        if new_pin == re_enter:
            self.pin = new_pin
            print("Pin changed successfully.")
        else:
            print("Both the Pins are not the same! Kindly check.")


class AdminAccess:
    @staticmethod
    def admin_access():
        total_balance = 0
        print("Admin Access - Customer Details:")
        for user in User.user_list:
            print("Name:", user.user_name)
            print("AccNumber:", user.account_number)
            print("Balance:", user.balance_amount)
            total_balance += user.balance_amount

        print("The Total balance of all Accounts:", total_balance)


class Bank:
    @staticmethod
    def bank_access():
        print("User List:")
        for user in User.user_list:
            print("Name:", user.user_name)
            print("AccNumber:", user.account_number)


def main():
    print("1. Access User 2. Access Admin 3. Access Bank")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        user_pin = input("Enter the Pin: ")
        user = find_user_by_pin(user_pin)
        if user:
            process = int(input("Enter your choice (1: Withdraw, 2: Change PIN, 3: Check Balance): "))
            if process == 1:
                amount = int(input("Enter the amount to withdraw: "))
                user.withdraw(amount)
            elif process == 2:
                user.change_pin()
            elif process == 3:
                user.display_balance_info()
            else:
                print("Invalid choice!")
        else:
            print("User not found or invalid PIN.")
    elif choice == 2:
        AdminAccess.admin_access()
    elif choice == 3:
        Bank.bank_access()
    else:
        print("Invalid choice!")


def find_user_by_pin(pin):
    for user in User.user_list:
        if user.pin == pin:
            return user
    return None


if __name__ == "__main__":
    User("venkat", 123456789, 1000, "989")
    User("ram", 123456, 1000, "686")
    main()
