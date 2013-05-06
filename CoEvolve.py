from selector import nextpop
from initialPop import initialPop
from HomiChauff import fitFunc
from operator import attrgetter
from TestFitnessFunctions import testFitFunc

def averageScore(pop):
	total = sum(pop)
	return float(total)/float(len(pop))
	
def bestScore(pop,minmax='max'):
	if minmax == 'max':
		return sorted(pop,key=attrgetter('rawScore'))[len(pop)-1]
	else:
		return sorted(pop,key=attrgetter('rawScore'))[0]

lower = 0
upper = 9
rpop = initialPop(20,lower,upper,5)
ypop = initialPop(20,lower,upper,5)
print('r',averageScore(rpop),bestScore(rpop))
print('y',averageScore(ypop),bestScore(ypop))

for i in range(500):
	
	testFitFunc(rpop,ypop)
	print('r',rpop)
	#if i % 100 == 0:
		#print(str(i),'r',averageScore(rpop),bestScore(rpop))
		#print(str(i),'y',averageScore(ypop),bestScore(ypop))
	rpop = nextpop(rpop,.03,lower,upper)
	ypop = nextpop(ypop,.03,lower,upper)		

testFitFunc(rpop,ypop)
print('r',averageScore(rpop),bestScore(rpop))
print('y',averageScore(ypop),bestScore(ypop))
