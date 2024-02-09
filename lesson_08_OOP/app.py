from client import Client


client = Client(private_key='111', rpc='arbitrum')
client2 = Client(private_key='222', rpc='arbitrum')

client.wallet.get_nonce()
client2.wallet.get_nonce()

client.transactions.sign_transaction()
client2.transactions.sign_transaction()
