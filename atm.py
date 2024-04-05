class User:
    userlst=[]
    def __init__(self, userName, accountNumber, balanceAmount, pin):
        self.userName = userName
        self.accountNumber = accountNumber
        self.balanceAmount = balanceAmount
        self.pin = pin
        User.userlst.append(self)
    def withdraw(self, amount):
        if amount > self.balanceAmount:
            print("Insufficient funds!")
        else:
            self.balanceAmount -= amount
            print("Updated Balance:", self.balanceAmount)
            self.display_balance_info()

    def display_balance_info(self):
        print("Balance Info:", [self.userName, self.accountNumber, self.balanceAmount, self.pin])

    def change_pin(self):
        new_pin = int(input("Enter the New Pin: "))
        re_enter = int(input("Re-Enter your new Pin: "))
        if new_pin == re_enter:
            self.pin = new_pin
            print("Pin changed successfully.")
        else:
            print("Both the Pins are not the same! Kindly check.")

users = [
    User("venkat", 123456789, 1000, 989),
    User("ram", 123456, 1000, 686)
]

def find_user_by_pin(pin):
    for user in users:
        if user.pin == pin:
            return user
    return None
user_pin = int(input("Enter the Pin: "))
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

class AdminAccess:
    def admin_access():
        # # database = User.userlst
        # print(database)
        total_balance=0
        print("Admin Access - Customer Details:")
        for user in User.userlst:
            print("Name:",user.userName)
            print("AccNumber:", user.accountNumber)
            print("Balance:", user.balanceAmount)
            total_balance+=user.balanceAmount

        print("The Toatl balance of the all Accounts")
        print(total_balance)
# Calling the admin_access method
AdminAccess.admin_access()
