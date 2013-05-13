from numpy import linspace
import random
import math
from math import sin, cos
import itertools
from predPreyForces import preyFourierForce, predFourierForce, predTestForce, preyTestForce, predBestForce, preyBestForce
from predPreySim import forwardEuler
from visualization import plotting
# from scipy.integrate import odeint


def fitFunc(rpop,ypop):
	'''r represents predator and y represents prey
	rpop and ypop are lists of all predator and prey genomes
	add scores to the predators and preys'''
	for r in rpop:
		for y in ypop:
			elapsedTime,closestPoint=testrun(r,y)
			score=elapsedTime+1000*closestPoint #Score formula
			r.rawScore+=score
			y.rawScore+=score

def distance(pr,py):
	'''takes two x,y coordinates and returns the distance between them'''
	return(math.sqrt((pr[0]-py[0])**2+(pr[1]-py[1])**2))

def testrun(r,y,animate = False, saveVid = False):
	'''take a predator and a prey 
	returns elapsedTime and closestPoint for scoring purposes'''
	# initial simulation parameters (masses, max forces, drag coefficients)
	mr = .018
	my = .010
	Frmax = .015
	Fymax = .010
	c = .001
	d = .001
	caught = 2 # "prey caught" threshold
	runtime = 250
	#starting parameters for simulation
	initParams = [25.0,25.0,0.0,0.0,0.0,0.0,0.0,0.0]
	
	closestPoint = 100
	elapsedTime = runtime
	
	def predPreyDE(params,t):
	'''returns the change in sim paramaters for next timestep'''
		pr = [params[0],params[1]]
		py = [params[2],params[3]]
		vr = [params[4],params[5]]
		vy = [params[6],params[7]]
		
		Fr = predBestForce(r,t,Frmax,pr,vr,py,vy,c)
		
		Fy = preyBestForce(y,t,Fymax,pr,vr,py,vy,d)
		
		return[	params[4],
				params[5],
				params[6],
				params[7],
				Fr[0]/mr,
				Fr[1]/mr,
				Fy[0]/my,
				Fy[1]/my ]
	
	#trange = linspace(0,100,100)
	#theChase = odeint(predPreyDE,initParams,trange,rtol=.01)
	
	theChase = forwardEuler(predPreyDE,initParams,runtime) #sim runs here
	
	for i in range(len(theChase)): #checks when prey caught
		dist = distance(theChase[i][0:2],theChase[i][2:4])
		if dist < caught:
			closestPoint = 0
			elapsedTime = i
			break
		elif (dist-caught) < closestPoint:
			closestPoint = (dist-caught)
	
	if animate:	#animates if called for
		plotting(theChase[:elapsedTime],saveVid)
		
	return elapsedTime,closestPoint
