GlowScript 2.1 VPython

#INPUTS: only put numerical values.

distance = ''
$('<input placeholder="How far away is the cannon from the water balloon (in meters)?"/>').appendTo($('body')).css('width', '384px').keypress(def (e):
    global distance
    if String.fromCharCode(e.keyCode) == '\r': # '\r' is a carriage return ("Enter")
        distance = $(this).val()
        scene.trigger('input')
)
scene.waitfor('input') # this fails to proceed after scene.trigger('input')

theta = ''
$('<input placeholder="What is the initial launch angle of the projectile? (degrees)"/>').appendTo($('body')).css('width', '292px').keypress(def (e):
    global theta
    if String.fromCharCode(e.keyCode) == '\r': # '\r' is a carriage return ("Enter")
        theta = $(this).val()
        scene.trigger('input')
)
scene.waitfor('input') # this fails to proceed after scene.trigger('input')


drop = ''
$('<input placeholder="How long after takeoff does the drone drop the water balloon? (seconds)"/>').appendTo($('body')).css('width', '375px').keypress(def (e):
    global drop
    if String.fromCharCode(e.keyCode) == '\r': # '\r' is a carriage return ("Enter")
        drop = $(this).val()
        scene.trigger('input')
)
scene.waitfor('input') # this fails to proceed after scene.trigger('input')


cent = (float(distance)/2) + 5
scene = display(width=600,height=520,center = vec(0,cent,0))
scene.range = scene.center.y + 10
scene.autoscale = False
scene.background = vec(1,1,1)

angle = (float(theta) * pi) / 180

ground = box(pos=vec(0,-5,0), length = (2*scene.range) + 20, height = 8,width = 15, color = color.green)
wb = sphere(radius=1, pos = vec(-scene.range + 15,ground.pos.y+5,0),color= color.cyan)
dronespeed = 15
quad = box(pos=vec(-scene.range + 15,ground.pos.y+5+2,0),length = 2, height = 2, width = 1, color=color.red)
vquad = vec(0,dronespeed,0)



cannon = cylinder(pos = vec(-wb.pos.x+(10*Math.cos(angle)),ground.pos.y + 5,0), radius = .8, axis = vec(-10*Math.cos(angle),10*Math.sin(angle),0),color = color.blue)
cannonball = sphere(radius = .5, pos = vec((-wb.pos.x+(10*Math.cos(angle)))-10*Math.cos(angle),ground.pos.y+5+(10*Math.sin(angle)),0),color=color.magenta, make_trail=True, trail_type="points",
interval=1000, retain=1200)


vcb = 35
vcball = vec(-Math.cos(angle)*vcb,vcb*Math.sin(angle),0)

mwb = .1
g = 9.8
Fg = vec(0,-(mwb*g), 0)
vwb = vec(0,0,0)

mcb = .1
Fgc = vec(0,-(mcb*g),0)

t=0
deltat=0.0001

cannonxtime = (float(distance)) / (vcb*Math.cos(angle))
yval_at_x = (-4.9*((cannonxtime)**2)) + (vcb*Math.sin(angle)*cannonxtime) + (10*Math.sin(angle))
falltime = (-dronespeed - sqrt((dronespeed**2) - (4*-4.9*((15*drop)-yval_at_x)))) / -9.8

delay = falltime - cannonxtime

while t <= float(drop):
  rate(8000)
  quad.pos = quad.pos + (vquad*deltat)
  wb.pos = wb.pos + (vquad*deltat)
  t = t + deltat

vwb = vec(0,dronespeed,0)
while (t <= (float(drop) + cannonxtime + delay) and wb.pos.y > ground.pos.y + 5):
  rate(6000)
  quad.pos = quad.pos + (vquad*deltat)
  if t >= float(drop)+delay:
    cannonball.pos = cannonball.pos + (vcball*deltat) + (.5*(Fgc/mcb)*(deltat**2))
    vcball = vcball + (Fgc/mcb)*deltat
  if t >= float(drop):
    wb.pos = wb.pos + vwb*deltat+(.5*(Fg/mwb)*deltat**2)
    vwb = vwb + (Fg/mwb)*deltat
  t = t +deltat  

print("(" + wb.pos.x + ", " + yval_at_x + ")")