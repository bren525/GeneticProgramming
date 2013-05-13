import matplotlib.pyplot as plt
import time
import operator
import os
import sys
margin = 10

def plotting(results,saveVid = False,gen = -1,closestPoint=0):
	
	"""
	This first section of the code determines the dimensions
	of the plot based on how far the predator and prey traveled
	
	"""
	ypred=sorted(results, key=operator.itemgetter(1))
	yprey=sorted(results, key=operator.itemgetter(3))
	xpred=sorted(results, key=operator.itemgetter(0))
	xprey=sorted(results, key=operator.itemgetter(2))
	if ypred[0][1] < yprey[0][3]:
		ymin=ypred[0][1]-margin
	else:
		ymin=yprey[0][3]-margin
	if ypred[len(ypred)-1][1] > yprey[len(yprey)-1][3]:
		ymax=ypred[len(yprey)-1][1]+margin
	else:
		ymax=yprey[len(yprey)-1][3]+margin
	if xpred[0][0] < xprey[0][2]:
		xmin=xpred[0][0] -margin
	else:
		xmin=xprey[0][2]-margin
	if xpred[len(xpred)-1][0] > xprey[len(xprey)-1][2]:
		xmax=xpred[len(xpred)-1][0]+margin
	else:
		xmax=xprey[len(xprey)-1][2]+margin
	fig = plt.figure(figsize=(8,6))

	#plt.ylim(min(ymin,xmin),max(ymax,xmax))
	#plt.xlim(min(ymin,xmin),max(ymax,xmax))

	plt.ylim(ymin,ymax)
	plt.xlim(xmin,xmax)
	
	"""
	Animates the results by plotting a new point
	at each time step.
	"""
	os.system('mkdir gen'+str(gen)+'Dir')
	currentPath = os.path.abspath(sys.argv[0])
	currentDir = os.path.dirname(currentPath)
	gotCaught='No Catch'
	if len(results)<250:
		gotCaught='Caught'
	
	plt.ion()
	if gen != -1:
		plt.title('Generation '+str(gen)+' Best Pred vs Best Prey\n'
					+'Elapsed Time: '+str(len(results)) 
					+' Minimum Distance: '+str(closestPoint))
	else:
		plt.title('Elapsed Time: '+str(len(results)) 
					+' Minimum Distance: '+str(closestPoint))
	for i in range(0, len(results)+15):
		j = i
		if j > len(results) - 1:
			j = len(results) - 1
		plt.plot(results[j][0],results[j][1],'ro',markersize=7)
		plt.plot(results[j][2],results[j][3],'go',markersize=7)
		plt.draw()
		if saveVid: # Save each image
			desiredPath = os.path.join(currentDir,'gen'+str(gen)+'Dir\\img'+str(i))
			plt.savefig(desiredPath, ext = '.png')
	plt.close()
	# Creates and mp4 from images with x264 compression
	os.system('ffmpeg -y -f image2 -r 30 -i .\\gen'+str(gen)+'Dir\\img%d.png -c:v libx264 gen'+str(gen)+'.mp4')
