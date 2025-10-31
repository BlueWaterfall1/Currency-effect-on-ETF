import yfinance as yf
from datetime import datetime
from dateutil.relativedelta import relativedelta
import matplotlib.pyplot as plt

tickers = ["CUKX.L","CSCA.AS","DBXJ.DE","XESC.DE","SXR8.DE"]
currencies = ["GBPUSD=X","CADUSD=X","JPYUSD=X","EURUSD=X"]
currencies_names = ["GBP","CAD","JPY","EUR","USD"]

while True:  # allow the user to choose the number of years to consider for the historical data
    try:
        years_etf = int(input("Over how many years would you like to calculate the ETF's annualized return?(max 10 years):"))
        if 1 <= years_etf <= 10:
            break
        else:
            print("Please enter a number between 1 and 10.")
    except:
        print("Please enter a valid integer.")

while True:
    try:
        years_currency = int(input("Over how many years would you like to assume that the currency returns to its average level?(max 21 years):"))
        if 1 <= years_currency <= 21:
            break
        else:
            print("Please enter a number between 1 and 21.")
    except:
        print("Please enter a valid integer.")
        
while True:
    try:
        years_return = int(input("Over how many years do you assume that the currencies will return to their historical average?(max 40 years):"))
        if 1 <= years_return <= 40:
            break
        else:
            print("Please enter a number between 1 and 40.")
    except:
        print("Please enter a valid integer.")

today = datetime.today()
start_etf = today-relativedelta(years=years_etf)
start_currency = today-relativedelta(years=years_currency)

returns = []
ratios = []

for ticker in tickers:   # calculate the historical performance
    data_etf = yf.download(ticker,start_etf,today)    
    prices = list(data_etf["Close"][ticker])
    first_price = prices[0]
    last_price = prices[-1]
    perf = (last_price/first_price)**(1/years_etf) - 1
    returns.append(perf)
    
for currency in currencies:  # calculate the ratio between the currency’s current value and its historical average
    data_currency = yf.download(currency,start_currency,today)
    exchange_rates = list(data_currency["Close"][currency])
    average_rate = sum(exchange_rates)/len(exchange_rates)
    current_rate = exchange_rates[-1]
    ratio = current_rate/average_rate
    ratios.append(ratio)

ratios.append(1)     # add usd
        
etf_perf = []
comparison = []

for i in range(len(returns)):
    perf2 = (1+returns[i])**years_return * (1/ratios[i]) - 1
    etf_perf.append(perf2)
    comparison.append((1+returns[i])**years_return - 1)
    
etf_sorted = sorted(zip(etf_perf,currencies_names),reverse=True)
etf_perf_sorted,etf_names_sorted = zip(*etf_sorted)
comparison_sorted = sorted(zip(comparison,currencies_names),reverse=True)
comparison_perf_sorted,comparison_names_sorted = zip(*comparison_sorted)

plt.figure(figsize=(12,5))   # plot the histograms in descending order of values
plt.bar(etf_names_sorted, etf_perf_sorted, color='blue')
for i,value in enumerate(etf_perf_sorted):
    plt.text(i,value+0.003,f"{value*100:+.1f}%",ha='center',va='bottom')
plt.ylabel("Performance")
plt.title("Performance including currency effects")
plt.show()

plt.figure(figsize=(12,5))
plt.bar(comparison_names_sorted, comparison_perf_sorted, color='green')
for i,value in enumerate(comparison_perf_sorted):
    plt.text(i,value+0.003,f"{value*100:+.1f}%",ha='center',va='bottom')
plt.ylabel("Performance")
plt.title("Performance excluding currency effects")
plt.show()
