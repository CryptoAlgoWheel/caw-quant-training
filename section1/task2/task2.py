from binance.client import Client
import pandas as pd
import time

def int2time(timestamp):
    timestamp = timestamp/ 1000 # 13位ts
    value = time.gmtime(timestamp)
    dt = time.strftime('%Y-%m-%d %H:%M:%S', value) # '%Y-%m-%d %H:%M:%S'
    return dt

API_KEY = ''
API_SECRET = ''
client = Client(API_KEY, API_SECRET)



# get historical kline data from any date range
klines = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_1HOUR, "1 Dec, 2017", "2 Dec, 2017")
klines=pd.DataFrame(columns=["Open time","Open","High","Low","Close","Volume","Close time","Quote asset volume","Number of trades","Taker buy base asset volume","Taker buy quote asset volume","Ignore"],data=klines)
klines["Open time"]=klines["Open time"].apply(lambda x: int2time(x))
klines.to_csv("BTC-USDT-20171201-20171202.csv",index=False, header=True) 

# get market depth
depth = client.get_order_book(symbol='BTCUSDT')
depth = pd.DataFrame(columns=["Price","Volume"],data=depth['bids'])
depth.to_csv("BTC-USDT-lastest-depth.csv",index=False, header=True) 

# get trades
trades = client.get_recent_trades(symbol='BTCUSDT')
trades = pd.DataFrame(trades)
trades["time"]=trades["time"].apply(lambda x: int2time(x))
trades.to_csv("BTC-USDT-lastest-trades.csv",index=False, header=True) 


# Place a test order
from binance.enums import *
order = client.create_test_order(
    symbol='BTCUSDT',
    side=SIDE_BUY,
    type=ORDER_TYPE_LIMIT,
    timeInForce=TIME_IN_FORCE_GTC,
    quantity=100,
    price='9168')

# order = client.get_order(
#     symbol='BTCUSDT',
#     orderId='orderId')