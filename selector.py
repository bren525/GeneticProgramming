from mutations import mutate
from crossOver import crossOver
import random
from operator import attrgetter
from genome import gen

'''Our selector uses a roulette wheel selection method,
'''

def nextrpop(rpop,mutRate):
	size = len(rpop)
	total = sum(rpop)
	for rgen in rpop:
		rgen.normScore = 1 - (float(rgen.score)/float(total)) #set normalized scores (inverted for predator)
		
	rpop.sort(key = attrgetter('normScore')) #sort based on score
	accumulator = 0
	
	for rgen in rpop:
		accumulator += rgen.normScore
		rgen.accumulatedScore = accumulator
	
	nextpop = []
	for i in range(0,size,2):
		pick = random.rand()
		for rgen in rpop:
			if rgen.accumulatedScore > pick:
				mom = rgen
				break;
		pick = random.rand()
		for rgen in rpop:
			if rgen.accumulatedScore > pick:
				dad = rgen
				break;
		if (size - i) > 1:
			sis,bro = mutate(crossOver(mom,dad)
			nextpop.extend([mutate(sis,mutRate),mutate(bro,mutRate)])
		else:
			nextpop.extend(mutate(crossOver(mom,dad,1),mutRate))
	return nextpop
		
def nextypop(ypop,mutRate):
	size = len(ypop)
	total = sum(ypop)
	for ygen in ypop:
		ygen.normScore = float(ygen.score)/float(total)
		
	ypop.sort(key = attrgetter('normScore'))
	accumulator = 0
	
	for ygen in ypop:
		accumulator += ygen.normScore
		ygen.accumulatedScore = accumulator
	
	nextpop = []
	for i in range(0,size,2):
		pick = random.rand()
		for ygen in ypop:
			if ygen.accumulatedScore > pick:
				mom = ygen
				break;
		pick = random.rand()
		for ygen in ypop:
			if ygen.accumulatedScore > pick:
				dad = ygen
				break;
		if (size - i) > 1:
			sis,bro = mutate(crossOver(mom,dad)
			nextpop.extend([mutate(sis,mutRate),mutate(bro,mutRate)])
		else:
			nextpop.extend(mutate(crossOver(mom,dad,1),mutRate))
	return nextpop


if __name__=='__main__':
	print(nextrpop([[1,2,3],[4,5,6],[7,8,9],[10,11,12]],0.2))
	print(nextypop([[1,2,3],[4,5,6],[7,8,9],[10,11,12]],0.2))

