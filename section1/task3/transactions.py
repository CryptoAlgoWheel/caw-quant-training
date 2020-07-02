  
from etherscan.transactions import Transactions

key=""

get_status
TX_HASH = '0x15f8e5ea1079d9a0bb04a4c58ae5fe7654b5b2b4463375ff7ffb490aa0032f3a'
api = Transactions(api_key=key)
status = api.get_status(tx_hash=TX_HASH)
print(status)


get_tx_receipt_status
TX_HASH = '0x513c1ba0bebf66436b5fed86ab668452b7805593c05073eb2d51d3a52f480a76'
api = Transactions(api_key=key)
receipt_status = api.get_tx_receipt_status(tx_hash=TX_HASH)
print(receipt_status)