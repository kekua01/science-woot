GlowScript 2.7 VPython
from visual import *
scene = display(width=600, height = 420, center=vec(10,0,0))
scene.range = 30
scene.autoscale = False
scene.background = vec(.5,1,1)


g = -9.8
e1 = gcurve(color=color.green)
e2 = gcurve(color=color.red)
building1 = box(pos=vec(-24,-20,-5),size=vec(30,62,2))
building2 = box(pos=vec(24,-16,-5),size=vec(30,62,2), shininess = 0)

#create batman and grappling hook
guy = box(pos=vec(-8,12,0), size = vec(2,2,2), color = color.red)
scene.camera.follow(guy)
rope = helix(pos=guy.pos, axis = vec(0,0,0),coils=55,radius=.3,color=color.black)

#variables for time and interval of time change
t = 0
dt = .001

#USER CAN CHANGE THESE
#tensile strength (force required to break rope)
ts = 4500
#392.4 pounds per square millimeter
#mass of batman
guy.m = 90
#initial velocity of fired grappling hook
grapple_shot = 20
#angle of fired grappling hook
angle1 = 30

scene.waitfor("mouseup")
theta1 = (angle1*pi)/180
rope.v = vec(grapple_shot*cos(theta1),grapple_shot*sin(theta1),0)
ar = vec(0,g,0)

while rope.axis.y >= 0: 
  rate(1/dt)
  rope.v = rope.v + ar*dt  
  rope.axis = rope.axis + (rope.v)*dt
  t = t + dt
anchor = rope.pos + rope.axis
hook = sphere(pos = anchor, radius = .6, color=color.black)
L = mag(anchor - guy.pos)

jump = 0 * guy.m
angle2 = 80
theta2 = (angle2*pi)/180
guy.p = vec(jump*cos(theta2),jump*sin(theta2),0)
Ft = vec(0,0,0)
Fgg = guy.m*vec(0,g,0)

scene.waitfor("mouseup")
click = False
t=0
V = arrow(pos=guy.pos, axis = vec(0,0,0), shaftwidth = .5, color = color.green)
A = arrow(pos=guy.pos, axis  = vec(0,0,0), shaftwidth=.5, color = color.blue)
T = arrow(pos=guy.pos, axis  = vec(0,0,0), shaftwidth= .5, color = color.red)
while t < 20:
  rate(1/dt)
  if mag(Ft) > ts or click == True:
    click = True
    Ft = vec(0,0,0)
  else:
    pull = anchor-guy.pos
    v = mag(guy.p) / guy.m
    a = (v**2)/L
    x = guy.pos.x - anchor.x
    y = anchor.y - guy.pos.y
    theta = atan(x/y)
    Ft=(guy.m*-g*cos(theta)+guy.m*a)*norm(pull)
    rope.pos = guy.pos 
    rope.axis = anchor - guy.pos
  Fnet = Ft + Fgg
  guy.p = guy.p + Fnet*dt
  guy.pos = guy.pos + (guy.p/guy.m)*dt
  V.pos = guy.pos
  V.axis = guy.p / guy.m
  A.pos = guy.pos
  A.axis = Fnet / guy.m 
  T.pos = guy.pos
  T.axis = Ft / guy.m
  h = abs(anchor.y - L - guy.pos.y)
  e1.plot(pos=(t,mag(Ft)))
  #e2.plot(pos=(t,guy.m*-g*h))
  t = t + dt
  def letgo():
    global click
    click = True
  scene.bind("mouseup",letgo)


