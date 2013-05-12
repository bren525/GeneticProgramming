import matplotlib.pyplot as plt
from numpy import linspace

log = open('Temp5Log.txt','r')

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

plt.plot(range(len(Av)),Av,'b-')
plt.plot(range(len(br)),br,'r-')
plt.plot(range(len(by)),by,'g-')
plt.show()
