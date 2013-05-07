import random

def mutate(genome, mutRate, rangeMin=0, rangeMax=1000):
	""" mutator for list of integers that introduces new random #"""
	listSize = len(genome)
	mutations = 0
	for it in range(listSize):
		if FlipCoin(mutRate):
			genome[it] = random.uniform(rangeMin,rangeMax)
			mutations += 1
	return genome
			

def FlipCoin(p):
   if p == 1.0: return True
   if p == 0.0: return False
   if random.random() <= p: return True
   else: return False


if __name__=='__main__':
	print(mutate([1,3,5,2,80,43,57,62],0.05,1,100))
