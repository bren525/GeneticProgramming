from mutations import mutate
from crossOver import crossOver
import random
from operator import attrgetter
from genome import Gen

'''Our selector uses a roulette wheel selection method,
'''

def nextpop(pop,mutRate,maxmin = 'max'):
	size = len(pop)
	total = sum(pop)
	for gen in pop:
		if maxmin == 'max':
			gen.normScore = (float(gen.rawScore)/float(total)) #set normalized scores (inverted for predator)
		else:
			gen.normScore = 1 - (float(gen.rawScore)/float(total)) #set normalized scores (inverted for predator)
		
	pop.sort(key = attrgetter('normScore')) #sort based on score
	accumulator = 0
	
	for gen in pop:
		accumulator += gen.normScore
		gen.accumulatedScore = accumulator
	
	nextpop = []
	for i in range(0,size,2):
		pick = random.random()
		for gen in pop:
			if gen.accumulatedScore > pick:
				mom = gen
				break
		pick = random.random()
		for gen in pop:
			if gen.accumulatedScore > pick:
				dad = gen
				break
		if (size - i) > 1:
			sis,bro = crossOver(mom,dad)
			nextpop.append(mutate(sis,mutRate))
			nextpop.append(mutate(bro,mutRate))
		else:
			nextpop.append(mutate(crossOver(mom,dad,1),mutRate))
	return nextpop
		


<<<<<<< HEAD
if __name__ == "__main__":
	nothing = 'nothing'
=======

if __name__=='__main__':
	print(nextrpop([[1,2,3],[4,5,6],[7,8,9],[10,11,12]],0.2))
	print(nextypop([[1,2,3],[4,5,6],[7,8,9],[10,11,12]],0.2))

>>>>>>> 497791289d0fb2d07b9eb7f12ee5435877329f25
