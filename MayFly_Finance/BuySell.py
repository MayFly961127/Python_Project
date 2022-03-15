taken = ['CPAC', 'SXC', 'ASC', 'BSBR']
import numpy as np
for i in taken:
  df_stock = pdr.get_data_yahoo(i)
  df_close = df_stock['Close']
  close = np.reshape(df_close.to_numpy(),len(df_close))
  t_2 = close[-3] - close[-2]
  t_1 = close[-2] - close[-1]
  if t_2*t_1 < 0:
    print('Sell 2 or 3 stocks')
  else:
    print('Buy or Keep')