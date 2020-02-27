# Plot-Bollinger-Bands
Bollinger Bands are a financial analysis technique for indicating trend reversals. These bands are calculated by calculating a moving average based on historical data, and then subtracting 2 standard deviations of the price from the moving average. When the adjusted close is above the upper band, it can signal a trend reversal. There are also many other interpretations of Bollinger Bands, this project simply provides a way to easily visualize a stock ticker's 10-day moving average, adjusted close, upper and lower bollinger bands.

# Requirements
This program requires the following libraries to work: matplotlib, numpy, pandas

# Limitations
This program is hardcoded to use a 10-day moving average, which means it is limited to short to medium term financial analysis. More changes would be needed in order to improve the user experience such as entering the time period for the moving average, etc. Also, boillinger bands can only estimate trend reversal's and there are much higher level financial analysis techniques that are more accurate. The date on the x-axis can also overlap if the time period is too small 

# This project was based on Bernard Brenyah's tutorial and was tweaked for the purpose of making it easier for the user to use:
https://medium.com/python-data/setting-up-a-bollinger-band-with-python-28941e2fa300
