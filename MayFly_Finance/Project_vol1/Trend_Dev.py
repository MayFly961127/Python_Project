import numpy as np
import pandas as pd
import yfinance as yfin
import pandas_datareader as pdr
import matplotlib.pyplot as plt
def Trend_Dev(index, stock, step, step_sub, step_sub_sub):
    # stock = input("Enter the ACT symbol of the stock ")
    # step = int(input("Enter the months for trend Dev "))
    # step_sub = int(input("Enter the sub months for trend Dev "))
    # step_sub_sub = int(input("Enter the MV for the trend Dev "))
    list_index = ['Dow','^DJI',
                  '\nS&P','GSPC',
                  '\nNAS','^IXIC']
    print(list_index)
    print('Trend_dv_dn ', step)
    print('Trend_dv_nu ', step_sub)
    print('Trend_dv_MV', step_sub_sub)
    def MV(stock, step):
        mv_step = step
        mv_stock = []
        n = len(stock)
        i = 0
        while i < n - mv_step + 1:
            window_stock = stock[i: i + mv_step]
            mv_stock.append(round(sum(window_stock) / mv_step, 5))
            i += 1
        return mv_stock

    yfin.pdr_override()
    index_choosen = index
    df_SOFI = pdr.get_data_yahoo(stock, start = '1900-01-01')
    df_SOFI = df_SOFI.reset_index()
    Date_latest_stock = df_SOFI['Date']
    Date_latest_stock = Date_latest_stock.to_numpy()[0]
    df_SP = pdr.get_data_yahoo(index_choosen, start = Date_latest_stock)
    df_SP = df_SP.reset_index()
    if len(df_SOFI) > len(df_SP):
        df_SOFI = df_SOFI[-len(df_SP):]
        stock_close = df_SOFI['Close']
        sp_close = df_SP['Close']
        stock_close = np.reshape(stock_close.to_numpy(), len(df_SP))
        sp_close = np.reshape(sp_close.to_numpy(), len(df_SP))
    else:
        df_SP = df_SP[-len(df_SOFI):]
        stock_close = df_SOFI['Close']
        sp_close = df_SP['Close']
        stock_close = np.reshape(stock_close.to_numpy(), len(df_SOFI))
        sp_close = np.reshape(sp_close.to_numpy(), len(df_SOFI))
    #This is what need
    rs_close = stock_close/sp_close
    Date = df_SOFI['Date'].dt.strftime('%Y-%m-%d')
    Date = np.reshape(Date.to_numpy(),len(Date))

    #MV
    step = step*30
    step_sub = step_sub*30
    step_sub_sub = step_sub_sub*30
    Trend_dv_de = MV(stock_close, step)
    Trend_dv_de = np.array(Trend_dv_de)
    m = len(Trend_dv_de)
    Trend_dv_nu = MV(stock_close, step_sub)
    Trend_dv_nu = Trend_dv_nu[-m:]
    Trend_dv_nu = np.array(Trend_dv_nu)
    Trend_dv_MV = MV(stock_close, step_sub_sub)
    Trend_dv_MV = Trend_dv_MV[-m:]

    Trend_dv = Trend_dv_de/Trend_dv_nu
    #plot the stock
    Date_trend = Date[-m:]
    x_close = np.linspace(0,len(Date_trend),len(Date_trend))
    x_trend = x_close[-m:]
    plt.figure(figsize = (12,4))
    plt.plot(x_close, stock_close[-m:])
    split = int(len(x_close)**(3/4))
    plt.xticks(x_close[::split], Date_trend[::split], rotation = 45)
    plt.title(stock)
    plt.grid()
    plt.show()
    #plot the RS
    plt.figure(figsize = (12,4))
    plt.plot(x_close, rs_close[-m:])
    plt.xticks(x_close[::split], Date_trend[::split], rotation = 45)
    plt.title('RS with nasdaq: ' + str(stock))
    plt.grid()
    plt.show()

    #plot the result
    fig, ax = plt.subplots(figsize = (12,4))
    ax.plot(x_trend, Trend_dv, '-r' ,label = 'Trend_Dev')
    ax2 = ax.twinx()
    ax2.plot(x_trend,Trend_dv_MV, '--k', label = 'MV_' + str(step_sub_sub/30))
    split_trend = int(len(x_trend)**(3/4))
    ax.set_xticks(x_trend[::split_trend])
    ax.set_xticklabels(Date_trend[::split_trend], rotation = 45)
    plt.title('Trend Deviation')
    fig.legend()
    plt.show()