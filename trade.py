class Trade:
    def __init__(self, exchange, price, timestamp):
        self.exchange = exchange
        self.price = price
        self.timestamp = timestamp

    def toString(self):
        return ( '[' + self.timestamp + '][' + self.exchange + '] ' + str(self.price) ) 