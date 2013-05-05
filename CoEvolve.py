from selector import nextpop
from initialPop import initialPop
from HomiChauff import fitFunc
from operator import attrgetter

def averageScore(pop):
	total = 0
	for gen in pop:
		total+=gen.rawScore
	return float(total)/float(len(pop))
	
def bestScore(pop,minmax='max'):
	if minmax == 'max':
		return sorted(pop,key=attrgetter('rawScore'))[len(pop)-1]
	else:
		return sorted(pop,key=attrgetter('rawScore'))[0]

rpop = initialPop(10,0,1000,5)
ypop = initialPop(10,0,1000,5)
fitFunc(rpop,ypop)
print('r',averageScore(rpop),bestScore(rpop))
print('y',averageScore(ypop),bestScore(ypop))

for i in range(10000):
	fitFunc(rpop,ypop)
	rpop = nextpop(rpop,.05)
	ypop = nextpop(ypop,.05)
	

fitFunc(rpop,ypop)
print('r',averageScore(rpop),bestScore(rpop))
print('y',averageScore(ypop),bestScore(ypop))
