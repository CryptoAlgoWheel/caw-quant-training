from etherscan.accounts import Account

key=""


# get_all_blocks_mined
# address = '0x2a65aca4d5fc5b5c859090a6c34d164135398226'
# api = Account(address=address, api_key=key)
# blocks = api.get_all_blocks_mined(offset=10000, blocktype='uncles')
# print(blocks)

# get_all_transactions
# address = '0x49edf201c1e139282643d5e7c6fb0c7219ad1db7'
# api = Account(address=address, api_key=key)
# api.get_transaction_page(page=1, offset=10)
# transactions = api.get_all_transactions()
# transactions = api.get_all_transactions(offset=10000, sort='asc',
#                                         internal=False)
# print(transactions[0])

# get_all_transactions
# address = '0xddbd2b932c763ba5b1b7ae3b362eac3e8d40121a'
# api = Account(address=address, api_key=key)
# balance = api.get_balance()
# print(balance)

# get_balance_multiple
# address = ['0xddbd2b932c763ba5b1b7ae3b362eac3e8d40121a',
#            '0xddbd2b932c763ba5b1b7ae3b362eac3e8d40121a']

# api = Account(address=address, api_key=key)
# balances = api.get_balance_multiple()
# print(balances)

# get_blocks_mined_page
# address = '0x2a65aca4d5fc5b5c859090a6c34d164135398226'
# api = Account(address=address, api_key=key)
# blocks = api.get_blocks_mined_page(page=1, offset=10000, blocktype='blocks')
# print(blocks)

# get_transaction_page
# address = '0xddbd2b932c763ba5b1b7ae3b362eac3e8d40121a'
# api = Account(address=address, api_key=key)
# transactions = api.get_transaction_page(page=1, offset=10000, sort='des')
# print(transactions)

# get_transaction_page erc20
# address = '0xddbd2b932c763ba5b1b7ae3b362eac3e8d40121a'
# api = Account(address=address, api_key=key)
# transactions = api.get_transaction_page(page=1, offset=10000, sort='des', erc20=True)
# print(transactions)
