import random

def crossOver(mom,dad,count):
	"""Takes in two genomes swaps their elements and produces two babies"""
	
	cut = random.randint(1, len(mom)-1)
	
	if count >= 1:
		sis=mom[:]
		sis[cut:]=dad[cut:]

	if count == 2:
		bro=dad[:]
		bro[cut:]=mom[cut:]
	
	return sis,bro

if __name__ == '__main__':
	print(crossOver([1,2,3,4,5,6],[7,8,9,10,11,12],2))
