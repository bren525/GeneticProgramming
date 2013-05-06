from selector import nextpop
from initialPop import initialPop
from HomiChauff import fitFunc
from operator import attrgetter
from TestFitnessFunctions import testFitFunc2

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
rpop = initialPop(200,lower,upper,5)
ypop = initialPop(200,lower,upper,5)
print('r',averageScore(rpop),bestScore(rpop))
print('y',averageScore(ypop),bestScore(ypop))

for i in range(5000):
	
	testFitFunc2(rpop,ypop)
	if i % 100 == 0:
		print(str(i),'r',averageScore(rpop),bestScore(rpop))
		print(str(i),'y',averageScore(ypop),bestScore(ypop))
	rpop = nextpop(rpop,.05,lower,upper)
	ypop = nextpop(ypop,.05,lower,upper)		

testFitFunc2(rpop,ypop)
print('r',averageScore(rpop),bestScore(rpop))
print('y',averageScore(ypop),bestScore(ypop))
