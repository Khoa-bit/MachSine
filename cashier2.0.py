import json

filename = 'wallet.json'
with open(filename) as f:
    wallet = json.load(f)

money = {"20_000": 0, "10_000": 0, "5_000": 0, "2_000": 0, "1_000": 0, "500": 0}
candy = False

# Prompt cashier
print("Change money machSine")
give =  int(input("Take:"))
price = int(input("Cost:"))
change = 0

# Post change
if (give > price):
    change = give - price
    print(f"Original change: {change}")

    # Calculate change with existing amount
    while(change != 0):
        if (change >= 20_000 and wallet["20_000"] > 0):
            change -= 20_000
            wallet["20_000"] -= 1
            money["20_000"] += 1

        elif (change >= 10_000 and wallet["10_000"] > 0):
            change -= 10_000
            wallet["10_000"] -= 1
            money["10_000"] += 1
            
        elif (change >= 5_000 and wallet["5_000"] > 0):
            change -= 5_000
            wallet["5_000"] -= 1
            money["5_000"] += 1

        elif (change >= 2_000 and wallet["2_000"] > 0):
            change -= 2_000
            wallet["2_000"] -= 1
            money["2_000"] += 1

        elif (change >= 1_000 and wallet["1_000"] > 0):
            change -= 1_000
            wallet["1_000"] -= 1
            money["1_000"] += 1

        elif (change >= 500 and wallet["500"] > 0):
            change -= 500
            wallet["500"] -= 1
            money["500"] += 1

        else:
            candy = True
            break

    # Give change to customer
    print("Change:")

    for currency, amount in money.items():
        if amount != 0:
            print(f"{currency}vnd x{amount}")

    if candy:
        print(f"Candy instead? ({change}vnd left)")

elif (give == price):
    print("Thank you! See you soon.")
else:
    print("Not enough money.")

with open(filename, 'w') as f:
    json.dump(wallet, f)