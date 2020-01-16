def integration(a,b,n,func):
    h  =  (b-a)/n
    step = a+h
    fa = func(a)
    fb = func(a +h)
    su = 0
    for i in range(n):
        su = su + (0.5*h*(fb + fa))
        fa = fb
        #a = b
        step = step + h
        fb = func(step)
    return su
#testing integration -- working perfectly
'''
def func(x):
    y= 2*x - 5
    return y
a = 2
b=5
n=[50,100,500,1000]
for k in n:
    print(integration(a,b,k,func))
'''
