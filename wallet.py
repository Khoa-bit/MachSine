import json

class Wallet:
    """A class to manage MachSine's wallet."""
    def __init__(self):
        pass

    def read_wallet(self):
        """Display wallet content."""
        # Load current wallet.
        filename = 'wallet.json'
        with open(filename) as f:
            wallet = json.load(f)

        # Display wallet
        print("Content:")

        for currency, amount in wallet.items():
            if amount != 0:
                print(f"{currency}vnd x{amount}")

    def restock_wallet(self):
        print("Restock to 5 bills for each currency.")
        wallet = {"20_000": 5, "10_000": 5, "5_000": 5, "2_000": 5, "1_000": 5, "500": 5}

        # Update wallet.
        filename = 'wallet.json'
        with open(filename, 'w') as f:
            json.dump(wallet, f)

        self.read_wallet()