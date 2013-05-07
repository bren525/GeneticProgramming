
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D

# def data_gen():
# 	# prey = ([1,4],[5,1],[20,11])
# 	# pred = ([4,9],[1,2],[11,13])
#     t = data_gen.t
#     cnt = 0
#     while cnt < 1000:
#         cnt += 1
#         t += 0.05
#         yield t, np.sin(2*np.pi*t) * np.exp(-t/10.)
# data_gen.t = 0

def DataGen_Prey():
	prey = ([1,4],[5,1],[20,11])
	for i in range(0, 3):
		prey_x = prey[i][0]
		prey_y = prey[i][1]
		plt.setp(line1, color='b',linewidth=2.0)
        
		yield prey_x, prey_y

		
def DataGen_Predator():
	pred = ([4,9],[1,2],[11,13])
	for i in range(0, 3):
		pred_x = pred[i][0]
		pred_y = pred[i][1]
		plt.setp(line2, color='r',linewidth=2.0)  
        # plt.gca().set_color_cycle(['blue'])
		yield pred_x, pred_y

fig = plt.figure()
ax = fig.add_subplot(111)
line1, = ax.plot([], [], lw=2)
line2, = ax.plot([], [], lw=2)
ax.set_ylim(0, 15)
ax.set_xlim(0, 21)
ax.grid()
xdata, ydata = [], []
# plt.gca().set_color_cycle(['red', 'green', 'blue', 'yellow'])
# colors = plt.cm.jet(np.linspace(0,1,))

def run(data1):
    # update the data
    prey_x,prey_y = data1
    xdata.append(prey_x)
    ydata.append(prey_y)
    xmin, xmax = ax.get_xlim()
    ax.figure.canvas.draw()
    # if prey_x >= xmax:
    #     ax.set_xlim(xmin, 2*xmax)
    #     ax.figure.canvas.draw()
    line1.set_data(xdata, ydata)

    return line1,

def run2(data2):
    # update the data
    pred_x,pred_y = data2
    xdata.append(pred_x)
    ydata.append(pred_y)
    xmin, xmax = ax.get_xlim()
    # ax.figure.canvas.draw()
    # if pred >= xmax:
    #     ax.set_xlim(xmin, 2*xmax)
    #     ax.figure.canvas.draw()
    line2.set_data(xdata, ydata)
    

    return line2,

ani = animation.FuncAnimation(fig, run, DataGen_Prey, blit=True, interval=1000,
    repeat=False)
ani2 = animation.FuncAnimation(fig, run2, DataGen_Predator, blit=True, interval=1000,
    repeat=False)
# plt.plot([1,2],[2,14],'r.')
plt.show()




