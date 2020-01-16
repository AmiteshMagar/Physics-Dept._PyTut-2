import p9
import p10

def subRout11(n,Lx,Ly,m):
    #First generate the array x1
    Lx1= []
    for i in range(1,n+1):
        calc = Lx[0] + ((i-1)*(Lx[n-1]-Lx[0]))/m
        Lx1.append(calc) #exit loop
    #we now have the X1 array
    #lets generate the Y1 array using p9 module
    Ly1 = p9.subRout(n,Lx,Ly,n,Lx1)
    #lets use the p10 program to generate yPrime array
    #it will be tking n, Lx1, Ly1
    LyPrime =[]
    LyPrime = p10.subRout10(n,Lx1,Ly1)
    return LyPrime, Ly1

#testing p11 -- Well this works, but dont know if correct
#please verify the formula with hand calculations before proceeding
'''
n = 2
Lx =[2,3]
Ly = [5,4]
m=2
print(subRout11(n,Lx,Ly,m))
'''
