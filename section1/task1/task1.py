import requests
import pandas as pd
import json
import time
import datetime

def int2time(timestamp):
    # timestamp = timestamp/ 1000 # 13位ts
    value = time.localtime(timestamp)
    dt = time.strftime('%Y-%m-%d %H:%M:%S', value) # '%Y-%m-%d %H:%M:%S'
    return dt

def time2int(ts):
    value = time.strptime(ts, '%Y-%m-%d %H:%M:%S')
    intime = time.mktime(value)
    return intime


class cryptocompare:
    def __init__(self,addr="https://min-api.cryptocompare.com/"):
        self._addr = addr

    def get_histohour(self):
        timefrom=datetime.datetime(2017, 4, 1,18,0,0)#"2017-04-01 18:00:00"
        timeto=datetime.datetime(2020, 4, 1,18,0,0)  #"2020-04-01 18:00:00"
        def get_data(datetime):
            apiKey = ""
            url = "https://min-api.cryptocompare.com/data/histohour"
            params = {
                "api_key": apiKey,
                "fsym": "BTC",
                "tsym": "USDT",
                "e": "binance",
                "limit": 23,
                "toTs": time2int(str(datetime))
            }
            result = requests.get(url, params=params).json()

            df = pd.DataFrame(result['Data'])
            df['time']=pd.to_datetime(df['time'], unit='s').dt.strftime('%Y-%m-%d %H:%M:%S')
            order=['close','high','low','open',"volumefrom","volumeto",'time']
            df=df[order]
            df.columns=['close','high','low','open',"volume","baseVolume",'datetime']
            return df
        holder = pd.DataFrame(columns=['close','high','low','open',"volume","baseVolume",'datetime'])
        date=timefrom
        while date <= timeto:
            df=get_data(date)
            holder=holder.append(df, ignore_index=True)
            date+=datetime.timedelta(days=1)
        t1=timefrom.strftime('%Y%m%d')
        t2=timeto.strftime('%Y%m%d')
        holder.to_csv("BTC-USDT-%s-%s.csv"%(t1,t2),index=False, header=True) 
    
    
    def mktcapfull(self):
        apiKey = "de5b2dcdaaea9bd25f362226b9912ccda870879cfa75afe2192fc6bd6fe22acf"
        url = "https://min-api.cryptocompare.com/data/top/mktcapfull"
        params = {
            "api_key": apiKey,
            "fsym": "BTC",
            "tsym": "USDT",
            'MARKET': "binance"
        }
        result = requests.get(url, params=params).json()
        df = pd.DataFrame(result['Data'])
        df.to_csv("marketcapfull.csv",index=False, header=True) 




df=cryptocompare()
df.get_histohour()
df.mktcapfull()
