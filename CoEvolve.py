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

log = open("CoEvolveLog3.txt",'a')
log.write('NewTest\n')

for i in range(5000):
	fitFunc(rpop,ypop)
	
	if i%10 = 0:
		log.write(str('Generation ')+str(i)+'\n')
		print('Generation',i)
		log.write(str('r ')+str(averageScore(rpop))+' '+str(bestScore(rpop))+'\n')
		log.write(str('y ')+str(averageScore(ypop))+' '+str(bestScore(ypop))+'\n')
		for r in rpop:
			log.write('r '+str(r)+'\n')
		for y in ypop:
			log.write('y '+str(y)+'\n')
	
	rpop = nextpop(rpop,.05,lower,upper,'min')
	ypop = nextpop(ypop,.05,lower,upper,'max')

fitFunc(rpop,ypop)
log.write(str('Generation ')+str(i)+'\n')
print('Generation',i)
log.write(str('r ')+str(averageScore(rpop))+' '+str(bestScore(rpop))+'\n')
log.write(str('y ')+str(averageScore(ypop))+' '+str(bestScore(ypop))+'\n')
for r in rpop:
	log.write('r '+str(r)+'\n')
for y in ypop:
	log.write('y '+str(y)+'\n')
testrun(bestScore(rpop,'min'),bestScore(ypop,'min'),True)

