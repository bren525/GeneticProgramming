from pyevolve import G1DList
from pyevolve import GSimpleGA

from pyevolve import Mutators	
from pyevolve import Initializators	
string = 'Hello World!'
N = len(string)

def eval_func(chromosome):
	score = 10000

	for i in range(len(chromosome)):
		score-= abs(chromosome[i]-ord(string[i]))
	return score

genome = G1DList.G1DList(N)
genome.setParams(rangemin = 0, rangemax = 256)
genome.evaluator.set(eval_func)
genome.mutator.set(Mutators.G1DListMutatorIntegerRange)

ga = GSimpleGA.GSimpleGA(genome)
ga.setPopulationSize(20)
ga.setCrossoverRate(0.01)
ga.setMutationRate(0.02)
ga.setGenerations(5000)
ga.evolve(freq_stats=100)
print ga.bestIndividual()

best = []
for i in ga.bestIndividual():
	best.append(chr(i))
print best
#[72, 101, 108, 108, 111, 32, 87, 111, 114, 108, 100, 33]
