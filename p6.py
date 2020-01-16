def secant(x0,func):
    y0 = x0 + 0.1
    fx = func(x0)
    fy = func(y0)
    flag = 0
    for i in range(10000):
        yf = y0 - (fy*((y0 - x0)/(fy-fx)))
        if abs(yf - y0)<1e-5:
            flag = 1
            return yf
        x0 = y0
        y0 = yf
        fx = fy
        fy = func(y0)
    if flag == 0:
        return "We could not reach convergence after 10000 iterations"

