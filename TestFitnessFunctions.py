def testFitFunc(rpop,ypop):
	"""
	Scores each list based on the
	number of zeros it contains
	"""

	for r in rpop:
		score = 0
		for p in r:
			if p == 0:
				score +=1
		r.rawScore = score
		
	for y in ypop:
		score = 0
		for p in y:
			if p == 0:
				score +=1
		y.rawScore = score

def testFitFunc2(rpop,ypop):
		
	"""
	Scores each r in rpop based on how far
	each element in its list is from
	the corresponding element in each y in
	ypop list, and vice versa
	"""
	
	size = len(rpop[0])
	for r in rpop:
		for y in ypop:
			for i in range(size):
				r.rawScore += abs(r[i]-y[i])
				y.rawScore += abs(r[i]-y[i])
				
				
