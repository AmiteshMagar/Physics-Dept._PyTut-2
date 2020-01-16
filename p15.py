import p12
def grav(y):
    R= 6.371e6
    num= 9.81 * (R)**2
    den = (y + R)**2
    g = num/den
    return 500*g

print(p12.integration(0,800000,1000,grav))
