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
