from __future__ import division
from visual import *
scene.width=1024
scene.height=760


# CONSTANTS
G = 6.7e-11
mEarth = 6e24
mcraft = 15e3
deltat = 60
t = 0
pscale = 0.5
fscale = 2000
dpscale = 25


#OBJECTS AND INITIAL VALUES
Earth = sphere(pos=vector(0,0,0), radius=6.4e6, color=color.cyan)
scene.range=11*Earth.radius
pArrow = arrow(color=color.green)
fArrow = arrow(color=color.cyan)
dpArrow = arrow(color=color.red)
# Add a radius for the spacecraft. It should be BIG, so it can be seen.

craft = sphere(pos=vector(-7.552e07,-3.392e06,0),radius = 1000000, color=color.yellow)
vcraft = vector(110,2644,0)
pcraft = mcraft*vcraft
#print("pcraft =", pcraft)
r = craft.pos-Earth.pos
rmag = sqrt((craft.pos.x-Earth.pos.x)**2+(craft.pos.y-Earth.pos.y)**2+(craft.pos.z-Earth.pos.z)**2)
Fmag = (G*mcraft*mEarth)/((rmag)**2)
rhat = r/rmag
Fnet = -Fmag*rhat
print("Fnet =", Fnet)

trail = curve(color=craft.color)    # This creates a trail for the spacecraft
scene.autoscale = 0                 # And this prevents zooming in or out

print("p=", pcraft)
print("Fnet=", Fnet)

# CALCULATIONS
while t < 1860624:
    #rate(1000000) # This slows down the animation (runs faster with bigger number)
    r = craft.pos-Earth.pos
    rmag = sqrt((craft.pos.x-Earth.pos.x)**2+(craft.pos.y-Earth.pos.y)**2+(craft.pos.z-Earth.pos.z)**2)
    Fmag = (G*mcraft*mEarth)/((rmag)**2) 
    rhat = r/rmag
    Fnet = -Fmag*rhat
    pcraft_i = pcraft + vector (0,0,0)
    pcraft = pcraft + Fnet*deltat
    deltap = pcraft - pcraft_i
    vcraft = pcraft/mcraft
    craft.pos = craft.pos + vcraft*deltat
    pArrow.pos = craft.pos
    pArrow.axis = pcraft*pscale
    fArrow.pos = craft.pos
    fArrow.axis = Fnet*fscale
    dpArrow.pos = craft.pos
    dpArrow.axis= deltap * dpscale
   
    


    # Add statements here for the iterative update of gravitational
    # force, momentum, and position. 


    # Uncomment these two lines to exit the loop if
    # the spacecraft crashes onto the Earth.
    if rmag < Earth.radius:
    #if craft.pos.x > 10*Earth.radius:
        break

    trail.append(pos=craft.pos)  
    t = t+deltat

print("craft.pos=", craft.pos)
print("vcraft=", vcraft)    

print("Calculations finished after ",t, "seconds")
