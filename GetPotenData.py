import numpy as np
from pandas_datareader import data as pdr
import yfinance as yfin
import pandas as pd
yfin.pdr_override()
#import all stocks name
df = pd.read_csv('https://pkgstore.datahub.io/core/nyse-other-listings/nyse-listed_csv/data/3c88fab8ec158c3cd55145243fe5fcdf/nyse-listed_csv.csv')
df_name = df['ACT Symbol']
m = len(df)
prob = []
#Save Close and name of equity that satisfies the condition
close = []
stock = []

for j in range(m):
  start_date = '2022-01-01'
  df_Stock = pdr.get_data_yahoo(df_name[j], start = start_date)
  price = df_Stock['Close']
  n = len(price)
  price_limit = 100 #dollars

  #For index error
  try:
    if price[-1]*price[-2] > 0 and price[-1] < price_limit:
      #If the theorem is right, go to true box, otherwise go to false box
      true_box = []
      false_box = []
      #for ZeroDivision error
      try:
        true_val = 0
        false_val = 0
        for i in range(n):
          #Index error
          try:
            #t-2 is the day before yesterday, t-1 is yesterday, and t-0 is today
            t_2 = price[i] - price[i+1]
            t_1 = price[i+2] - price[i+1]
            mul_12 = (t_2)*(t_2)
            t_0 = price[i+3] - price[i+2]
            if mul_12 > 0:
              if t_0 > 0:
                true_val += 1
              else:
                false_val += 1
            elif mul_12 < 0:
              if t_0 < 0:
                true_val += 1
              else:
                false_val += 1
          except IndexError:
            break
        Probability = true_val/(true_val + false_val)
      except ZeroDivisionError:
        continue
      if Probability > 0.5:
        stock.append(df_name[j])
        close.append(price[-1])
        prob.append((Probability*100 - 50)**(3/2))
        k = round((j+1)*100/m,2)
        print(k,'%')
  except IndexError:
    continue
df_PotenStock = pd.DataFrame({'Stock': stock, 'Close': close, 'Value': prob})
file_name = input("Decide your csv file name ")
df_PotenStock.to_csv(file_name)