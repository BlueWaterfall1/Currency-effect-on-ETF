# Currency-effect-on-ETF
This code simulates the potential gain of certain ETFs with underlying assets in different currencies, based on their historical performance and the potential variation of currency values against the dollar.
# Assumptions:
Exchange fees are ignored (reasonable since there are brokers with very low currency conversion costs, like Interactive Brokers).
Currencies are assumed to return to their historical average (reasonable, as only currencies from developed countries are chosen).
When buying an ETF, all currency conversions are assumed to happen instantly (so we don’t consider the currency in which the ETF is traded).

# Choice of indices and ETFs:
This simulator is mainly for personal use, so it prioritizes options suited for European investors (preference for accumulating ETFs, UCITS, etc.).
I chose the 5 currencies most represented in the MSCI World index.
I chose the S&P 500 for the United States and the FTSE 100 for the UK because they are the most popular, meaning more liquid funds and lower ETF fees in general.
For Japan, I chose MSCI Japan instead of the Nikkei 225 because the Nikkei 225 is a price-weighted equity index, which seemed less relevant.
For Canada, I chose MSCI Canada instead of the S&P/TSX Composite because the latter is not very accessible for European investors.
For Europe, I chose the Euro Stoxx 50 because the Stoxx Europe 600 includes countries whose currencies are not the euro, which is an issue given the simulator’s objective.
I try to choose ETFs with large fund size (>100M), low fees, and accumulating structure, but I have to make compromises because some ETFs have limited data available on Yahoo Finance.

# Attention:
To calculate the historical performance, the maximum number of years that can be considered is 10, due to limited data for the MSCI Canada ETF. However, since markets have performed particularly well over the past 10 years, the projections should be taken as indicative only.
This project is for educational and personal purposes only. The results do not constitute any investment advice.
