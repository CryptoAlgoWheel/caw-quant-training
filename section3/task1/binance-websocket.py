import time
from binance.client import Client # Import the Binance Client
from binance.websockets import BinanceSocketManager # Import the Binance Socket Manager
import pandas as pd

# Although fine for tutorial purposes, your API Keys should never be placed directly in the script like below. 
# You should use a config file (cfg or yaml) to store them and reference when needed.
API_KEY = ''
API_SECRET = ''


# Instantiate a Client 
client = Client(api_key=API_KEY, api_secret=API_SECRET)

# Instantiate a BinanceSocketManager, passing in the client that you instantiated
bm = BinanceSocketManager(client)

def int2time(timestamp):
    timestamp = timestamp/ 1000 # 13位ts
    value = time.gmtime(timestamp)
    dt = time.strftime('%Y-%m-%d %H:%M:%S', value) # '%Y-%m-%d %H:%M:%S'
    return dt
def int2min(timestamp):
    timestamp = timestamp/ 1000 # 13位ts
    value = time.gmtime(timestamp)
    dt = time.strftime('%M', value) # '%Y-%m-%d %H:%M:%S'
    return dt
# This is our callback function. For now, it just prints messages as they come.
def handle_message(msg):
    global data
    global t
    # If the message is an error, print the error
    if msg['e'] == 'error':    
        print(msg['m'])
    # If the message is a trade: print time, symbol, price, and quantity
    else:
        msg=msg['k']
        
        if int2min(msg['T'])!= int2min(t):
            t=msg['T']
            print("close: {} high: {} low: {} open: {} volume: {} baseVolume: {} datetime:{}".format(msg['c'],msg['h'],msg['l'],msg['o'],msg['v'],msg['q'],int2time(msg['T'])))
            #data.loc[data.shape[0]+1]=[msg['c'],msg['h'],msg['l'],msg['o'],msg['v'],msg['q'],int2time(msg['T'])]
            data=data.append({'close':msg['c'],'high':msg['h'],'low':msg['l'],'open':msg['o'],'volume':msg['v'],'baseVolume':msg['q'],'datetime':int2time(msg['T'])},ignore_index=True)
            data.to_csv("BTC-USDT-lastest-kline.csv",index=False, header=False, mode='a')


data=pd.DataFrame(columns=['close','high','low','open','volume','baseVolume','datetime'])
t=0
# Start trade socket with 'ETHBTC' and use handle_message to.. handle the message.
conn_key = bm.start_kline_socket('BTCUSDT', callback=handle_message, interval=Client.KLINE_INTERVAL_1MINUTE)
# then start the socket manager
bm.start()

# let some data flow..
time.sleep(90)
# stop the socket manager
bm.stop_socket(conn_key)
#data.to_csv("BTC-USDT-lastest-kline.csv",index=False, header=False, mode='a') #, header=True