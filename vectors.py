from __future__ import division
from visual import *

baseball = sphere(pos=vector(-4,-2,5), radius=0.40, color=color.red)
tennisball = sphere(pos=vector(3,1,-2), radius=0.15, color=color.green)

bt = arrow(pos=vector(baseball.pos), axis=vector(tennisball.pos-baseball.pos), color=color.cyan)
arrow.x = arrow(pos=vector(baseball.pos), axis=vector(bt.axis.x,0,0), color=color.red)
arrow.y = arrow(pos=vector(baseball.pos), axis=vector(0,bt.axis.y,0), color=color.red)
arrow.z = arrow(pos=vector(baseball.pos), axis=vector(0,0,bt.axis.z), color=color.red)

print(tennisball.pos - baseball.pos)







       



