from __future__ import division
from visual import *
from visual.graph import* #Invoke graphing routine
scene.y = 400 #Move orbit window below graph
scene.width=1024
scene.height=760


# CONSTANTS
G = 6.7e-11
mEarth = 6e24
mcraft = 15e3
#mMoon = 7e22
mMoon = 1
deltat = 60
t = 0
pscale = 0.5
fscale = 2000
dpscale = 25
Fnet_tangent_scale = 100000
Fnet_perp_scale = 100000



#OBJECTS AND INITIAL VALUES
Earth = sphere(pos=vector(0,0,0), radius=6.4e6, color=color.cyan)
Moon = sphere(pos=vector(4e8,0,0), radius=2.75e6, color=color.white)
scene.range=150*Earth.radius
pArrow = arrow(color=color.green)
fArrow = arrow(color=color.cyan)
dpArrow = arrow(color=color.red)
Fnet_tangent_arrow = arrow(color=color.yellow)
Fnet_perp_arrow = arrow(color=color.magenta)

r_EarthMoon = Moon.pos - Earth.pos
Moon.v = vector(0, sqrt((G*mEarth)/mag(r_EarthMoon)), 0)
momentum_Moon = Moon.v * mMoon
# Add a radius for the spacecraft. It should be BIG, so it can be seen.


craft = sphere(pos=vector(-73600000,-5120000,0),radius = 1000000, color=color.yellow)
vcraft = vector(-300,3180,0)
pcraft = mcraft*vcraft
#print("pcraft =", pcraft)
r = craft.pos-Earth.pos
rmag = sqrt((craft.pos.x-Earth.pos.x)**2+(craft.pos.y-Earth.pos.y)**2+(craft.pos.z-Earth.pos.z)**2)
Fmag = (G*mcraft*mEarth)/((rmag)**2)
rhat = r/rmag
Fnet = -Fmag*rhat
print("Fnet =", Fnet)

trail = curve(color=craft.color)
mtrail = curve(color=Moon.color)# This creates a trail for the spacecraft
scene.autoscale = 0                 # And this prevents zooming in or out

print("p=", pcraft)
print("Fnet=", Fnet)

# CALCULATIONS
U_graph = gcurve(color=color.blue)
K_graph = gcurve(color=color.yellow)
Energy_graph = gcurve(color=color.green)
while t <8640000:
    #scene.center=craft.pos
    #scene.range=craft.radius*60
    rate(10000) # This slows down the animation (runs faster with bigger number)
    r = craft.pos-Earth.pos
    rmag = mag(r)
    rhat = norm(r)
    r2 = craft.pos - Moon.pos
    r2mag = mag(r2)
    r2hat = r2/r2mag

    Fmearth = (G*mcraft*mEarth)/((rmag)**2)
    Fearth = -Fmearth*rhat
    FmMoon = (G*mcraft*mMoon)/((r2mag)**2)
    Fmoon = -FmMoon*r2hat
    Fnet = Fearth + Fmoon

    p_init = mag(pcraft)
    pcraft = pcraft + Fnet*deltat
    p_final = mag(pcraft)
    phat = pcraft/mag(pcraft)
    Fnet_tangent = ((p_final - p_init)*phat)/deltat

    Fnet_perp = Fnet - Fnet_tangent
    
    
    
    vcraft = pcraft/mcraft
    craft.pos = craft.pos + vcraft*deltat
    pArrow.pos = craft.pos
    pArrow.axis = pcraft*pscale

    Fnet_tangent_arrow.pos = craft.pos
    Fnet_tangent_arrow.axis = Fnet_tangent*Fnet_tangent_scale
    Fnet_perp_arrow.pos = craft.pos
    Fnet_perp_arrow.axis = Fnet_perp*Fnet_perp_scale

    K_craft = .5*mcraft * mag(vcraft)**2
    U_craft_Earth = (-G*mcraft*mEarth)/rmag
    U_craft_Moon = (-G*mcraft*mMoon)/r2mag
    E = K_craft + U_craft_Earth + U_craft_Moon

    U_graph.plot(pos=(t,U_craft_Earth+U_craft_Moon))
    K_graph.plot(pos=(t,K_craft)) 
    Energy_graph.plot(pos=(t,E))

    r_EarthMoon = Moon.pos - Earth.pos
    Force_EarthMoon = (-G*mEarth*mMoon)/((mag(r_EarthMoon))**2)*norm(r_EarthMoon)
    Force_craftMoon = Fmoon
    Fnet_Moon = Force_EarthMoon + Force_craftMoon

    momentum_Moon = Fnet_Moon*deltat + momentum_Moon
    Moon.v = momentum_Moon/mMoon
    Moon.pos = Moon.v*deltat + Moon.pos
    
    


    ##
    #pcraft_i = pcraft + vector (0,0,0)
    #pcraft = pcraft + Fnet*deltat
    #deltap = pcraft - pcraft_i

    #fArrow.pos = craft.pos
    #fArrow.axis = Fnet*fscale
    #dpArrow.pos = craft.pos
    #dpArrow.axis= deltap * dpscale

    # Add statements here for the iterative update of gravitational
    # force, momentum, and position. 


    # Uncomment these two lines to exit the loop if
    # the spacecraft crashes onto the Earth.

    if rmag < Earth.radius:
        break
    if r2mag < Moon.radius:
        break
    
    #if craft.pos.x > 10*Earth.radius:
        break

    trail.append(pos=craft.pos)
    mtrail.append(pos=Moon.pos)
    t = t+deltat

#print ("pcraft=", p_final)
#print("vcraft=", mag(vcraft))
#print("Fnet_perp=", mag(Fnet_perp))
#print("r=", mag(r))
print("final_pos=", craft.pos)
print("final_v=", vcraft)
print("Fgrav=", Fnet)
print("Fnet_tangent=",mag(Fnet_tangent))
print("Fnet_perp=", mag(Fnet_perp))

#print("craft.pos=", craft.pos)
#print("vcraft=", vcraft)    
#print("Calculations finished after ",t, "seconds")

