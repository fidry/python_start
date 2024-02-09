from wallet import Wallet
from transactions import Transactions


class Client:
    def __init__(self, private_key: str, rpc: str):
        self.private_key = private_key
        self.rpc = rpc

        self.wallet = Wallet(self)
        self.transactions = Transactions(self)
