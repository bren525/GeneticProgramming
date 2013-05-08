from copy import copy
def forwardEuler(func,init,length):
	result = [copy(init)]
	lastStep = init
	for i in range(length):
		change = func(lastStep,i)
		for j in range(len(lastStep)):
			lastStep[j] += change[j]
		result.append(copy(lastStep))
	return result
