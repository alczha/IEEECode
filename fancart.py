from __future__ import division
from visual import *

# Constants
mcart = 0.3356 #mass in kg

#Objects
track = box(pos=vector(0, -0.05, 0), size=vector(2.0, 0.05, 0.10), color=color.white)
cart = box(pos=vector(-.023, 0, 0), size=vector(0.1, 0.04, 0.06), color=color.red)

#Initial Conditions
vcart=vector(-0.142, 0.416, 0)
pcart = mcart*vcart
print("cart momentum=", pcart)

deltat = 0.01
t = 0

#Calculation Loop
Fair = vector(-.104, 0, 0)
while t <4.01:
    pcart = pcart + Fair*deltat
    vcart = pcart/mcart
    cart.pos = cart.pos + vcart*deltat
    #print("the pos is now",cart.pos)
    t = t + deltat
    #print("after the loop")
    rate(100)
print(cart.pos)
print(vcart)
