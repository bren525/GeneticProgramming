import matplotlib.pyplot as plt
from numpy import linspace

log = open('2BestCoEvolveLog.txt','r')

gen = range(10001)
Av = []
br = []
by = []
counter = 0
for line in log:
	if counter % 6 == 1:
		Av.append(float(line.split(' ')[3]))
	elif counter % 6 == 2:
		br.append(float(line.split(']')[1][1:]))
	elif counter % 6 == 5:
		by.append(float(line.split(']')[1][1:]))
	counter +=1
print(len(Av),len(gen))
plt.plot(gen,Av,'b-')
plt.plot(gen,br,'r-')
plt.plot(gen,by,'g-')
plt.show()
