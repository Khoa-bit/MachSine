import json

class MachSine:
    """A class to represent a MachSine."""
    def __init__(self):
        # Initialize stats
        self.money = {}
        self.candy = False
        self.wallet_before_change = {}

    def process_money(self, change):
        # Load wallet
        filename = 'wallet.json'
        with open(filename) as f:
            wallet = json.load(f)

        # Save wallet for checking conditions.
        self.wallet_before_change = wallet.copy()
        print(f"wallet_before_change: {self.wallet_before_change}")
        
        # Calculate change
        while(change != 0):
            if (change >= 20_000 and wallet["20_000"] > 0):
                change -= 20_000
                wallet["20_000"] -= 1
                self.money["20_000"] += 1

            elif (change >= 10_000 and wallet["10_000"] > 0):
                change -= 10_000
                wallet["10_000"] -= 1
                self.money["10_000"] += 1
                
            elif (change >= 5_000 and wallet["5_000"] > 0):
                change -= 5_000
                wallet["5_000"] -= 1
                self.money["5_000"] += 1

            elif (change >= 2_000 and wallet["2_000"] > 0):
                change -= 2_000
                wallet["2_000"] -= 1
                self.money["2_000"] += 1

            elif (change >= 1_000 and wallet["1_000"] > 0):
                change -= 1_000
                wallet["1_000"] -= 1
                self.money["1_000"] += 1

            elif (change >= 500 and wallet["500"] > 0):
                change -= 500
                wallet["500"] -= 1
                self.money["500"] += 1

            else:
                candy = True
                break
        
        # Update wallet.
        print(wallet)
        print(f"wallet_before_change but after change: {self.wallet_before_change}")
        filename = 'wallet.json'
        with open(filename, 'w') as f:
            json.dump(wallet, f)

        # Return left-over change
        return change

    def change_money(self):
        # Initialize change and reset.
        self.money = {"20_000": 0, "10_000": 0, "5_000": 0, "2_000": 0, "1_000": 0, "500": 0}
        self.candy = False

        # Prompt user
        give =  int(input("Take:"))
        price = int(input("Cost:"))
        print()

        # Give change
        if (give > price):
            original_change = give - price
            print(f"Original change: {original_change}")

            final_change = self.process_money(original_change)

            # Check whether machine have enough money in wallet to give change.
            if (final_change < 500):
                # Give change to customer
                print("Change:")

                # Display change
                for currency, amount in self.money.items():
                    if amount != 0:
                        print(f"{currency}vnd x{amount}")

                if self.candy:
                    print(f"Candy instead? ({final_change}vnd left)")

            else:
                # Unsuccessful transaction, revert changes to wallet
                filename = 'wallet.json'
                with open(filename, 'w') as f:
                    json.dump(self.wallet_before_change, f)

                print("Cannot give change... :(")
                print("Sorry for this inconvenience. Please use less money or contact our staff for help.")

        # No need to give change
        elif (give == price):
            # Update wallet
            original_change = give
            self.process_money(original_change)

            print("Perfect! See you soon. :)")

        # Prompt user to add more money
        elif (give < price):
            missing = price - give
            print(f"Sorry... You are missing {missing}vnd.")