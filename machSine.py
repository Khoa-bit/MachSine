import json

class MachSine:
    """A class to represent a MachSine."""
    def __init__(self):
        # Load wallet
        filename = 'wallet.json'
        with open(filename) as f:
            self.wallet = json.load(f)

    def change_money(self):
        # Initialize change
        money = {"20_000": 0, "10_000": 0, "5_000": 0, "2_000": 0, "1_000": 0, "500": 0}
        candy = False

        # Prompt user
        give =  int(input("Take:"))
        price = int(input("Cost:"))
        change = 0
        print()

        # Post change
        if (give > price):
            change = give - price
            print(f"Original change: {change}")

            # Calculate change with existing amount
            while(change != 0):
                if (change >= 20_000 and self.wallet["20_000"] > 0):
                    change -= 20_000
                    self.wallet["20_000"] -= 1
                    money["20_000"] += 1

                elif (change >= 10_000 and self.wallet["10_000"] > 0):
                    change -= 10_000
                    self.wallet["10_000"] -= 1
                    money["10_000"] += 1
                    
                elif (change >= 5_000 and self.wallet["5_000"] > 0):
                    change -= 5_000
                    self.wallet["5_000"] -= 1
                    money["5_000"] += 1

                elif (change >= 2_000 and self.wallet["2_000"] > 0):
                    change -= 2_000
                    self.wallet["2_000"] -= 1
                    money["2_000"] += 1

                elif (change >= 1_000 and self.wallet["1_000"] > 0):
                    change -= 1_000
                    self.wallet["1_000"] -= 1
                    money["1_000"] += 1

                elif (change >= 500 and self.wallet["500"] > 0):
                    change -= 500
                    self.wallet["500"] -= 1
                    money["500"] += 1

                else:
                    candy = True
                    break

            # Check whether machine have enough money in wallet to give change.
            if (change < 500):
                # Give change to customer
                print("Change:")

                for currency, amount in money.items():
                    if amount != 0:
                        print(f"{currency}vnd x{amount}")

                if candy:
                    print(f"Candy instead? ({change}vnd left)")

            else:
                print("Cannot give change... :(")
                print("Sorry for this inconvenience. Please use less money or contact our staff for help.")


        elif (give == price):
            print("Perfect! See you soon. :)")
        elif (give < price):
            change = price - give
            print(f"Sorry... You are missing {change}vnd.")

        # Update wallet.
        filename = 'wallet.json'
        with open(filename, 'w') as f:
            json.dump(self.wallet, f)