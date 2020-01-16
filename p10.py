def subRout10(n,Lx,Ly):
    LyPrime = []
    #this for us to compute the last value
    Lx.append(Lx[0])
    Ly.append(Ly[0])
    for i in range(n):
        calc= (Ly[i+1] - Ly[i])/(Lx[i+1] - Lx[i])
        LyPrime.append(calc)
    Ly.pop(len(Ly)-1)
    return LyPrime

#testing subRout10 -- works perfectly!
'''
Lx =[2,5,3]
Ly=[5,4,8]
n=3
print(subRout10(n,Lx,Ly))
'''
