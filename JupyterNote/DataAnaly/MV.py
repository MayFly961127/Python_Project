def MV(stock, step):
    mv_step = step
    n = len(stock)
    mv_stock = []
    i = 0
    while i < n - mv_step + 1:
        window_stock = stock[i: i + mv_step]
        mv_stock.append(round(sum(window_stock) / mv_step, 5))
        i += 1
    return mv_stock