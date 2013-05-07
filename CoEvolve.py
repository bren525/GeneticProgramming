from selector import nextpop
from initialPop import initialPop
from fitSim import fitFunc,testrun
from operator import attrgetter
from TestFitnessFunctions import testFitFunc2
import math

def averageScore(pop):
	total = sum(pop)
	return float(total)/float(len(pop))
	
def bestScore(pop,minmax='max'):
	if minmax == 'max':
		return sorted(pop,key=attrgetter('rawScore'))[len(pop)-1]
	else:
		return sorted(pop,key=attrgetter('rawScore'))[0]

lower = -math.pi
upper = math.pi
rpop = initialPop(20,lower,upper,128)
ypop = initialPop(20,lower,upper,128)

'''for i in range(1):
	
	fitFunc(rpop,ypop)
	if i % 100 == 0:
		print(str(i),'r',averageScore(rpop),bestScore(rpop))
		print(str(i),'y',averageScore(ypop),bestScore(ypop))
	rpop = nextpop(rpop,.05,lower,upper,'min')
	ypop = nextpop(ypop,.05,lower,upper,'max')'''

fitFunc(rpop,ypop)
print('r',averageScore(rpop),bestScore(rpop))
print('y',averageScore(ypop),bestScore(ypop))
testrun(bestScore(rpop),bestScore(ypop),True)

