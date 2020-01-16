import math
def gaussian(a,b,func):
    z1 = math.sqrt(5- 2*(math.sqrt(10/7)))
    z2 = math.sqrt(5 + 2*(math.sqrt(10/7)))
    Lzi = [0, (1/3)*z1, (-1/3)*z1,(1/3)*z2,(-1/3)*z2]
    w1 =(13*math.sqrt(70) + 322)/900
    w2 = (322 - 13*math.sqrt(70))/900
    Lwi = [ (128/225),w1,w1,w2,w2]
    pro = (b-a)/2
    add = (b+a)/2
    su =0
    for i in range(5):
        su = su + (Lwi[i]*func((pro * Lzi[i]) + add))
    return (su*pro)

#testing gaussian - works perfectly
'''
def func(x):
    y = 2*x - 5
    return y
a= 2
b= 5
print(gaussian(a,b,func))
'''
