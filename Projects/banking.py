class Bank:
    allUsers = {}
    
    def __init__(self, name, balance):
        try:
            balance = int(balance)
            self.name = name
            self.balance = balance
            self.__saveBalance()
            Bank.allUsers[name] = balance
        except ValueError as e:
            print(e)
    
    def deposit(self, amount):
        try:
            amount = int(amount)
            self.balance += amount
            with open(f'{self.name}Transaction.txt', 'a') as file:
                file.write(f'Deposit: {amount} \t\t Balance: {self.balance}\n')
            Bank.allUsers[self.name] = self.balance
            return f'Total balance is {self.balance}'
        except ValueError as e: 
            print(f"Invalid input: {e}")
            
    def withdraw(self, amount):
        try: 
            amount = int(amount)
            if amount > self.balance:
                return 'Not enough balance'
            else:
                self.balance -= amount
                with open(f'{self.name}Transaction.txt', 'a') as file:
                    file.write(f'Withdraw: {amount} \t\t Balance: {self.balance}\n')
                Bank.allUsers[self.name] = self.balance
                return f'Remaining balance is {self.balance}'
        except ValueError as e:
            print(f"Invalid input: {e}")

    def checkBalance(self):
        print(f'{self.name}, Your balance is {self.balance}')
      
    def __saveBalance(self):
        with open(f'{self.name}Transaction.txt', 'w') as file:
            file.write(f'{self.name}: {self.balance}\n')

while True:
    # first get the user name
    user = input('Enter the user name: ')
    if user.isalpha:
        # check if the user exists in all users 
        if user not in Bank.allUsers:
            print('You don\'t have an account, please create one')
            # ask user if he wants to create an account or not
            choice = input('Do you want to create a new account? (y/n): ')
            if choice in ['y', 'n']:
                if choice == 'y':  # in this case create an account
                    # ask for initial amount
                    amount = input('\nEnter the initial amount: ')
                    obj = Bank(user, amount)
                    print(f'Account created for {user} with initial balance: {amount}')
                else:    
                    break
        else:
            # ask if user wants to deposit or withdraw
            action = input('\nEnter "d" for deposit, "w" for withdraw, or "x" for quitting: ')
            if action == 'd':  # in this case I have to perform the deposit
                amount = input('Enter the amount to deposit: ')
                result = obj.deposit(amount)
                print(result)
            
            elif action == 'w':  # in this case I have to perform the withdrawal
                amount = input('Enter the amount to withdraw: ')
                result = obj.withdraw(amount)
                print(result)

            elif action == 'x':
                print('Thank you for using our banking system.')
                break
            else:
                print("Invalid action. Please enter 'd', 'w', or 'x'.")
    else:
        print('please enter valid user name')
