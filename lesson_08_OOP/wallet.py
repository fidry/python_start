from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from client import Client


class Wallet:
    def __init__(self, client: Client):
        self.client = client

    def get_balance(self):
        print(self.client.private_key, 'проверяю баланс')

    def get_nonce(self):
        print(self.client.private_key, 'проверяю nonce')
