def testFitFunc(rpop,ypop):
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
	size = len(rpop[0])
	for r in rpop:
		for y in ypop:
			for i in range(size):
				r.rawScore += abs(r[i]-y[i])
				y.rawScore += abs(r[i]-y[i])
				
				
