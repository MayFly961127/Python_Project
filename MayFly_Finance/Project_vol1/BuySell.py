import numpy as np
import pandas_datareader as pdr
import yfinance as yfin
import matplotlib.pyplot as plt
taken = ['SOFI', 'ITUB', 'BBD']
yfin.pdr_override()
start_date = '2022-01-01'
df_brent = pdr.get_data_yahoo('BZ=F', start = start_date)
df_SP = pdr.get_data_yahoo('^IXIC', start = start_date)
df_SP = df_SP.reset_index()
df_brent = df_brent.reset_index()
df_brent_close = df_brent['Close']
df_date = df_SP['Date']
df_date = df_date.dt.strftime('%Y-%m-%d')
df_SP = df_SP['Close']
brent_close = np.reshape(df_brent_close.to_numpy(),len(df_brent_close))
SP_close = np.reshape(df_SP.to_numpy(), len(df_SP))
RS_brent_SP = SP_close/brent_close
x_data = np.linspace(0, len(SP_close), len(SP_close))
date = np.reshape(df_date.to_numpy(),len(df_brent_close))

print(round(np.corrcoef(SP_close, brent_close)[0,1],2)*100, '%')
print(brent_close[-1])
#Plot brent VS Nasdaq
plt.figure(figsize = (10,6))
plt.plot(x_data, RS_brent_SP, 'g')
plt.title('Brent and Nasdaq')
plt.xticks(x_data[::10], date[::10], rotation = 45)
plt.show()
for i in taken:
  df_stock = pdr.get_data_yahoo(i, start = start_date)
  df_close = df_stock['Close']
  close = np.reshape(df_close.to_numpy(),len(df_close))
  RS_stock_SP = close/SP_close

  o_2 = brent_close[-2] - brent_close[-3]
  o_1 = brent_close[-1] - brent_close[-2]
  t_2 = close[-2] - close[-3]
  t_1 = close[-1] - close[-2]
  oil_factor = o_2*o_1

  if oil_factor >= 0:
    print('Not great: ' +  str(i))
    print('The day before: ', t_2, '\nYesterday: ', t_1)
  else:
    if t_2 * t_1 >= 0:
      print('Great: ' + str(i))
    else:
      print('Keep Eyes on' + str(i))
  plt.figure(figsize = (10,6))
  plt.plot(x_data, close, 'r')
  plt.title('Close_stock:' + str(i))
  plt.xticks(x_data[::10], date[::10], rotation = 45)
  plt.show()
  plt.figure(figsize = (10,6))
  plt.plot(x_data, RS_stock_SP, 'r')
  plt.title('RS stock with SP')
  plt.xticks(x_data[::10], date[::10], rotation = 45)
  plt.show()