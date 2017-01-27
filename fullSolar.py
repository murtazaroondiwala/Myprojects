# from __future__ import *
from visual import *
import math


display(title='Solar System - Murtaza Roondiwala',x=0, y=0,z=0, width=1000, height=786, background=(0,0,0))

class timeHoursSeconds(object):
    def __init__(self,s,h,d,y):
        self.s = s
        self.h = h
        self.d = d
        self.y = y
    def fromStoHours(self):
        h = self.s/60/60
        return h
    def fromStoDays(self):
        d = self.s/60/60/24
        return d
    def fromStoYears(self):
        y = self.s/60/60/24/365
        return y
    def fromDaysToS(self):
        s = self.d*24*60*60
        return s
    def fromDaysToH(self):
        h = self.d * 24
        return h
    def fromDaysToY(self):
        y = self.d/365
        return y
	
	

class planet(object):
	G = 6.67 * math.pow(10,-11)
	MassS = 1.989 * math.pow(10,31)# Mass of the Sun	
	MassE = 5.973 * math.pow(10,24)#mass of earth

	def __init__(self,name,mass,rs,theta0,radius):
		self.name = name
		self.mass = mass
		self.rs = rs
		self.theta0 = theta0
		self.radius = radius

	def GravityForce(self):
		F = self.G*(self.MassS*self.mass)/math.pow(self.rs,2)
		return F
	
	def AngularVelocity(self):
		AngV = math.sqrt(self.GravityForce()/(self.mass * self.rs))
		return AngV

	def Velocity(self):
		V = self.AngularVelocity()*self.rs
		return V	

	def AngularPosition(self,t):
		theta = self.theta0 + self.AngularVelocity()*t
		return theta

	def VarAngPos(self,t,dt):
		dtheta = self.AngularPosition(t+dt)-self.AngularPosition(t)
		return dtheta


class Moons(planet):
	
	def __init__(self,name,mass,rs,theta0,radius):
		super(Moons,self).__init__(name,mass,rs,theta0,radius)
	
	def GravityForce(self):
		F = self.G*(self.MassE*self.mass)/math.pow(self.rs,2)
		return F		


mercury = planet("Mercury",3.302 * math.pow(10,23),57910000000,0,0.3)
venus = planet("Venus",4.8685 * math.pow(10,24),108200000000,0,0.4)
earth = planet("Earth",5.973 * math.pow(10,24),149600000000,0,0.5)
mars = planet("Mars",6.4185 * math.pow(10,23),227900000000,0,0.45)
jupiter = planet("Jupiter",1.8986 * math.pow(10,27),778500000000,0,.8)
saturn = planet("Saturn",5.6846 * math.pow(10,26),1433000000000,0,0.7)
uranus = planet("Uranus",8.6832 * math.pow(10,25),2877000000000,0,0.6)
neptune = planet("Neptune",1.0243 * math.pow(10,26),4503000000000,0,0.6)
Sring = planet("Sring",5.6846 * math.pow(10,26),1433000000000,0,0.7)

#moon
v=vector(1.3,0,0)
z=vector(2,0,0)
y=vector(3,0,0)
x=vector(4,1,0)

r = vector(1.2,0,0)

moon = Moons("Moon",7.347 * math.pow(10,22),384400000,0,0.2)

io = Moons("io",7.347 * math.pow(10,22),384400000,0,0.5)
Europa = Moons("Moon",10.347 * math.pow(10,28),484400000,0,0.8)
callisto = Moons("Moon",11.347 * math.pow(10,30),584400000,0,1.2)
ganymede = Moons("Moon",21.347 * math.pow(10,38),684400000,0,1.5)


S = sphere(pos=vector(0,0,0),color=color.yellow,radius=1.155)

#visual 
me = sphere(pos=vector(3,0,0),color=color.white,radius=0.2,make_trail=True)
ven = sphere(pos=vector(5,0,0),color=color.orange,radius=0.3,make_trail=True)
e = sphere(pos=vector(7,0,0),radius=0.4,make_trail=True,material= materials.earth)
m = sphere(pos=vector(10,0,0),color=color.red,radius=0.3,make_trail=True,opacity=0.5)
j = sphere(pos=vector(20,0,0),color=color.orange,radius=0.8,make_trail=True)
s = sphere(pos=vector(30,0,0),color=color.yellow,radius=0.4,make_trail=True)
u = sphere(pos=vector(40,0,0),color=color.cyan,radius=0.5,make_trail=True)
n = sphere(pos=vector(50,0,0),color=color.blue,radius=0.3,make_trail=True)
S = sphere(pos=vector(0,0,0),color=color.yellow,radius=1.155)
S_ring=ring(pos=s.pos, axis=(0,0,1), radius=1, thickness=0.1,color = (255,255,55))

moo = sphere(pos=e.pos+r
	,color=color.white,radius=0.15,make_trail=True)

ios = sphere(pos=j.pos+r,color=color.white,radius=0.15,make_trail=True)
Europas = sphere(pos=j.pos+z,color=color.yellow,radius=0.15,make_trail=True)
callistos = sphere(pos=j.pos+y,color=color.white,radius=0.3,make_trail=True)
ganymedes = sphere(pos=j.pos+x,color=color.white,radius=0.2,make_trail=True)

j_moon= [io,Europa,callisto,ganymede]
j_moons =[ios,Europas,callistos,ganymedes]

planet = [me,ven,e,m,j,s,u,n,S_ring]
planets = [mercury,venus,earth,mars,jupiter,saturn,uranus,neptune,Sring]



t = 0
dt = timeHoursSeconds(10000,0,0,0)
years = timeHoursSeconds(0,0,365,0)
seconds = years.fromDaysToS()

while t<seconds:
	rate(50)
	for plan in range(len(planets)):
		planet[plan].pos = rotate(planet[plan].pos,angle= planets[plan].VarAngPos(t,dt.s),axis = (0,0,1))
	


	v = rotate(v,angle=moon.VarAngPos(t,dt.s),axis=(0,0,1))	
	r = rotate(r,angle=io.VarAngPos(t,dt.s),axis=(0,0,1))
	z = rotate(z,angle=Europa.VarAngPos(t,dt.s),axis=(0,0,1))
	y = rotate(y,angle=callisto.VarAngPos(t,dt.s),axis=(0,0,1))
	x = rotate(x,angle=ganymede.VarAngPos(t,dt.s),axis=(0,0,1))
	
	moo.pos = e.pos + v
	ios.pos = j.pos+r
	Europas.pos = j.pos+z
	callistos.pos = j.pos+y
	ganymedes.pos = j.pos+x
	
	t+= dt.s


