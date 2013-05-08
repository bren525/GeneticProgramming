import matplotlib.pyplot as plt
import time
import operator

def plotting(results):
	ycheck=sorted(results, key=operator.itemgetter(1))
	ychecker=sorted(results, key=operator.itemgetter(3))
	xcheck=sorted(results, key=operator.itemgetter(0))
	xchecker=sorted(results, key=operator.itemgetter(2))
	if ycheck[0][1] < ychecker[0][3]:
		ymin=ycheck[0][1]-50
	else:
		ymin=ychecker[0][3]-50
	if ycheck[len(ycheck)-1][1] > ychecker[len(ychecker)-1][3]:
		ymax=ycheck[len(ycheck)-1][1]+50
	else:
		ymax=ychecker[len(ychecker)-1][3]+50
	if xcheck[0][0] < xchecker[0][2]:
		xmin=xcheck[0][0] -50
	else:
		xmin=xchecker[0][2]-50
	if xcheck[len(xcheck)-1][0] > xchecker[len(xchecker)-1][2]:
		xmax=xcheck[len(xcheck)-1][0]+50
	else:
		xmax=xchecker[len(xchecker)-1][2]+50
	fig = plt.figure(figsize=(8,6))
	plt.ylim((ymin,ymax))
	plt.xlim((xmin,xmax))
	plt.ion()
	for i in range(0, len(results)):   
		plt.plot(results[i][0],results[i][1],'ro',markersize=7)
		plt.plot(results[i][2],results[i][3],'go',markersize=7)
		plt.draw()
		#time.sleep(0.001)
	plt.show(1)
if __name__ == '__main__':

    print('BRENDAN is a poopyhead')
