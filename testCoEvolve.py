from selector import nextpop
from initialPop import initialPop
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

lower = 0
upper = 100
rpop = initialPop(20,lower,upper,5)
ypop = initialPop(20,lower,upper,5)


for i in range(1000):
	testFitFunc2(rpop,ypop)
	
	if i%100 == 0:
		
		print('Generation',i)
		print(str('r ')+str(averageScore(rpop))+' '+str(bestScore(rpop)))
		print(str('y ')+str(averageScore(ypop))+' '+str(bestScore(ypop)))
	
	rpop = nextpop(rpop,.05,lower,upper,'max')
	ypop = nextpop(ypop,.05,lower,upper,'max')

testFitFunc2(rpop,ypop)
print('Generation',1000)
print(str('r ')+str(averageScore(rpop))+' '+str(bestScore(rpop)))
print(str('y ')+str(averageScore(ypop))+' '+str(bestScore(ypop)))
testFitFunc2(rpop,ypop)
