def calculateAvg(tickers):
    prices = []

    for ticker in tickers:
        if(ticker['target'] == 'USDT' or ticker['target'] == 'USD' and ticker['last'] < 500000):
            prices.append(ticker['last'])
    
    avg = sum(prices)/len(prices)

    return avg

def checkForArbitrage(tickers, avg, threshold):

    arbitrages = []

    for ticker in tickers:
        if ticker['target'] == 'USD' or ticker['target'] == 'USDT':
            price = ticker['last']

            deviation = abs(price -avg)/avg

            if deviation >= threshold:
                arbitrages.append(toString(ticker, deviation))

    return arbitrages


def toString(ticker):
    msg = '[' + ticker['market']['name'] + '] '
    msg += ticker['base'] + '/' + ticker['target'] + ': ' + str(ticker['last'])
    return msg

# def toString(ticker, arb):
#     msg = '[' + ticker['market']['name'] + '] '
#     msg += ticker['base'] + '/' + ticker['target'] + ': ' + str(ticker['last'])
#     msg += '(' + str(arb) + '%)'
#     return msg

def logAllPairs(fileName, tickers):
    with open('log.txt', 'a') as fid:
        for pair in tickers:
            fid.write(pair['market']['identifier'] + '\n')
        
        fid.close()

def logMsg(msg):
    with open('log.txt', 'a') as fid:
        fid.write(msg)
