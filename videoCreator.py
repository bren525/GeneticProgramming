from fitSim import testrun
import string
'''Samples log as desired and converts animations to video'''
log = open('5BestCoEvolveLog.txt','r')
counter = 0
br = []
by = []
gen = -1
for line in log:
	if counter < 721 and counter > 606:
		if counter % 6 == 1:
			gen = int(line.split(' ')[0])
		elif counter % 6 == 2:
			br = eval(string.join(line.split(' ')[1:9]))
		elif counter % 6 == 5:
			by = eval(string.join(line.split(' ')[1:9]))
			testrun(br,by,True,True,gen)
	counter+=1
	
