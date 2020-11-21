GlowScript 2.1 VPython
from visual import *
from visual.graph import *

vgraph = gcurve(color=color.green)
agraph = gcurve(color=color.red)
fsgraph = gcurve(color = color.blue)
### print maximum compression, time to come to stop, dissipating
angle_deg = int(prompt("What is the angle of elevation of the ramp?"))
angle = (pi*angle_deg) / 180
mass = 2
cbsize = .5
mu_s = .4
mu_k = .3
spring_length = 1.5
block_distance = 4
springk = 100
rampl = spring_length + block_distance + (block_distance/2)
sprad = block_distance / 22
ang = 90 - angle

def mag(vector):
  return sqrt((vector.x**2)+(vector.y**2))
  
scene = display(width=600,height=520,center = vec(((Math.cos(angle)*rampl)/2),(Math.sin(angle)*rampl)/2,0))

if Math.cos(angle) >= Math.sin(angle):
  scene.range = (Math.cos(angle)*rampl) / 1.85
else:
  scene.range = (Math.sin(angle)*rampl) / 1.85
scene.autoscale = False
scene.background = vec(1,1,1)
ramp = triangle(v0 = vertex(pos=vec(0,0,0),color=vec(.804,.52,.3)), v1 = vertex(pos=vec(Math.cos(angle) * rampl,0,0),color=vec(.804,.52,.3)), v2 = vertex(pos=vec(Math.cos(angle) * rampl,Math.sin(angle)*rampl,0),color=vec(.804,.52,.3),shininess=vec(0,0,0)))

block = box(pos=vec((Math.cos(angle)*(spring_length+block_distance+(cbsize/2))) - ((cbsize/2)*(Math.cos(90-angle))), (Math.sin(angle)*(spring_length+block_distance+(cbsize/2))) + ((cbsize/2)*(Math.sin(90-angle))), 0), axis = vec(Math.cos(angle),Math.sin(angle),0), size = vec(cbsize,cbsize,cbsize), color = vec(1,0,0), shininess = vec(0,0,0))
spring = helix(pos=vec(sprad*-Math.cos(90-angle),sprad*Math.sin(90-angle),0), axis=vec(Math.cos(angle)*spring_length, Math.sin(angle)*spring_length, 0), radius = sprad, coils = 13*spring_length)

t = 0
deltat = .0001

block_a = vec(0,0,0)
block_net = vec(0,0,0)
block_v = vec(0,0,0)

impact = spring.pos.y + spring.axis.y

force_grav = vec(0,-9.8*mass,0)
norm = force_grav.y*Math.cos(angle)
force_norm = vec(Math.cos(ang)*norm,Math.sin(ang)*norm,0)
ff = -norm*mu_k
force_k_friction = vec(ff*Math.cos(angle),ff*Math.sin(angle),0)
gap = force_grav.y*Math.sin(angle)
parallel = vec(gap*Math.cos(angle),gap*Math.sin(angle),0)

block_netog = vec(parallel.x + force_k_friction.x, parallel.y + force_k_friction.y,0)
block_net = block_netog
block_a = block_net / mass

fs= vec(0,0,0)
e = -force_grav.y*(Math.sin(angle)*block_distance)
Eg = e
time = sqrt((block_distance )/(.5*mag(block_a)))
comp = mag(force_norm) * mu_s
while t <= time:
  rate(10000)
  if mag(block_net) > comp:
    block_v = block_v + (block_a*deltat)
    
    block.pos.x = block.pos.x + (block_v.x*deltat)
    block.pos.y = block.pos.y + (block_v.y*deltat)
    
    t = t + deltat


deltas = 0

K = .5*mass*(mag(block_v)**2)
Ediss = Eg - K
wfric = (block_distance * mag(force_k_friction))

b = (-force_grav.y*Math.sin(angle)) + mag(force_k_friction)
a = .5 * springk
c = -(Eg - wfric)

stretch = (-b + sqrt((b**2) - (4*a*c))) / (2*a)

t = 0
v = mag(block_v)
sl = spring_length + .001
test = True
while True:
  rate(10000)
  
  
  if (block.pos.y-((cbsize/2)*sin(angle))) < impact:
    if block_v.x < 0:
      block_net = vec(parallel.x+force_k_friction.x+fs.x,parallel.y+force_k_friction.y+fs.y,0)
      spring_length = spring_length - (.5*mag(block_a)*(deltat**2)) + (-mag(block_v)*deltat)
      vel = -mag(block_v)
    else:
      block_net = vec(parallel.x-force_k_friction.x+fs.x,parallel.y-force_k_friction.y+fs.y,0)
      spring_length = spring_length + (.5*mag(block_a)*(deltat**2)) + (mag(block_v)*deltat) 
      vel = mag(block_v)
    spring.axis.x = spring.axis.x + (block_v.x*deltat)
    spring.axis.y = spring.axis.y + (block_v.y*deltat)
  if (block.pos.y - ((cbsize/2)*sin(angle))) > impact:
    if block_v.x > 0:
      block_net = vec(parallel.x-force_k_friction.x,parallel.y-force_k_friction.y,0)
      vel = mag(block_v)
    if block_v.x < 0:
       vel = -mag(block_v)
       block_net = vec(parallel.x+force_k_friction.x,parallel.y+force_k_friction.y,0)
  deltas =  sl - spring_length
  fs = vec(springk*deltas*Math.cos(angle),springk*deltas*Math.sin(angle),0)
  block_a = block_net / mass
  block_v = block_v + (block_a*deltat)
  block.pos.x = block.pos.x + (block_v.x*deltat)
  block.pos.y = block.pos.y + (block_v.y*deltat)
  fsgraph.plot(pos=(t,mag(fs)))
  if block_a.x < 0:
    acc = -mag(block_a)
  else:
    acc = mag(block_a)
  agraph.plot(pos=(t,acc))
  vgraph.plot(pos=(t,vel))
  if mag(block_v) < .001 and mag(block_net) < comp:
    break
  t = t + deltat
  Ediss = 0
print("Maximum compression of spring: " + stretch)
print("Time for block to come to rest: " + t)
print("Dissipated energy: " + Ediss)