#Made by: Amitesh

import math
'''from p6 import secant'''
#apparently import statement doesn't work in this case
# because the functoin in p6 take only 1 value for computation,
#but our function takes in 3 values
#To avoid editig the previous program I will be wirting different ways solve using THIS function

#This is the funtion that takes the value of alpha to check
def func(a,v0,h):
    const = math.sqrt((2*9.8*h)/(v0**2))
    sol = math.sin(a) - const
    return sol

#testing func -- works perfectly
'''print(func(math.pi/4,20,10))'''
#Secant solution -- Works perfectly!!
#remove the multi-line-comment apostrophes
'''
def secant(x0,v,h,func):
    y0 = x0 + (math.pi/8) #Minor correction
    fx = func(x0,v,h)
    fy = func(y0,v,h)
    flag = 0
    for i in range(10000):
        yf = y0 - (fy*((y0 - x0)/(fy-fx)))
        if abs(yf - y0)<1e-5:
            flag = 1
            return yf
        x0 = y0
        y0 = yf
        fx = fy
        fy = func(y0,v,h)
    if flag == 0:
        return "We could not reach convergence after 10000 iterations"

a = math.pi/4
h = float(input("Enter the height"))
v = float(input("enter the velocity"))

def conv(rad):
    deg= rad * 180 / math.pi
    return deg
print(conv(secant(a,v,h,func)))
'''

#Newton - Raphson technique -- Works Perfectly!!
'''
def newtraph(x0,v,h,func,deri):
    last = 0
    flag = 0
    for i in range(10000):
        error = func(x0,v,h)/deri(x0,v,h,func)
        last = x0
        if abs(error)<1e-5:
            return last
        x0 = last - error
    if flag==0:
        return "we could not achieve convergence after 10000 iterations"
def deri(x,v,h,func):
    f = func( x + 1e-5,v,h)
    s = func(x,v,h)
    d = (f - s)/1e-6
    return d

#Regular block
a = math.pi/4
h = float(input("Enter the height"))
v = float(input("enter the velocity"))

def conv(rad):
    deg= rad * 180 / math.pi
    return deg
print(conv(newtraph(a,v,h,func,deri)))
'''
#Bisection takes in two values and they must have positive and negative
#return made by the functoin
#in simple words, its a headache going after bisection adn seeing our sin is always positive
#beacuse we are dealing with the first quadrant, Bisection cannot be applied
