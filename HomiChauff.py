from scipy.integrate import odeint
import numpy
import random
import math

def fitFunc(rpop,ypop):
	# r represents predator and y represents prey
	# genpr and genpy are lists of all predator and prey genomes
	# will return lists (scorepr and scorepy) of all final scores 

	for r in rpop:
		for y in ypop:
			[elapsedtime,closestpt]=testrun(r,y)
			score=elapsedtime+1000*closestpt
			r.rawScore+=score
			y.rawScore+=score


def testrun(r,y):
	mr = 18*(10**-3)
	my = 10*(10**-3)
	Fmaxr = 15*(10**-3)
	Fmaxy = 10*(10**-3)
	c = 1*(10**-3)
	initParams = [50.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
	def predPreyDE(params,t):
		print(params)
		pr = numpy.matrix([params[0],params[1]])
		py = numpy.matrix([params[2],params[3]])
		vr = numpy.matrix([params[4],params[5]])
		vy = numpy.matrix([params[6],params[7]])
		
		Fr = predForce(r,t,Fmaxr,pr,vr,py,vy)
		FrRand = numpy.matrix([(random.random()-.5)*(Fmaxr/3),(random.random()-.5)*(Fmaxr/3)])
		FrDrag = -vr*c
		FrTotal = Fr+FrDrag+FrRand
		
		Fy = preyForce(y,t,Fmaxy,pr,vr,py,vy)
		FyRand = numpy.matrix([(random.random()-.5)*(Fmaxy/3),(random.random()-.5)*(Fmaxy/3)])
		FyDrag = -vy*c
		FyTotal = Fy+FyDrag+FyRand
		
		paramchange = [params[4],params[5],params[6],params[7],numpy.array(FrTotal)[0][0],numpy.array(FrTotal)[0][1],numpy.array(FyTotal)[0][0],numpy.array(FyTotal)[0][1]]

		return(paramchange)
	
	theChase = odeint(predPreyDE,initParams,range(0,250,1))
	print(theChase)
	#return(elaspedtime,closestpt)


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

if __name__ == "__main__":
	testrun([4,12,6,12,10,3.5,14,9,2,19,9,2,25,8,2,14,7,2.6],'hello')
