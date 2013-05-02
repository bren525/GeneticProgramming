import random

def crossOver(mom,dad,count):
	"""Takes in two genomes swaps their elements and produces two babies"""
	
	cut = random.randint(1, len(mom)-1)
	
	if count >= 1:
		sis=mom.clone()
		sis[cut:]=dad[cut:]
	if count == 2:
		bro=dad.clone()
		bro[cut:]=dad[cut:]
	
return bro,sis

if __name__ == '__main__':
	print(crossOver([1,3,5,8],[2,4,7,9],2))
