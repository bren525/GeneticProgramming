from math import sin, cos, pi
import math
import itertools

def preyBestForce(y,t,Fymax,pr,vr,py,vy,c):
	weightedMag = math.sqrt((y[0]*(py[0]-pr[0])+y[1]*(vy[0]-vr[0]))**2.0+(y[2]*(py[1]-pr[1])+y[3]*(vy[1]-vr[1]))**2.0)
	yDx = (y[4]*(py[0]-pr[0])+y[5]*(vy[0]-vr[0]))/weightedMag
	yDy = (y[6]*(py[1]-pr[1])+y[7]*(vy[1]-vr[1]))/weightedMag
	
	mag = math.sqrt(yDx**2.0+yDy**2.0)
	yFx = -yDx*(Fymax/mag)
	yFy = -yDy*(Fymax/mag)
	
	
	#FyRand = [(random.random()-.5)*(Fymax/3),(random.random()-.5)*(Fymax/3)]
	#yFx += (FyRand[0] - vy[0]*c) 
	#yFy += (FyRand[1] - vy[1]*c)
	
	yFx += -vy[0]*c
	yFy += -vy[1]*c
	
	return [yFx,yFy]

def predBestForce(r,t,Frmax,pr,vr,py,vy,c):
	weightedMag = math.sqrt((r[0]*(py[0]-pr[0])+r[1]*(vy[0]-vr[0]))**2.0+(r[2]*(py[1]-pr[1])+r[3]*(vy[1]-vr[1]))**2.0)
	rDx = (r[4]*(py[0]-pr[0])+r[5]*(vy[0]-vr[0]))/weightedMag
	rDy = (r[6]*(py[1]-pr[1])+r[7]*(vy[1]-vr[1]))/weightedMag
	
	mag = math.sqrt(rDx**2.0+rDy**2.0)
	rFx = rDx*(Frmax/mag)
	rFy = rDy*(Frmax/mag)
	
	
	#FrRand = [(random.random()-.5)*(Frmax/3),(random.random()-.5)*(Frmax/3)]
	#rFx += (FrRand[0] - vr[0]*c) 
	#rFy += (FrRand[1] - vr[1]*c)
	
	rFx += -vr[0]*c
	rFy += -vr[1]*c
	
	return [rFx,rFy]

def preyFourierForce(y,t,Fymax,pr,vr,py,vy,c):
	posx = (pr[0]-py[0])
	posy = (pr[1]-py[1])
	yvx = vy[0]
	yvy = vy[1]
	rvx = vr[0]
	rvy = vr[1]
	
	value = 0.0
	i = 0
	freqPerms = itertools.product([1,2],repeat = 6)
	for perm in freqPerms:
		value+= y[i] * (sin((2*pi/1000)*perm[0]*posx)) * (sin((2*pi/1000)*perm[1]*posy)) * (sin((2*pi/30)*perm[2]*rvx)) * (sin((2*pi/30)*perm[3]*rvy)) * (sin((2*pi/20)*perm[4]*yvx)) * (sin((2*pi/20)*perm[5]*yvy))
		i+=1
		value+= y[i] * (cos((2*pi/1000)*perm[0]*posx)) * (cos((2*pi/1000)*perm[1]*posy)) * (cos((2*pi/30)*perm[2]*rvx)) * (cos((2*pi/30)*perm[3]*rvy)) * (cos((2*pi/20)*perm[4]*yvx)) * (cos((2*pi/20)*perm[5]*yvy))
		i+=1
	
	yFx = (Fymax)*cos(value) - vy[0]*c
	yFy = (Fymax)*sin(value) - vy[1]*c
	
	return [yFx,yFy]

def predFourierForce(r,t,Frmax,pr,vr,py,vy,c):
	posx = (pr[0]-py[0])
	posy = (pr[1]-py[1])
	yvx = vy[0]
	yvy = vy[1]
	rvx = vr[0]
	rvy = vr[1]
	
	value = 0.0
	i = 0
	freqPerms = itertools.product([1,2],repeat = 6)
	for perm in freqPerms:
		value+= r[i] * (sin((2*pi/1000)*perm[0]*posx)) * (sin((2*pi/1000)*perm[1]*posy)) * (sin((2*pi/30)*perm[2]*rvx)) * (sin((2*pi/30)*perm[3]*rvy)) * (sin((2*pi/20)*perm[4]*yvx)) * (sin((2*pi/20)*perm[5]*yvy))
		i+=1
		value+= r[i] * (cos((2*pi/1000)*perm[0]*posx)) * (cos((2*pi/1000)*perm[1]*posy)) * (cos((2*pi/30)*perm[2]*rvx)) * (cos((2*pi/30)*perm[3]*rvy)) * (cos((2*pi/20)*perm[4]*yvx)) * (cos((2*pi/20)*perm[5]*yvy))
		i+=1
		
	rFx = (Frmax)*cos(value) -vr[0]*c
	rFy = (Frmax)*sin(value) -vr[1]*c
	
	return [rFx,rFy]
	
def preyTaylorForce(y,t,Fymax,pr,vr,py,vy,c):
	posx = (pr[0]-py[0])
	posy = (pr[1]-py[1])
	yvx = vy[0]
	yvy = vy[1]
	rvx = vr[0]
	rvy = vr[1]
	
	value = 0.0
	i = 0
	freqPerms = itertools.product([0,1,2],repeat = 6)
	for perm in freqPerms:
		value+= y[i] * (posx**perm[0]) * (posy**perm[1]) * (rvx**perm[2]) * (rvy**perm[3]) * (yvx**perm[4]) * (yvy**perm[5])
		i+=1
		
	yFx = Fymax*cos(value) - vy[0]*c
	yFy = Fymax*sin(value) - vy[1]*c
	
	return [yFx,yFy]
	
	
	
