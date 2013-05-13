import random
from genome import Gen

def crossOver(mom,dad,count=2):
	"""Takes in two genomes swaps their elements and produces one or two babies"""
	
	cut = random.randint(1, len(mom)-1) 	#picks random cut points
	
	if count <= 1:  	#produces one baby
		sis=mom[:]
		sis[cut:]=dad[cut:]
		sis = Gen(sis)
		return sis

	if count == 2:		#produces two babies
		sis=mom[:]
		sis[cut:]=dad[cut:]
		sis = Gen(sis)
		bro=dad[:]
		bro[cut:]=mom[cut:]
		bro = Gen(bro)
		return sis,bro
	
	

if __name__ == '__main__':
	print(crossOver([1,2,3,4,5,6],[7,8,9,10,11,12],2))
