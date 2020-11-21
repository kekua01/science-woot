GlowScript 2.6 VPython



angle = 4.2
k = .135
springL = .19
stringL = .05
ramplength = rl = 2.27
ramp2length = rl2 = 1.90
distance_from_cliff = d = 1.255
mass_of_red_cart = m_r = (1.25259)
mass_of_blue_cart = m_b = (.50651)
mass_of_wooden_block = m_wb = .14
mu = .208
cart_length = cartL = .16
theta = (angle * pi) / 180
scene = display(width=600,height=400,center = vec(0,0,0))
scene.range = 1.7
scene.autoscale = False
scene.background = vec(1,1,1)
c = Math.cos(theta) 
s = Math.sin(theta)
g = 9.8
M = m_r + m_b + m_wb

Fpull = abs(g * m_r * cos((pi/2)- theta))
springstretch = k * Fpull
springL = springL + springstretch



###math:
vF = sqrt((2*mu*g*m_wb*d) / M)
vI = (vF * M) / m_r
E = .5 * M * (vI**2)
h = E / (g*M)

L = h / sin(theta)

ramp1 = box(pos = vec(-1.3,-.4,0), size = vec(rl, .05, .2), axis = vec(c,-s,0), color = vec(.85,.85,.85), shininess = vec(0,0,0) )
ramp2 = box(size = vec(rl2,.05,.2), pos=vec (ramp1.pos.x +((c*rl)/2) + ((rl2)/2),ramp1.pos.y- ((s*rl)/2) ,0 ),color = vec(.85,.85,.85))
center = ramp2.pos.x-(ramp2.size.x/2)





RCARpos = vec(center - (L*c), ramp2.pos.y+(.07/2)+(ramp2.size.y/2) + (L*s),0)
RCAR = box(pos= RCARpos, size = vec(cartL, .07, .1), color = vec(1,0,0), axis = vec(c,-s,0) )
scene.camera.follow(RCAR)
block = box(size = vec(.15,.07,.1), color=vec(0,0,0), pos=vec((ramp2.pos.x + ((ramp2.size.x)/2))-d -((cartL)/2),ramp2.pos.y+(ramp2.size.y/2)+(.07/2),0))
BCAR = box(size = vec(cartL,.07,.1), color=vec(0,0,1), pos=vec(block.pos.x-(block.size.x/2)-(cartL/2),block.pos.y,0))

dd = stringL + (cartL/2)
ddd = springL + (cartL/2) + stringL
spring = helix(pos = vec(RCAR.pos.x-(c*ddd),RCAR.pos.y+(s*ddd)+.05-(.07/2),0), axis = vec(springL*c,-springL*s,0), radius = .05, coils= 10, color = vec(0,0,0))
string = curve(pos=[vec(RCAR.pos.x-(c*dd),RCAR.pos.y+(s*dd),0), vec(RCAR.pos.x-(c*cartL/2), RCAR.pos.y+(s*.07),0)],color = color.cyan, radius = .006)
###box(pos=vec(ramp2.pos.x+(ramp2.size.x/2) - (d/2), 0,0), size = vec(d, .01,.01), color = vec(0,1,1))

t = 0
deltat = .0001
while t < .1:
  rate(1000)
  t = t + deltat
t = 0

Fg_red = vec(0,-m_r * g, 0)
Fnetval = abs(g * m_r * cos((pi/2)- theta))
Fnet = Fnetval * vec(c,-s,0)
a = Fnet / m_r
v = vec(0,0,0)
while RCAR.pos.x < center:
  rate(10000)
  v = v + (a*deltat) 
  RCAR.pos.x = RCAR.pos.x + (v.x*deltat)
  RCAR.pos.y = RCAR.pos.y + (v.y*deltat)
  
  t = t + deltat


t = 0

RCAR.axis = vec(cartL,0,0)

speed = sqrt((v.x**2) + (v.y**2))


v = vec(speed,0,0)


while (RCAR.pos.x + (cartL/2)) < (BCAR.pos.x-(cartL/2)):
  
  rate(10000)
  RCAR.pos.x = RCAR.pos.x + (v.x*deltat)
  RCAR.pos.y = RCAR.pos.y + (v.y*deltat)
  
  t = t + deltat
  
t = 0
print(speed)
speedF = (speed * m_r)  / (M)



Fnormval = g * (m_wb)
Fnet = Ffric = vec(-mu * Fnormval, 0,0)
block_a = Fnet / (M) 

v = vec(speedF, 0,0)

while v.x > 0 :
  rate(10000)
  v = v + (block_a*deltat)
  RCAR.pos = RCAR.pos + (v*deltat)
  BCAR.pos = BCAR.pos + (v*deltat)
  block.pos = block.pos + (v*deltat)
  
  
  t = t + deltat
 
print("The center of your cart needs to be at mark {:.2f}{}." .format(rl - L, ' on the ramp')) 
print("The stopper needs to be placed at mark {:.2f}{}." .format(rl - L-springL - stringL, ' on the ramp'))
