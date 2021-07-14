from trade import Trade

class Pair:
    def __init__(self, base, target):
        self.base = base
        self.target = target
        self.trades = [ ]

    def createTrade(self, exchange, price, timestamp): 
        newTrade = Trade(exchange, price, timestamp)
        self.insertTrade(newTrade)

    def insertTrade(self, newTrade):
        price = newTrade.price

        i = 0
        inserted = 0
        while(i < len(self.trades)):
            if price < self.trades[i].price:
                self.trades.insert(i, newTrade)
                inserted = 1
                break
            i+=1
        if inserted == 0:
            self.trades.append(newTrade)

    def toString(self):
        msg = self.base + '/' + self.target + ' trading pairs: \n'
        msg += '\tnone' if len(self.trades) == 0 else '' 
        for trade in self.trades: 
            msg += '\t' + trade.toString() + '\n'
        return msg

            


    
