def newtraph(x0,func,deri):
    last = 0
    flag = 0
    for i in range(10000):
        error = func(x0)/deri(x0,func)
        last = x0
        if abs(error)<1e-5:
            return last
        x0 = last - error
    if flag==0:
        return "we could not achieve convergence after 10000 iterations"

def func(x):
    y = x**2 - 6
    return -y
def deri(x,func):
    f = func( x + 1e-5)
    s = func(x)
    d = (f - s)/1e-6
    return d
x0 = int(input())
print(newtraph(x0,func,deri))
