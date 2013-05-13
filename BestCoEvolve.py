''' '''

from selector import nextpop
from initialPop import initialPop
from fitSim import fitFunc,testrun
from operator import attrgetter
import math

def averageScore(pop): 
	'''returns a float which is the populations average score'''
	total = sum(pop)
	return float(total)/float(len(pop))
	
def bestAverageScore(pop,minmax='max'):
	'''returns the Gen with the highest score 
		and the Gen with the median score in a population'''
	if minmax == 'max':
		sort = sorted(pop,key=attrgetter('rawScore'))
		return sort[len(pop)-1], sort[11]
	else:
		sort = sorted(pop,key=attrgetter('rawScore'))
		return sort[0], sort[10]

def bestScore(pop,minmax='max'):
	'''returns the Gen with the highest score in a population'''
	if minmax == 'max':
		return sorted(pop,key=attrgetter('rawScore'))[len(pop)-1]
	else:
		return sorted(pop,key=attrgetter('rawScore'))[0]
#Initial parameters
lower = -10 #lower and upper are bounds for the Gen parameters
upper = 10
rpop = initialPop(20,lower,upper,8) #Initializes predator and prey populations
ypop = initialPop(20,lower,upper,8)

#Set up log to collect data
log = open("6BestCoEvolveLog.txt",'a')
log.write('NewTest\n')

for i in range(5): #Runs this number of generations
	#Calculates the population scores
	fitFunc(rpop,ypop)
	#Log relevant data
	print 'Generation '+str(i)
	br,ar = bestAverageScore(rpop,'min')
	by,ay = bestAverageScore(ypop)
	aSr = averageScore(rpop)
	aSy = averageScore(ypop)
	log.write(str(i)+ ' r Av: '+str(aSr)+'\nBest: '+str(br)+'\nMed: '+str(ar)+'\n')
	log.write(str(i)+ ' y Av: '+str(aSr)+'\nBest: '+str(by)+'\nMed: '+str(ay)+'\n')
	
	#Evolves! (gets the new pop)
	rpop = nextpop(rpop,.05,lower,upper,'min')
	ypop = nextpop(ypop,.05,lower,upper,'max')

fitFunc(rpop,ypop)
print 'Generation '+str(i+1)
br,ar = bestAverageScore(rpop,'min')
by,ay = bestAverageScore(ypop)
aSr = averageScore(rpop)
aSy = averageScore(ypop)
log.write(str(i+1)+ ' r Av: '+str(aSr)+'\nBest: '+str(br)+'\nMed: '+str(ar)+'\n')
log.write(str(i+1)+ ' y Av: '+str(aSr)+'\nBest: '+str(by)+'\nMed: '+str(ay)+'\n')
