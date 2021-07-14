import json
from pairmap import PairMap
import util
import trade
from time import sleep
from pycoingecko import CoinGeckoAPI

coin = 'ethereum'
e_ids = 'serum_dex,uniswap,uniswap_v2,uniswap_v3,pancakeswap,sushiswap,one_inch_liquidity_protocol,okex'

cg = CoinGeckoAPI()
coin_tickers = cg.get_coin_ticker_by_id(id=coin, exchange_ids=e_ids, pages=1)
btc = coin_tickers['tickers']

test = PairMap(btc)
print(test.toString())
util.logMsg(test.toString())






#arbitrages= util.checkForArbitrage(btc, avg=avgPrice, threshold=0.01)

#print(arbitrages)


# while True:
#     for exchange in btc:
#         if exchange['target'] == 'USDT' or exchange['target'] == 'USD' and exchange['last'] < 500000:
#             percent = float(((starting_price - exchange['last']) * 100) / exchange['last'])
#             if percent >= 1.5 and exchange['last'] >= 100:
#                 processed.append(str(exchange['market']['name']) +':'+ str(exchange['last']))
#         if len(processed) == 0:
#             sleep(30)
#             continue
#         else:
#             break
    
#print(processed)