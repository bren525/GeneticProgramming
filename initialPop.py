import random
from genome import Gen 

def initialPop(popSize,rangeMin,rangeMax,genLength):
	"""Creates the initial population for evolving"""
	
	pop=[]

	for i in range(popSize):
		genome=[]
		for j in range(genLength):
			param=random.uniform(rangeMin,rangeMax)
			genome.append(param)
		pop.append(Gen(genome))
				
	return pop


if __name__=='__main__':
	print(initialPop(10,1,12,4))
