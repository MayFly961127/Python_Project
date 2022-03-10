def RS(nu, de, start, end, step, trial):
    """nu is numerator for RS, and de is denominator for RS and step is moving average step. Finally trial is the nuber of polynomials that we can try"""

    from pandas_datareader import data as pdr
    import yfinance as yfin
    import numpy as np
    import matplotlib.pyplot as plt
    from sklearn.metrics import mean_squared_error
    from IPython.display import display
    yfin.pdr_override()

    # Getting Time
    if start == 'begin' and end == 'now':
        df_nu = pdr.get_data_yahoo(nu)
        df_de = pdr.get_data_yahoo(de)
    elif start == 'begin' and end != 'now':
        df_nu = pdr.get_data_yahoo(nu, end=end)
        df_de = pdr.get_data_yahoo(de, end=end)
    elif start != 'begin' and end == 'now':
        df_nu = pdr.get_data_yahoo(nu, start=start)
        df_de = pdr.get_data_yahoo(de, start=start)
    else:
        df_nu = pdr.get_data_yahoo(nu, start=start, end=end)
        df_de = pdr.get_data_yahoo(de, start=start, end=end)

    # Organiziang index
    df_nu = df_nu.reset_index()
    df_de = df_de.reset_index()
    latest = df_nu['Close'].tail(3)
    display(latest)

    # Sorting Data
    n = len(df_nu)
    df_date = df_nu['Date'].dt.strftime('%Y-%m-%d')
    df_date = np.reshape(df_nu[['Date']].to_numpy(), n)
    df_date = df_date.astype('datetime64[D]')
    df_nu = np.reshape(df_nu[['Close']].to_numpy(), n)
    df_de = np.reshape(df_de[['Close']].to_numpy(), n)
    x_data = np.arange(0, n, 1)

    # Make Relative Strength
    df_rs = df_nu / df_de

    # Make a curve fitting model
    def eval(x_data, p):
        import numpy as np
        n = len(x_data)
        m = len(p)
        sum_poly = []
        for i in range(n):
            poly = []
            for j in range(m):
                polynomials = p[j] * x_data[i] ** j
                poly.append(polynomials)
            sum_poly.append(np.sum(poly))
        return sum_poly

    model_nu = []
    model_rs = []
    for coef in range(trial):
        trial_nu = np.poly1d(np.polyfit(x_data, df_nu, coef))
        trial_rs = np.poly1d(np.polyfit(x_data, df_rs, coef))
        eval_nu = eval(x_data, trial_nu)
        eval_rs = eval(x_data, trial_rs)
        error_nu = mean_squared_error(df_nu, eval_nu)
        error_rs = mean_squared_error(df_rs, eval_rs)
        print(coef, 'th polynomials has', error_nu, 'in error_nu.',
              coef, 'th polynomials has', error_rs, 'in error_rs.\n')

    a = input("which power would you choose for stock: ")
    b = input("which power would you choose for RS: ")
    model_nu = np.poly1d(np.polyfit(x_data, df_nu, int(a)))
    model_rs = np.poly1d(np.polyfit(x_data, df_rs, int(b)))
    y_stock = eval(x_data, model_nu)
    y_rs = eval(x_data, model_rs)

    # Moving Average
    mv_stock = []
    mv_rs = []
    mv_step = step
    i = 0
    while i < n - mv_step + 1:
        window_stock = y_stock[i: i + mv_step]
        window_rs = y_rs[i: i + mv_step]
        mv_stock.append(round(sum(window_stock) / mv_step, 5))
        mv_rs.append(round(sum(window_rs) / mv_step, 5))
        i += 1

    # Make mv_date
    m = len(mv_stock)
    mv_x = x_data[step - 1:]

    # Visualize

    canvas = plt.figure(figsize=(30, 15))
    stock_plot = canvas.add_subplot(421)
    stock_plot.plot(mv_x, mv_stock, '-k', label='MV_' + str(step))
    stock_plot.plot(x_data, df_nu, 'ob', label='Real_Data')
    plt.xticks(x_data[::30], df_date[::30], rotation=45)
    plt.plot(x_data, y_stock, '-r', label='Curve fitted')
    plt.title(nu)
    plt.grid()
    plt.axis('tight')
    plt.legend()

    rs_plot = canvas.add_subplot(423)
    rs_plot.plot(mv_x, mv_rs, '-k', label='MV_' + str(step))
    rs_plot.plot(x_data, df_rs, 'oy', label='Real_data')
    rs_plot.plot(x_data, y_rs, '-g', label='Curve fitted')
    plt.xticks(x_data[::30], df_date[::30], rotation=45)
    plt.title('RS' + '(' + nu + '/' + de + ')')
    plt.grid()
    plt.axis('tight')
    plt.legend()
    canvas.tight_layout()
    plt.show()
