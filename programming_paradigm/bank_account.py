class BankAccount:
    def __init__(self, initial_balance=0):

        if not isinstance(initial_balance, (int, float)) or initial_balance < 0:
            raise ValueError("Initial balance must be a non-negative number.")
        self.__account_balance = initial_balance  # Encapsulation: use double underscore for "private"

    def deposit(self, amount):
        
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Deposit amount must be a positive number.")
        self.__account_balance += amount
        # print(f"Successfully deposited: ${amount:.2f}") # This print is handled by main-0.py

    def withdraw(self, amount):
        """
        Withdraws the specified amount from the account if funds are sufficient.

        Args:
            amount (float): The amount to withdraw. Must be positive.

        Returns:
            bool: True if the withdrawal was successful, False otherwise.
        """
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Withdrawal amount must be a positive number.")
        if self.__account_balance >= amount:
            self.__account_balance -= amount
            # print(f"Successfully withdrew: ${amount:.2f}") # This print is handled by main-0.py
            return True
        else:
            # print("Insufficient funds for withdrawal.") # This print is handled by main-0.py
            return False

    def display_balance(self):
        print(f"Current Balance: ${self.__account_balance:.2f}")