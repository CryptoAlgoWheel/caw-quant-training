from etherscan.accounts import Account
from etherscan.proxies import Proxies

key=""

# gas_price?
# api = Proxies(api_key=key)
# price = api.gas_price()
# print(price)

# get_block_by_number
# api = Proxies(api_key=key)
# block = api.get_block_by_number(5747732)
# print(block['number'])

# get_block_transaction_count_by_number
# api = Proxies(api_key=key)
# tx_count = api.get_block_transaction_count_by_number(block_number='0x10FB78')
# print(int(tx_count, 16))

# get_code
# api = Proxies(api_key=key)
# code = api.get_code('0xf75e354c5edc8efed9b59ee9f67a80845ade7d0c')
# print(code)

# get_most_recent_block
# api = Proxies(api_key=key)
# block = api.get_most_recent_block()
# print(int(block, 16))

# get_storage_at
# api = Proxies(api_key=key)
# value = api.get_storage_at('0x6e03d9cce9d60f3e9f2597e13cd4c54c55330cfd', 0x0)
# print(value)

# get_transaction_by_blocknumber_index
# api = Proxies(api_key=key)
# transaction = api.get_transaction_by_blocknumber_index(block_number='0x57b2cc',
#                                                        index='0x2')
# print(transaction['transactionIndex'])

# get_transaction_by_hash
# TX_HASH = '0x1e2910a262b1008d0616a0beb24c1a491d78771baa54a33e66065e03b1f46bc1'
# api = Proxies(api_key=key)
# transaction = api.get_transaction_by_hash(
#     tx_hash=TX_HASH)
# print(transaction['hash'])

# get_transaction_count
# api = Proxies(api_key=key)
# count = api.get_transaction_count('0x6E2446aCfcec11CC4a60f36aFA061a9ba81aF7e0')
# print(int(count, 16))

# get_transaction_receipt
# api = Proxies(api_key=key)
# receipt = api.get_transaction_receipt(
#     '0xb03d4625fd433ad05f036abdc895a1837a7d838ed39f970db69e7d832e41205d')
# print(receipt)

# get_uncle_by_blocknumber_index
# api = Proxies(api_key=key)
# uncles = api.get_uncle_by_blocknumber_index(block_number='0x210A9B',
#                                             index='0x0')
# print(uncles['uncles'])