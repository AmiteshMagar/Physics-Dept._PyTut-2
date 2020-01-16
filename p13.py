def simpson(a,b,n,func):
    h= (b-a)/n
    print("This is h " +str(h))
    step = a + h
    fa= func(a)
    fb= func(b)
    h1= h/3
    su = (fa + fb)
    for i in range(n-1):
        if i%2==0:
            su= su + (4*func(step))
        else:
            su = su + (2*func(step))
        step = step + h
    return (su * h1)

#Testing simpson
'''
def func(x):
    y= 2*x - 5
    return y
a = 2
b=5
n=[50,100,500,1000]
for k in n:
    print(simpson(a,b,k,func))
'''
