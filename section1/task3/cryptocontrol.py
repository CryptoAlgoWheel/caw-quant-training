from crypto_news_api import CryptoControlAPI

# Connect to the CryptoControl API
api = CryptoControlAPI("")

# # Connect to a self-hosted proxy server (to improve performance) that points to cryptocontrol.io
# proxyApi = CryptoControlAPI("", "http://cryptocontrol_proxy/api/v1/public")

# # Enable the sentiment datapoints
# api.enableSentiment()

# # Get top news
# print(api.getTopNews())

# # get latest russian news
# print(api.getLatestNews("ru"))

# get top bitcoin news
# print(api.getTopNewsByCoin("bitcoin"))

# # get top EOS tweets
# print(api.getTopTweetsByCoin("eos"))

# # get top Ripple reddit posts
# print(api.getLatestRedditPostsByCoin("ripple"))

# # get reddit/tweets/articles in a single combined feed for NEO
# print(api.getTopFeedByCoin("neo"))

# # get latest reddit/tweets/articles (seperated) for Litecoin
# print(api.getLatestItemsByCoin("litecoin"))

# # get details (subreddits, twitter handles, description, links) for ethereum
# print(api.getCoinDetails("ethereum"))

import pandas as pd
data= api.getTopNewsByCoin("bitcoin")
data=pd.DataFrame(data=data)
data.to_csv("BTC-news-cryptocontrol.csv",index=False, header=True) 