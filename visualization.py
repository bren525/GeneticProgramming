import matplotlib.pyplot as plt
import time


def plotting(results):
    fig = plt.figure(figsize=(8,6))
    plt.ylim((-500,500))
    plt.xlim((-500,500))
    plt.ion()
    for i in range(0, len(results)):   
        plt.plot(results[i][0],results[i][1],'ro',markersize=4)
        plt.plot(results[i][2],results[i][3],'bo',markersize=4)
        # print ('plot work!')
        plt.draw()
        time.sleep(0.1)
    plt.show(20)    

if __name__ == '__main__':

    print('BRENDAN is a poopyhead')
