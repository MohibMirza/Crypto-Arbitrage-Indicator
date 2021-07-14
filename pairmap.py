from pair import Pair


class PairMap:
    def __init__(self):
        self.map = dict()

    def addPairs(self, tickers):
        for ticker in tickers:
            self.addPair(ticker)     

    def addPair(self, ticker):
        base = ticker['base']
        target = ticker['target']
        tokens = base + '/' + target

        if tokens not in self.map:
            self.map[tokens] = Pair(base, target)
        
        exchange = ticker['market']['name']
        price = ticker['last']
        timestamp = ticker['last_fetch_at']


        self.map[tokens].createTrade(exchange, price, timestamp)

    def toString(self):
        print('len of pairs: ', len(self.map))
        msg = ''
        for pair in self.map:
            msg += self.map[pair].toString()

        return msg