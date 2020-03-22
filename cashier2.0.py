from machSine import MachSine

# Make an instance
machsine = MachSine()

while True:
    """Main Loop"""
    print()
    print("====================MACHSINE v2.0====================")
    print("Please type 1 or 2 to choose your action:")
    print("(type any letter to quit.)")
    print("1. Change money")
    print("2. Open wallet (Staff only")
    print("3. Restock wallet (Staff only)")

    action = input("Input: ")
    print()

    if action == "1":
        print("====================CHANGE MONEY====================")
        machsine.change_money()
    elif action == "2":
        pass
    elif action == "3":
        pass
    else:
        break