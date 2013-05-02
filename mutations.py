import random

def mutations(genome, **args):
	""" mutator for list of integers that introduces new random #"""
	
	listSize = len(genome)
	mutations = args["mutRate"] * (listSize)

	if mutations < 1:
		mutations = 0
		for it in xrange(listSize):
			if FlipCoin(args["mutRate"]):
				genome[it] = random.randint(args["rangeMin"],args["rangeMax"])
            	mutations += 1
	else: 
		for it in xrange(int(round(mutations))):
			whichGene = random.randint(0, listSize-1)
			genome[whichGene] = random.randint(args["rangeMin"],args["rangeMax"])
	return mutations,genome
			

def FlipCoin(p):
   if p == 1.0: return True
   if p == 0.0: return False
   if random.random <= p: return True
   else: return False


if __name__=='__main__':
	print(mutations([1,3,5,2,80,43,57,62],mutRate = 0.2, rangeMin = 1, rangeMax = 100))
