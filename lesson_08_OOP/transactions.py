from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from client import Client


class Transactions:
    def __init__(self, client: Client):
        self.client = client

    def aprrove(self):
        print(self.client.private_key, 'делаю approve')

    def sign_transaction(self):
        print(self.client.private_key, 'подписываю транзакцию')
