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


# rate of change (roc): https://www.investopedia.com/terms/p/pricerateofchange.asp
def roc(data, n):
    '''
    "a momentum-based technical indicator that measures the
    percentage change in price between the current price and
    the price a certain number of periods ago. The ROC indicator
    is plotted against zero, with the indicator moving upwards into
    positive territory if price changes are to the upside, and moving
    into negative territory if price changes are to the downside."
    '''
    roc = 100 * ((close - close.shift(n)) / close.shift(n))
    if fillna:
        roc = roc.replace([np.inf, -np.inf], np.nan).fillna(0)
    return pd.Series(roc, name='ROC')


# bollinger bands (bb): https://traderhq.com/ultimate-guide-to-bollinger-bands/
def calcbolBands(data, n):
    # Calculate n-Day Moving Average, Std Deviation, Upper Band and Lower Band
    data['MA'] = data['Adj Close'].rolling(window=n).mean()
    data['STD'] = data['Adj Close'].rolling(window=n).std()
    data['UpperBand'] = data['MA'] + (data['STD'] * 2)
    data['LowerBand'] = data['MA'] - (data['STD'] * 2)

    # Simple 30 Day Bollinger Band for Facebook (2016-2017)
    #     stock[pd.DataFrame('Adj Close', '30 Day MA', 'Upper Band', 'Lower Band')].plot(figsize=(12,6))
    data['Adj Close'].plot(figsize=(12, 6))
    data['MA'].plot(figsize=(12, 6))
    data['UpperBand'].plot(figsize=(12, 6))
    data['LowerBand'].plot(figsize=(12, 6))
    plt.title(f'{n} Day Bollinger Band for AAPL')
    plt.ylabel('Price (USD)')

    # fill inbetween
    #     plt.fill_between(x_axis, fb['Upper Band'], fb['Lower Band'], color='grey')

    plt.show();

    from datetime import *
    # remap indices with respect to the first date, in days

    # https://stackoverflow.com/questions/1345827/how-do-i-find-the-time-difference-between-two-datetime-objects-in-python

    def daysFromSecs(seconds=None):
        return divmod(seconds if seconds != None else duration_in_s, 86400)  # Seconds in a day = 86400

    start = data.index.values[0]
    for i in range(len(data.index.values)):
        print(daysFromSecs(int(data.index.values[i + 1]) - int(data.index.values[i]))).head()



    #######

    # Example of Standalone Simple Linear Regression
    from math import sqrt

    # Calculate root mean squared error
    def rmse_metric(actual, predicted):
        sum_error = 0.0
        for i in range(len(actual)):
            prediction_error = predicted[i] - actual[i]
            sum_error += (prediction_error ** 2)
        mean_error = sum_error / float(len(actual))
        return sqrt(mean_error)

    # Evaluate regression algorithm on training dataset
    def evaluate_algorithm(dataset, algorithm):
        test_set = list()
        for row in dataset:
            row_copy = list(row)
            row_copy[-1] = None
            test_set.append(row_copy)
        predicted = algorithm(dataset, test_set)
        #     print(predicted, '\n'*10)
        actual = [row[-1] for row in dataset]
        rmse = calcRMSE(actual, predicted)
        return (predicted, rmse)

    # Calculate the mean value of a list of numbers
    def mean(values):
        return np.sum(values) / float(len(values))

    # Calculate covariance between x and y
    def covariance(x, mean_x, y, mean_y):
        covar = 0.0
        for i in range(len(x)):
            covar += (x[i] - mean_x) * (y[i] - mean_y)
        return covar

    # Calculate the variance of a list of numbers
    def variance(values, mean):
        return sum([(x - mean) ** 2 for x in values])

    # Calculate coefficients
    def coefficients(dataset):
        x = [row[0] for row in dataset]
        y = [row[1] for row in dataset]
        x_mean, y_mean = calcMean(x), calcMean(y)
        b1 = calcCovariance(x, x_mean, y, y_mean) / calcVariance(x, x_mean)
        b0 = y_mean - b1 * x_mean
        return [b0, b1]

    # Simple linear regression algorithm
    def simple_linear_regression(train, test):
        predictions = list()
        b0, b1 = calcCoeffs(train)
        for row in test:
            yhat = b0 + b1 * row[0]
            predictions.append(yhat)
        return predictions

    # Test simple linear regression
    dataset = [[1, 1], [2, 3], [4, 3], [3, 2], [5, 5]]
    predicted, rmse = evaluate_algorithm(dataset, simple_linear_regression)
    print(f'Predicted: {predicted}', '\n' * 5)
    print('RMSE: %.3f' % (rmse))

    ######

   


########

# Example of Simple Linear Regression on the Swedish Insurance Dataset
from random import seed
from random import randrange
from csv import reader
from math import sqrt


def trainTestSplit(data, split):  # writing the training-testing set splitting algorithm from scratch
    openData = data['Open']
    train = list()
    trainSize = split * len(openData)
    copiedDataList = list(openData)
    while len(train) < trainSize:
        index = randrange(len(copiedDataList))
        train.append(copiedDataList.pop(index))
    return train, pd.Series(copiedDataList)

# split dataset into k folds
# def cvSplit(dataset, folds=5): # cross-validation split by method of k-fold cross-validation, default # folds is 5
#     splitData = list()
#     copiedDataList = list(dataset)
#     foldGap = int(len(dataset)/folds)
#     for _ in range(folds):
#         fold = list()
#         while len(fold) < foldGap:
#             index = randrange(len(copiedDataList))
#             fold.append(copiedDataList.pop(index))
#         splitData.append(fold)
#     return pd.Series(splitData)

##########