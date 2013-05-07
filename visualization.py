import matplotlib.pyplot as plt
import time

pred = ([1,2],[2,3],[2.5,3.25],[3,3.75],[3.5,4])
prey = ([20,15],[19.5,14],[18,14],[17.8,13.5],[19,12])

def createlists():
    pred_x = []
    pred_y = []
    prey_x = []
    prey_y = []

    for i in range(0, 4):
        prey_x.append(prey[i][0])
        prey_y.append(prey[i][1])
        pred_x.append(pred[i][0])
        pred_y.append(pred[i][1])
        i += 1
    return [pred_x, pred_y, prey_x, prey_y]

def plotting(pred, prey):
    fig = plt.figure()
    plt.ion()
    for i in range(0, len(pred)):   
        print (prey[i][0],prey[i][1])
        plt.plot(prey[i][0],prey[i][1],'ro')
        plt.plot(pred[i][0],pred[i][1],'bo')
        print ('plot work!')
        plt.draw()
        time.sleep(3)

if __name__ == '__main__':
    a=createlists()
    plotting(pred,prey)
