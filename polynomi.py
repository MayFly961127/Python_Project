def polynomi(x_data, p):
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