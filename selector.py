from mutations import mutate
from crossOver import crossOver
import random
from operator import attrgetter
from genome import Gen

'''Our selector uses a roulette wheel selection method,
'''

def nextpop(pop,mutRate,lower,upper,maxmin = 'max'):
	size = len(pop)
	total = 0
	for gen in pop:
		if maxmin == 'max':
			total += gen.rawScore
		else:
			total += (1.0/gen.rawScore)
	for gen in pop:
		if total == 0:
			gen.normScore = 1
		elif maxmin == 'max':
			gen.normScore = (float(gen.rawScore)/float(total)) #set normalized scores
		else:
			gen.normScore = ((1.0/float(gen.rawScore))/float(total)) #set normalized scores (inverted for predator)
		
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
			nextpop.append(mutate(sis,mutRate,lower,upper))
			nextpop.append(mutate(bro,mutRate,lower,upper))
		else:
			nextpop.append(mutate(crossOver(mom,dad,1),mutRate,lower,upper))
	return nextpop



