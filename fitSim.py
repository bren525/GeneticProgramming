from numpy import linspace
from scipy.integrate import odeint
from pylab import plot, axis, show
import random
import math
from math import sin, cos
import itertools
from predPreyForces import preyFourierForce, predFourierForce



def fitFunc(rpop,ypop):
	# r represents predator and y represents prey
	# rpop and ypop are lists of all predator and prey genomes
	# will return lists (scorepr and scorepy) of all final scores 
	count = 0
	for r in rpop:
		for y in ypop:
			count+=1
			print(count)
			elapsedTime,closestPoint=testrun(r,y)
			score=elapsedTime+1000*closestPoint
			r.rawScore+=score
			y.rawScore+=score

def distance(pr,py):
	return(math.sqrt((pr[0]-py[0])**2+(pr[1]-py[1])**2))

def testrun(r,y,animate = False):
	mr = .018
	my = .010
	Frmax = .015
	Fymax = .010
	c = .001
	caught = 2
	initParams = [10.0,10.0,0.0,0.0,0.0,0.0,0.0,0.0]
	
	closestPoint = 100
	elapsedTime = 100
	
	def predPreyDE(params,t):
		pr = [params[0],params[1]]
		py = [params[2],params[3]]
		vr = [params[4],params[5]]
		vy = [params[6],params[7]]
		
		dist = distance(pr,py)
		
		Fr = predFourierForce(r,t,Frmax,pr,vr,py,vy,c)
		
		Fy = preyFourierForce(y,t,Fymax,pr,vr,py,vy,c)
		
		return[	params[4],
				params[5],
				params[6],
				params[7],
				Fr[0]/mr,
				Fr[1]/mr,
				Fy[0]/my,
				Fy[1]/my ]
	
	trange = linspace(0,100,100)
	theChase = odeint(predPreyDE,initParams,trange,rtol=.01)
	
	for i in range(len(theChase)):
		dist = distance(theChase[i][0:2],theChase[i][2:4])
		if dist < caught:
			print('CAUGHT!')
			closestPoint = 0
			elapsedTime = i
		elif (dist-caught) < closestPoint:
			closestPoint = (dist-caught)
	
	if animate:	
		plot(theChase[:,0], theChase[:,1],'r-')
		plot(theChase[:,2], theChase[:,3],'b-')
		axis('equal')
		show()
		
	return elapsedTime,closestPoint

if __name__ == "__main__":
	from initialPop import initialPop
	print(testrun(initialPop(50,-math.pi,math.pi,8192)[0],initialPop(50,-math.pi,math.pi,8192)[0],True))
