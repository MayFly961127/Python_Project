import numpy as np
from pandas_datareader import data as pdr
import yfinance as yfin
import pandas as pd
yfin.pdr_override()
#import all stocks name
df = pd.read_csv('https://pkgstore.datahub.io/core/nyse-other-listings/nyse-listed_csv/data/3c88fab8ec158c3cd55145243fe5fcdf/nyse-listed_csv.csv')
df = df['ACT Symbol']
m = len(df)
prob = []
#Save Close and name of equity that satisfies the condition
close = []
stock = []

for j in range(10):
  df_Stock = pdr.get_data_yahoo(df[j])
  price = df_Stock['Close']
  n = len(price)
  price = price.to_numpy()
  price = np.reshape(price,n)
  try:
    if price[-1]*price[-2] > 0 and price[-1] < 50:
      #If the theorem is right, go to true box, otherwise go to false box
      true_box = []
      false_box = []
      try:
        for i in range(n):
          try:
            #t-2 is the day before yesterday, t-1 is yesterday, and t-0 is today
            t_2 = price[i] - price[i+1]
            t_1 = price[i+2] - price[i+1]
            mul_12 = (t_2)*(t_2)
            t_0 = price[i+3] - price[i+2]
            if mul_12 > 0:
              if t_0 > 0:
                true_box.append(1)
              else:
                false_box.append(0)
            elif mul_12 < 0:
              if t_0 < 0:
                true_box.append(1)
              else:
                false_box.append(0)
          except IndexError:
            break
        Probability = len(true_box)/(len(true_box) + len(false_box))
      except ZeroDivisionError:
        continue
      if Probability > 0.5:
        stock.append(df[j])
        close.append(price[-1])
        prob.append(Probability)
        k = round((j+1)*100/10,2)
        print(k,'%')
  except IndexError:
    continue

df_PotenStock = pd.DataFrame({'Stock': stock, 'Close': close, 'Porb': prob})
file_name = input('input file name')
df_PotenStock.to_csv(file_name)