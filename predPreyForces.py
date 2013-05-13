from math import sin, cos, pi
import math
import itertools

def preyBestForce(y,t,Fymax,pr,vr,py,vy,c):
	'''The prey behavior, takes and genome, y, and constructs and function with its parameters'''
	weightedMag = math.sqrt((y[0]*(py[0]-pr[0])+y[1]*(vy[0]-vr[0]))**2.0+(y[2]*(py[1]-pr[1])+y[3]*(vy[1]-vr[1]))**2.0)
	yDx = (y[4]*(py[0]-pr[0])+y[5]*(vy[0]-vr[0]))/weightedMag
	yDy = (y[6]*(py[1]-pr[1])+y[7]*(vy[1]-vr[1]))/weightedMag
	
	mag = math.sqrt(yDx**2.0+yDy**2.0)
	yFx = -yDx*(Fymax/mag)
	yFy = -yDy*(Fymax/mag)
	
	
	yFx += -vy[0]*c
	yFy += -vy[1]*c
	
	return [yFx,yFy]

def predBestForce(r,t,Frmax,pr,vr,py,vy,c):
	'''The predator behavior, takes and genome, y, and constructs and function with its parameters'''
	weightedMag = math.sqrt((r[0]*(py[0]-pr[0])+r[1]*(vy[0]-vr[0]))**2.0+(r[2]*(py[1]-pr[1])+r[3]*(vy[1]-vr[1]))**2.0)
	rDx = (r[4]*(py[0]-pr[0])+r[5]*(vy[0]-vr[0]))/weightedMag
	rDy = (r[6]*(py[1]-pr[1])+r[7]*(vy[1]-vr[1]))/weightedMag
	
	mag = math.sqrt(rDx**2.0+rDy**2.0)
	rFx = rDx*(Frmax/mag)
	rFy = rDy*(Frmax/mag)
	
	rFx += -vr[0]*c
	rFy += -vr[1]*c
	
	return [rFx,rFy]

def preyFourierForce(y,t,Fymax,pr,vr,py,vy,c):
	'''attempt at using Fourier expansion to construct the general prey solution'''
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
	'''attempt at using Fourier expansion to construct the general predator solution'''
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

def preyTestForce(y,t,Fymax,pr,vr,py,vy,c):
	'''existing prey strategy to test our simulation'''
	yDx = math.tan(t/15.0)
	yDy = math.cos(t/15.0)
	
	mag = math.sqrt(yDx**2.0+yDy**2.0)
	yFx = yDx*(Fymax/mag**2)
	yFy = yDy*(Fymax/mag**2)
	
	
	yFx += -vy[0]*c
	yFy += -vy[1]*c
	
	return [yFx,yFy]

def predTestForce(r,t,Frmax,pr,vr,py,vy,c):
	'''existing predator strategy to test our simulation'''
	k = 10.0
	weightedMag = math.sqrt(((py[0]-pr[0])+k*(vy[0]-vr[0]))**2.0+((py[1]-pr[1])+k*(vy[1]-vr[1]))**2.0)
	rDx = ((py[0]-pr[0])+k*(vy[0]-vr[0]))/weightedMag
	rDy = ((py[1]-pr[1])+k*(vy[1]-vr[1]))/weightedMag
	
	mag = math.sqrt(rDx**2.0+rDy**2.0)
	rFx = rDx*(Frmax/mag**2)
	rFy = rDy*(Frmax/mag**2)

	
	rFx += -vr[0]*c
	rFy += -vr[1]*c
	
	return [rFx,rFy]
