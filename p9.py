#Lets use import this time
import p8

def subRout(n,Lx,Ly,m,Lxi):
    Lyi = []
    for i in range(m):
        Lyi.append(p8.Lagrange(n,Lx,Ly,Lxi[i]))
    return Lyi
#Testing Subroutine -- Works perfectly!
'''
Lx = [2,3]
Ly = [5,4]
n = 2
m=3
Lxi = [1,6,5]
print(subRout(n,Lx,Ly,m,Lxi))
'''
