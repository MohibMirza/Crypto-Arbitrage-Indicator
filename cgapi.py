from util import logMsg
from pairmap import PairMap
from pycoingecko import CoinGeckoAPI

def getTickers(coin, e_ids):
    cg = CoinGeckoAPI()
    tickers = [ ]

    i=1
    while i < 10:

        ticker = cg.get_coin_ticker_by_id(id=coin, exchange_ids=e_ids, pages=i)['tickers']
        print(len(ticker))


        i+=1

        if( len(ticker) == 0 ):
            break

        tickers.append(ticker)
        
    return tickers

def makePairMap(listOfTickers):

    mainMap = PairMap()

    for tickers in listOfTickers:
        mainMap.addPairs(tickers)

    return mainMap


# test = getTickers('ethereum', 'serum_dex,uniswap,uniswap_v2,uniswap_v3,pancakeswap,sushiswap,one_inch_liquidity_protocol,okex')
# map = makePairMap(test)
# logMsg(map.toString())

cg = CoinGeckoAPI()
test = getTickers('ethereum', 'serum_dex,uniswap,uniswap_v2,uniswap_v3,pancakeswap,sushiswap,one_inch_liquidity_protocol,okex')
map = makePairMap(test)
logMsg(map.toString())


# coin = 'ethereum'
# e_ids = 'serum_dex,uniswap,uniswap_v2,uniswap_v3,pancakeswap,sushiswap,one_inch_liquidity_protocol,okex'
    
# tickers = getTickers(coin, e_ids)

# pairmap = PairMap()

# for ticker in tickers:
#     pairmap.addPair(ticker)

# logMsg(pairmap.toString())