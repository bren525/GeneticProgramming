from selector import nextpop
from initialPop import initialPop
from operator import attrgetter
from TestFitnessFunctions import testFitFunc2
import math

def averageScore(pop):
	'''returns a float which is the populations average score'''
	total = sum(pop)
	return float(total)/float(len(pop))
	
def bestScore(pop,minmax='max'):
	'''returns the Gen with the highest score in a population'''
	if minmax == 'max':
		return sorted(pop,key=attrgetter('rawScore'))[len(pop)-1]
	else:
		return sorted(pop,key=attrgetter('rawScore'))[0]

lower = 0 # bounds for Gen parameters
upper = 100
rpop = initialPop(20,lower,upper,5) # initializes pops
ypop = initialPop(20,lower,upper,5)


for i in range(1000):
	testFitFunc2(rpop,ypop) # sets pop scores
	
	if i%100 == 0: # prints every 100th generation
		
		print('Generation',i)
		print(str('r ')+str(averageScore(rpop))+' '+str(bestScore(rpop)))
		print(str('y ')+str(averageScore(ypop))+' '+str(bestScore(ypop)))
		
	#Evolves! (gets the new pop)
	rpop = nextpop(rpop,.05,lower,upper,'max')
	ypop = nextpop(ypop,.05,lower,upper,'max')

testFitFunc2(rpop,ypop)
print('Generation',1000)
print(str('r ')+str(averageScore(rpop))+' '+str(bestScore(rpop)))
print(str('y ')+str(averageScore(ypop))+' '+str(bestScore(ypop)))
testFitFunc2(rpop,ypop)
