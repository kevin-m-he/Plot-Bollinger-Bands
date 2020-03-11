#import necessary libraries and modules
import pandas_datareader as pdr
import pandas as pd
import matplotlib.pyplot as plt
import datetime
from datetime import date, timedelta

#fix implicit datetime error
pd.plotting.register_matplotlib_converters()


def plotstock(ticker,n):
    #creates variable for today's date and subtracts however many days a user inputs
    today = date.today()
    time_frame = today - timedelta(n)
    
    newday = str(today)
    oldday = str(time_frame)
    
    #Get yahoofinance stock data and put into a dataframe
    df = pdr.get_data_yahoo(ticker.upper(),start=time_frame,end=today)
    
    #get the adj_close from the dataframe
    adj_close = df['Adj Close']
    
    #Create a new column in df, 10 day simple moving average and the standard deviation
    df['10 Day MA'] = adj_close.rolling(10).mean()
    df['10 Day MA STDEV'] = adj_close.rolling(10).std()
    moving_average = df['10 Day MA']
    
    #Make a column for upper and lower bollinger bands
    df['Upper Band'] = df['10 Day MA']+df['10 Day MA STDEV']*2
    df['Lower Band'] = df['10 Day MA']-df['10 Day MA STDEV']*2
    
    #get the index for the data frame
    dates = pd.Series(df.index)
    
    #Setup an empty matplotlib figure
    plt.style.use('bmh')
    fig = plt.figure(figsize=(12,6))
    ax = fig.add_subplot(111)
    
    #get index values
    x_axis = df.index.to_numpy()
    
    #Shade the area between the upper and lower bands
    ax.fill_between(x_axis,df['Upper Band'],df['Lower Band'],color='yellow')
    
    #Plot adjusted closing price and moving averages
    ax.plot(x_axis,df['Adj Close'],color='blue',lw=2)
    ax.plot(x_axis,df['10 Day MA'],color='black',lw=2)
    
    #plot dashed lines for upper and lower bands
    ax.plot(x_axis,df['Upper Band'],linestyle='dashed',color='grey')
    ax.plot(x_axis,df['Lower Band'],linestyle='dashed',color='grey')
    
    #setup titles and axis labels
    ax.set_title('10 Day Moving Average Bollinger Band For '+ticker.upper())
    ax.set_xlabel('Date')
    ax.set_ylabel('Price (USD)')
    labels = ['Adjusted Close','10 Day Moving Average']
    ax.legend(labels)
    
    return plt.show()

def main():
    #Have user input stock ticker and amount of days they want to go back
    while True:
        #make sure user inputs a stock ticker and not numbers
        ticker = input('Please enter the stock ticker of what you would like to plot:\n\n')
        try:
            x = int(ticker)
            print('Please enter a stock ticker with letters, not a number or decimal')
            print('_________________________________________________________________')
            continue
        except:
            pass
        try:
            x = float(ticker)
            print('Please enter a stock ticker with letters, not a number or decimal')
            print('_________________________________________________________________')
            continue
        except:
            break
    print('_________________________________________________________________')
    while True:    
        #make sure day amount is a number
        n = input('How long do you want to go back?\n\nPlease enter an amount of days:\n\n')
        try:
            y = int(n)
            break
        except:
            print('Please enter a number for the amount of days, not a decimal or word')
            print('_________________________________________________________________')
            continue

    plotstock(ticker,int(n))

if __name__ == '__main__':
    main()
