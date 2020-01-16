def Lagrange(n,Lx,Ly,x):
    su =0
    pro = 1
    for i in range(n):
        for j in range(n):
            if i!=j:
                pro =pro * ((x-Lx[j])/(Lx[i]-Lx[j]))
        su =su + (Ly[i] * pro)
        pro = 1
    return su
#Test lagrange -- Works perfectly
'''
lx = (2,3)
ly=(5,4)
x = 6
n =2
print(Lagrange(n,lx,ly,x))
'''
