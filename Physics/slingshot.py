GlowScript 2.7 VPython

scene = display(width=500,height=500,center = vec(0,0,0))
scene.range = 80
scene.background = vec(1,1,1)
scene.autoscale = False
f1 = gcurve()

angle = 35
theta = (angle*pi / 180)
k = 70
m = 6
chutelength = 4.5
hit = False

cliffgap = 60
cliffW = (200-cliffgap)
cliff1 = box(color=color.green, pos=vec((-cliffgap/2)-(cliffW/2), -100,0), size = vec(cliffW,100,5))
cliff2 = box(color=color.green, pos=vec((cliffgap/2)+(cliffW/2), -100,0), size = vec(cliffW,100,5))
slingshot = helix(pos=vec(-cliffgap,cliff1.pos.y+(cliff1.size.y/2),0),axis=vec(13*cos(theta),13*sin(theta),0), coils=10,radius=1.4)
ball = sphere(color=color.red,radius=1.4,pos=slingshot.pos+slingshot.axis)
#scene.camera.follow(ball)

g= -9.8
Fg = vec(0,0,0)
ball.p = vec(0,0,0)
Fnet = vec(0,0,0)
Fn = norm(slingshot.axis)
s0 = ball.pos
x = vec(0,0,0)
Fric = 0

rho = 1.225
radius = .1
Aball = pi*(radius**2)
C = .47
Fair = vec(0,0,0)

#plane that drops person
plane = box(pos=vec(80,75,0), size=vec(10,1.5,2),color=vec(0,0,0))
person = box(pos=vec(plane.pos.x,plane.pos.y-(plane.size.y/2)-.7,0),size=vec(2.8,2.8,2.8),color=color.blue)
V = vec(-9.5,0,0)
person.m = 4
person.p = V*person.m
grav = vec(0,g*person.m,0)
Aperson = .1**2
c2 = 1
air = -.5*rho*c2*Aperson*(mag((person.p/person.m))**2)*norm(person.p)
chutetime= 1 + random() + random() + random() + random()
tube = cylinder(pos=vec(1000,0,0),axis=vec(0,chutelength,0),radius=.5)
chute = ellipsoid(pos=vec(1000,0,0),length=7,height=2,width=1,color=color.black)
t=0
dt=.001
while person.pos.x >= 30:
  rate(1/dt)
  plane.pos = plane.pos + (person.p/person.m*dt)
  person.pos= person.pos + (V*dt)
  angle = norm(scene.mouse.pos - slingshot.pos)
  slingshot.axis = 13*angle
  ball.pos = slingshot.pos + (13* angle) 
  t = t + dt
  
t = 0

launch = False
while ball.pos.y-(ball.radius) > -50 or ball.pos.x < 30 or person.pos.y-(person.size.y/2) > -50 or ball.p.x > 0::
  rate(1/dt)
  grav = vec(0,g*person.m,0)
  def launched():
    global launch
    launch = True
  scene.bind("mouseup",launched)
  if launch == False:
    ball.pos = slingshot.pos + (13* angle)
    angle = norm(scene.mouse.pos - s0)
    slingshot.axis = 13*angle
    s0 = ball.pos
    Fn = -450*norm(slingshot.axis)
  if launch == True:
    Fs = k*x
    x = s0 - (slingshot.pos+slingshot.axis)
    
    if ball.p.x <= 0:
      Fn = Fn
    else:
      Fn = vec(0,0,0)
    if ball.pos.y-(ball.radius) <= -50 and ball.pos.x > 0:
      ball.p.y = 0
      Fric = -3
    Fnet = Fn + Fs + Fg + Fair + vec(Fric,0,0)
    ball.p = ball.p + (Fnet*dt)
    ball.pos = ball.pos + (ball.p/m)*dt
    
      
    if x.x >= 0:
      slingshot.axis = slingshot.axis + (ball.p/m*dt)
    else:
      Fg = vec(0,g*m,0)
      Fair = -.5*rho*C*Aball*(mag(ball.p/m)**2)*norm(ball.p)
      x = vec(0,0,0)
  if person.pos.y-(person.size.y/2) <= -50:
    person.p.y=0
    Fric = -3  
  Fnet2 = grav + air + vec(Fric,0,0)
  air = -.5*rho*c2*Aperson*((mag(person.p/person.m))**2)*norm(person.p)
  person.p = person.p + (Fnet2*dt)  
  
    
  person.pos = person.pos + (person.p/person.m*dt)
  plane.pos = plane.pos + (3*V*dt)
  if t >= chutetime and hit == False:
    Aperson = 1.6
    chute.pos = person.pos +  vec(0,chutelength,0)
    tube.pos = person.pos
    chute.v = person.p/person.m
  if hit == True:
    chute.pos = chute.pos + (chute.v*dt)
    tube.pos = tube.pos + (chute.v*dt)
  if ball.pos.x + (ball.radius) >= person.pos.x-(person.size.x/2) and hit == False and ball.pos.y - ball.radius < person.pos.y+(person.size.y/2)  and ball.pos.y+ball.radius > person.pos.y-(person.size.y/2) and ball.pos.x <person.pos.x:
    ball.p = person.p = ball.p + person.p
    m = person.m = m + person.m
    C = c2 = .75
    Aball = Aperson = .1**2
    hit = True
  t = t+dt
  