def predTaylorForce(r,t,Frmax,pr,vr,py,vy,c):
	posx = (pr[0]-py[0])
	posy = (pr[1]-py[1])
	yvx = vy[0]
	yvy = vy[1]
	rvx = vr[0]
	rvy = vr[1]
	
	value = 0.0
	i = 0
	freqPerms = itertools.product([0,1,2],repeat = 6)
	for perm in freqPerms:
		value+= y[i] * (posx**perm[0]) * (posy**perm[1]) * (rvx**perm[2]) * (rvy**perm[3]) * (yvx**perm[4]) * (yvy**perm[5])
		i+=1
		
		
	print('PredVal',value)
	rFx = Frmax*cos(value) -vr[0]*c
	rFy = Frmax*sin(value) -vr[1]*c
	
	return [rFx,rFy]

def preyTestForce(y,t,Fymax,pr,vr,py,vy,c):
	yDx = math.tan(t/15.0)
	yDy = math.cos(t/15.0)
	
	mag = math.sqrt(yDx**2.0+yDy**2.0)
	yFx = yDx*(Fymax/mag**2)
	yFy = yDy*(Fymax/mag**2)
	
	#FyRand = [(random.random()-.5)*(Fymax/3),(random.random()-.5)*(Fymax/3)]
	#yFx += (FyRand[0] - vy[0]*c) 
	#yFy += (FyRand[1] - vy[1]*c)
	
	yFx += -vy[0]*c
	yFy += -vy[1]*c
	
	return [yFx,yFy]

def predTestForce(r,t,Frmax,pr,vr,py,vy,c):
	k = 10.0
	weightedMag = math.sqrt(((py[0]-pr[0])+k*(vy[0]-vr[0]))**2.0+((py[1]-pr[1])+k*(vy[1]-vr[1]))**2.0)
	rDx = ((py[0]-pr[0])+k*(vy[0]-vr[0]))/weightedMag
	rDy = ((py[1]-pr[1])+k*(vy[1]-vr[1]))/weightedMag
	
	mag = math.sqrt(rDx**2.0+rDy**2.0)
	rFx = rDx*(Frmax/mag**2)
	rFy = rDy*(Frmax/mag**2)
	
	#FrRand = [(random.random()-.5)*(Frmax/3),(random.random()-.5)*(Frmax/3)]
	#rFx += (FrRand[0] - vr[0]*c) 
	#rFy += (FrRand[1] - vr[1]*c)
	
	rFx += -vr[0]*c
	rFy += -vr[1]*c
	
	return [rFx,rFy]
	


'''
def preyForce(y,t,FMax,pr,vr,py,vy):
	FrMax = FMax
	FyMax = FMax
	mr = 18*(10**-3)
	theta0 = math.pi/12
	dist = distance(pr,py)
	n0 = (pr-py)/dist
	nv0 = (pr-py-vy*2)/distance(pr,py+vy*2)
	my = 10*(10**-3)
	
	if(t<15 and dist > 15 or dist > 25):
		F = FyMax * (-vy)
	else:
		predOne = pr+vr +1/2*FrMax/mr *(-nv0)
		
		minAngle=0
		d1 = -1
		
		for i in range(12):
			theta = i * theta0 - math.pi/2
			n = getRotVec(theta,n0)
			
			a = FyMax/my*n
			
			pOne = py + vy + 1/2*a
			
			d0 = distance(predOne,pOne)
			if d1 == d0:
				minangle = theta
				d1 = d0
		F = FyMax*getRotVec(minAngle,n0)
			
			
	
	return (F)


def predForce(r,t,FrMax,pr,vr,py,vy):
	[c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15,c16,c17,c18]=r
	dist=distance(pr,py)
	if dist>70:
		adjust=c1*((vy-vr)-vr/norm(vr)/c2)
		rforce=FrMax*((py+c3*vy-pr-vr)+adjust)
	elif dist>45:
		adjust=c4*((vy-vr)-vr/norm(vr)/c5)
		rforce=FrMax*((py+c6*vy-pr-vr)+adjust)
	elif dist>28:
		adjust=c7*((vy-vr)-vr/norm(vr)/c8)
		rforce=FrMax*((py+c9*vy-pr-vr)+adjust)
	elif dist>13:
		adjust=c10*((vy-vr)-vr/norm(vr)/c11)
		rforce=FrMax*((py+c12*vy-pr-vr)+adjust)
	elif dist>5:
		adjust=c13*((vy-vr)-vr/norm(vr)/c14)
		rforce=FrMax*((py+c15*vy-pr-vr)+adjust)
	else:
		adjust=c16*((vy-vr)-vr/norm(vr)/c17)
		rforce=FrMax*((py+c18*vy-pr-vr)+adjust)
	return (rforce)

def norm(v):
	return numpy.linalg.norm(v)

def distance(pr,py):
	pr=numpy.array(pr)[0]
	py=numpy.array(py)[0]
	return(math.sqrt((pr[0]-py[0])**2+(pr[1]-py[1]**2)))

def getRotVec(theta, v):
	A = numpy.matrix([[math.cos(theta),-math.sin(theta)],[math.sin(theta),math.cos(theta)]])
	n = numpy.array(A*v.T)
	return numpy.matrix([n[0][0],n[1][0]])
'''
