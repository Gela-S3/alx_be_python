import sys
from bank_account import BankAccount

def main():
    # Example starting balance for testing. You can change this.
    account = BankAccount(100)

    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    # Split the argument into command and optional parameters
    command_parts = sys.argv[1].split(':')
    command = command_parts[0]
    
    amount = None
    if len(command_parts) > 1:
        try:
            amount = float(command_parts[1])
        except ValueError:
            print("Error: Amount must be a number.")
            sys.exit(1)

    if command == "deposit":
        if amount is not None:
            try:
                account.deposit(amount)
                print(f"Deposited: ${amount:.2f}")
            except ValueError as e:
                print(f"Error: {e}")
        else:
            print("Error: Deposit command requires an amount.")
    elif command == "withdraw":
        if amount is not None:
            try:
                if account.withdraw(amount):
                    print(f"Withdrew: ${amount:.2f}")
                else:
                    print("Insufficient funds.")
            except ValueError as e:
                print(f"Error: {e}")
        else:
            print("Error: Withdraw command requires an amount.")
    elif command == "display":
        if amount is None: # Ensure no amount is provided for display
            account.display_balance()
        else:
            print("Error: Display command does not take an amount.")
    else:
        print("Invalid command.")
        print("Commands: deposit, withdraw, display")

if __name__ == "__main__":
    main()