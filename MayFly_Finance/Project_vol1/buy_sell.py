 def buy_sell(list):
  import pandas_datareader as pdr
  import yfinance as yfin
  import numpy as np
  yfin.pdr_override()
  selected_stocks = list
  n = len(selected_stocks)
  for i in range(n):
    df_stock = pdr.get_data_yahoo(selected_stocks[i])
    price = df_stock['Close']
    price = np.reshape(price.to_numpy(),len(price))
    t_2 = price[-3] - price[-2]
    t_1 = price[-2] - price [-1]
    if t_2*t_1 < 0:
      print('Sell: ' + selected_stocks[i])
    else:
      print('Keep or buy: ' + selected_stocks[i])