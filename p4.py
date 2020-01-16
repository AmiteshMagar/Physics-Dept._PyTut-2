def bisect(a,b,func):
    fa = func(a)
    fb = func(b)
    flag = 0
    if (fa*fb)<0:
        print("Bisection method is possible")
    else:
        return "Bisection method is not possible"
    mean = (a + b)/2
    
    if abs(a)>abs(b):
        a,b=b,a
    fa = func(a)
    fb  =func(b)
    if fa>0 and fb<0:
        a,b=b,a
    #print(mean)
    for i in range(10000):
        fMean = func(mean)
        last = 0
        if fMean>0:
            last = b
            b= mean
        elif fMean<0:
            last = a
            a=mean
        elif fMean==0:
            return mean
        mean = (a+b)/2
        if abs(last-mean)<1e-5:
            flag = 1
    if flag == 0:
        print("after 10000 iterations, we could not achieve convergence")
    else:
        return last

