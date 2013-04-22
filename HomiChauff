
import scipy
import random

def fit_func(genr,geny):
	# r represents predator and y represents prey
	# genpr and genpy are lists of all predator and prey genomes
	# will return lists (scorepr and scorepy) of all final scores 

	rscores=[0]*gensize
	yscores=[0]*gensize

	for r in genr:
		for y in geny:
			[elapsedtime,closestpt]=testrun(r,y)
			score=elapsedtime+1000*closestpt
			rscores[genr.index(r)]+=score
			yscores[geny.index(y)]+=score
	
	return(rscores,yscores)



def testrun(r,y):
	mr = 18*(10**-3)
	my = 10*(10**-3)
	Fmaxr = 15*(10**-3)
	Fmaxy = 10*(10**-3)
	c = 1*(10**-3)
	init_params = [50,0,0,0,0,0,0,0]
	
	

	return(elaspedtime,closestpt)


def predpreyDE():


	return(paramchange)

def preyforce():

	return (yforce)


def predforce():

	return (rforce)
