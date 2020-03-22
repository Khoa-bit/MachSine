from machSine import MachSine
from wallet import Wallet

# Create instances
machsine = MachSine()
wallet = Wallet()

while True:
    """Main Loop"""
    print()
    print("====================MACHSINE v2.0====================")
    print("Please type 1 or 2 to choose your action:")
    print("(type any letter to quit.)")
    print("1. Change money")
    print("2. Read wallet (Staff only")
    print("3. Restock wallet (Staff only)")

    action = input("Input: ")
    print()

    if action == "1":
        print("====================CHANGE MONEY====================")
        machsine.change_money()

    elif action == "2":
        wallet.read_wallet()
    elif action == "3":
        pass
    else:
        break
    
    # Wait for user
    print()
    input("Press any key to continue.")