import module_manager
module_manager.review()

# Author: Roshan Ram
# AndrewID: rram

import yfinance as yfinance

import module_manager
module_manager.review()

import yfinance as yf # to pull stock data with yf.download(name, yyyy-mm-dd of opening, yyyy-mm-dd of opening)

import numpy as np # used for everything lol
import pandas as pd # data mainpulation
import matplotlib.pyplot as plt # graphing/plotting

%matplotlib inline
#just to make stuff look nice

################################################################################################################

stock = None
while not isinstance(stock, str):
    stock = input("Enter your desired stock. Only alphanumeric characters please.")
openingInp = input("Enter your desired opening date. (yyyy-mm-dd)") #'2016-01-01'
closingInp = input("Enter your desired closing date. (yyyy-mm-dd)") # '2019-08-01'


data = yf.download(stock, openingInp, closingInp)


# commodity channel index (CCI) algorithm
# mathematical calculation: https://www.investopedia.com/terms/c/commoditychannelindex.asp
# CCI = (Typical price – MA of Typical price) / (0.015 * Standard deviation of Typical price)
def calcCCI(data, numDays):
    movingAverageSum = 0
    typicalPrice = (data['Low'] + data['High'] + data['Close'])/3
#     for row in range(len(data['Low'])-30):
#         for i in range(30):
#             movingAverageSum +=
    top = typicalPrice - pd.Series(typicalPrice).rolling(window=numDays).mean()
    bottom = pd.Series(0.015 * pd.Series(typicalPrice).rolling(window=numDays).std())
    cci = pd.Series(top/bottom, name = 'CCI')
    data = data.join(cci)
    return data


def showCCI(data, numDays):
    cci = calcCCI(data, numDays)['CCI']
    fig = plt.figure(figsize=(7, 5))
    ax = fig.add_subplot(2, 1, 1)
    ax.set_xticklabels([])
    plt.plot(data['Close'], lw=1)
    plt.title('NSE Price Chart')
    plt.ylabel('Close Price')
    plt.grid(True)
    bx = fig.add_subplot(2, 1, 2)
    plt.plot(cci, 'k', lw=0.75, linestyle='-', label='CCI')
    plt.legend(loc=2, prop={'size': 9.5})
    plt.ylabel('CCI values')
    plt.grid(True)
    plt.setp(plt.gca().get_xticklabels(), rotation=30)
    plt.show()


def rollingAverage(data, numDays):
    total = [0]
    movingAverages = []
    for i, x in enumerate(data, 1):
        total.append(total[i - 1] + x)
        if i >= numDays:
            currMovingAverage = (total[i] - total[i - numDays]) / numDays
            movingAverages.append(currMovingAverage)

    return pd.Series(movingAverages)


# exponential calculation:
# https://www.investopedia.com/ask/answers/122314/what-exponential-moving-average-ema-formula-and-how-ema-calculated.asp
def calcMA(data, numDays, calcType):
    '''
    calculates the moving average
    data: the data you want to use
    numDays: number of days to perform the average over
    calcType: the type of average to be done--
    '''
    if calcType == 'simple':
        simple = pd.Series(pd.Series(data['Close']).rolling(window=numDays).mean(), name='SMA')
        #         pd.Series(typicalPrice).rolling(window=numDays).mean()
        data = data.join(simple)
        return data
    elif calcType == 'exponential':
        #         exp = pd.Series(pd.ewma(data['Close'], span = numDays, min_periods = numDays))
        exp = data.ewm(span=numDays, min_periods=numDays,
                       adjust=False).mean()  # todo this doesn't work, just rewrite real way

        data = data.join(exp)
        return data

# ease of movement:
def EVM(data, numDays):
 distMoved = ((data['High'] + data['Low'])/2) - ((data['High'].shift(1) + data['Low'].shift(1))/2)
 boxRatio = (data['Volume'] / 100000000) / ((data['High'] - data['Low']))
 evm = distMoved/boxRatio
 evmMA = pd.Series(rollingMean(evm, numDays), name = 'EVM')
 data = data.join(evmMA)
 return data

def stochasticK(df):
    """Calculate stochastic oscillator %K for given data.
    input: pandas DataFrame
    output: pandas DataFrame
    """
    stochK = pd.Series((df['Close'] - df['Low']) / (df['High'] - df['Low']), name='stochastic %K')
    df = df.join(stochK)
    return df

def stochasticD(df, numDays):
    """Calculate stochastic oscillator %D for given data.
    input: pandas DataFrame
    output: pandas DataFrame
    """
    stochK = pd.Series((df['Close'] - df['Low']) / (df['High'] - df['Low']), name='stochastic %K')
    stochD = pd.Series(stochK.ewm(span=numDays, min_periods=numDays).mean(), name=f'stochastic %D, {str(numDays)} days') # todo: rewrite ewm manually
    df = df.join(stochD)
    return df


