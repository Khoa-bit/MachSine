import json

class Wallet:
    """A class to manage MachSine's wallet."""
    def __init__(self):
        """Load wallet."""
        filename = 'wallet.json'
        with open(filename) as f:
            self.wallet = json.load(f)

    def read_wallet(self):
        """Display wallet content."""
        print("Content:")

        for currency, amount in self.wallet.items():
            if amount != 0:
                print(f"{currency}vnd x{amount}")