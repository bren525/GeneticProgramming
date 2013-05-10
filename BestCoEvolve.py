from selector import nextpop
from initialPop import initialPop
from fitSim import fitFunc,testrun
from operator import attrgetter
import math

def averageScore(pop):
	total = sum(pop)
	return float(total)/float(len(pop))
	
def bestAverageScore(pop,minmax='max'):
	if minmax == 'max':
		sort = sorted(pop,key=attrgetter('rawScore'))
		return sort[len(pop)-1], sort[11]
	else:
		sort = sorted(pop,key=attrgetter('rawScore'))
		return sort[0], sort[10]

def bestScore(pop,minmax='max'):
	if minmax == 'max':
		return sorted(pop,key=attrgetter('rawScore'))[len(pop)-1]
	else:
		return sorted(pop,key=attrgetter('rawScore'))[0]

lower = -10
upper = 10
rpop = initialPop(20,lower,upper,8)
ypop = initialPop(20,lower,upper,8)

log = open("2BestCoEvolveLog.txt",'a')
log.write('NewTest\n')
scoreLog = open("2ScoreLog.txt",'a')

for i in range(10000):
	fitFunc(rpop,ypop)
	print('Generation ',i)
	br,ar = bestAverageScore(rpop,'min')
	by,ay = bestAverageScore(ypop)
	aSr = averageScore(rpop)
	aSy = averageScore(ypop)
	log.write(str(i)+ ' r Av: '+str(aSr)+'\nBest: '+str(br)+'\nMed: '+str(ar)+'\n')
	log.write(str(i)+ ' y Av: '+str(aSr)+'\nBest: '+str(by)+'\nMed: '+str(ay)+'\n')
	scoreLog.write(str(i)+','+str(aSr)+','+str(br.rawScore)+','+str(by.rawScore))
	
	rpop = nextpop(rpop,.05,lower,upper,'min')
	ypop = nextpop(ypop,.05,lower,upper,'max')

fitFunc(rpop,ypop)
print('Generation ',i+1)
br,ar = bestAverageScore(rpop,'min')
by,ay = bestAverageScore(ypop)
aSr = averageScore(rpop)
aSy = averageScore(ypop)
log.write(str(i+1)+ 'r Av: '+str(aSr)+' Best: '+str(br)+' Med: '+str(ar)+'\n')
log.write(str(i+1)+ 'y Av: '+str(aSr)+' Best: '+str(by)+' Med: '+str(ay)+'\n')
scoreLog.write(str(i+1)+','+str(aSr)+','+str(br.rawScore)+','+str(by.rawScore))
