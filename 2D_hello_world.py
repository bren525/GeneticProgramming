from pyevolve import G1DList
from pyevolve import GSimpleGA
from pyevolve import G2DList
from pyevolve import Mutators	
from pyevolve import Initializators	
string = 'Hello World!'
N = len(string)

def eval_func(chromosome):
	score = 100000

	for i in range(len(chromosome)):
		score-= abs(chromosome[i]-ord(string[i]))
	return score

def eval_func2(chromosome):
	score = 100000

	for i in range(chromosome.getWidth()):
		score-= abs(chromosome[0][i]-ord(string[i]))
	for i in range(chromosome.getWidth()):
		score -= abs(chromosome[0][i]-chromosome[1][chromosome.getWidth()-1-i])
	return score

genome1 = G2DList.G2DList(2,N)
genome1.setParams(rangemin = 0, rangemax = 256)
genome1.evaluator.set(eval_func2)
genome1.mutator.set(Mutators.G2DListMutatorIntegerGaussian)

ga = GSimpleGA.GSimpleGA(genome1)

ga.setGenerations(2000)
ga.evolve(freq_stats=100)
print ga.bestIndividual()

best = []
print best
#[72, 101, 108, 108, 111, 32, 87, 111, 114, 108, 100, 33]
