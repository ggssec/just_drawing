import numpy as np
import copy
import matplotlib.pyplot as plt

#迭代
def iteration(arx,ary):
    n = arx.shape[0]
    m = arx.shape[1]
    a = np.random.random((n,m))
    r = np.random.random((n,m))
    for k in range(0,100):
        for i in range(1,n-1):
            for j in range(1,m-1):
                     a[i][j] = ((arx[i][j+1]-arx[i][j-1])**2+(ary[i][j+1]-ary[i][j-1])**2)/4
                     r[i][j] = ((arx[i+1][j]-arx[i-1][j])**2+(ary[i+1][j]-ary[i-1][j])**2)/4
                     arx[i][j] = 1/(2*(a[i][j]+r[i][j]))*(a[i][j]*(arx[i+1][j]+arx[i-1][j])+r[i][j]*(arx[i][j+1]+arx[i][j-1]))
                     ary[i][j] = 1/(2*(a[i][j]+r[i][j]))*(a[i][j]*(ary[i+1][j]+ary[i-1][j])+r[i][j]*(ary[i][j+1]+ary[i][j-1]))
    return (arx,ary)

def rank(plots):
    plots = np.array(plots)
    center = plots.mean(axis= 0)
    jiaodu = np.ones((plots.shape[0],1),dtype='f')
    for i in range(0,plots.shape[0]):
        if (plots[i][1] >center[1]) and (plots[i][0] >center[0]):
            jiaodu[i] = np.arctan((center[1]-plots[i][1])/(center[0]-plots[i][0]))
        elif (plots[i][1] > center[1]) & (plots[i][0] < center[0]):
            jiaodu[i] = np.arctan(abs((center[1]-plots[i,1])/(center[0]-plots[i,0]))) + np.pi/2
        elif (plots[i][1] < center[1]) & (plots[i][0] < center[0]):
            jiaodu[i] = np.arctan(abs((center[1]-plots[i,1])/(center[0]-plots[i,0]))) + np.pi/2*2
        elif (plots[i][1] < center[1]) & (plots[i][0] > center[0]):
            jiaodu[i] = np.arctan(abs((center[1]-plots[i,1])/(center[0]-plots[i,0]))) + np.pi/2*3
        elif plots[i][0] == center[0] and plots[i][1]>center[1]:
            jiaodu[i] = 0
        elif plots[i][0] == center[0] and plots[i][1]<center[1]:
            jiaodu[i] = np.pi
        elif plots[i][1] == center[1] and plots[i][0]>center[0]:
            jiaodu[i] = np.pi/2
        elif plots[i][1] == center[1] and plots[i][0]<center[0]:
            jiaodu[i] = np.pi*3/2
    plot = plots[np.argsort(jiaodu,axis=0)]
    plot_sque = np.squeeze(plot)
    return plot_sque

def block(plots):
    # plots = np.array(plots)
    num_plots = np.shape(plots)[0]
    if num_plots == 4:
        num_group =1
        return plots,num_group
    elif num_plots%2 ==0 and num_plots != 4:
        num_group = int ((num_plots-4)/2+1)
        group_plots_init = plots[:4].copy()
        for i in range(1,num_group):
            group_plots_transient = np.array([plots[0],plots[2*i+1],plots[2*i+2],plots[2*i+3]])
            group_plots_transient = np.vstack((group_plots_init, group_plots_transient))
            group_plots_init = group_plots_transient.copy()
        group_plots_init = group_plots_init.reshape((num_group,4,2))
        return group_plots_init,num_group
    elif num_plots%2 != 0:
        num_group = int((num_plots +1- 4) / 2 + 1)
        group_plots_init = plots[:4].copy()
        if num_group>2:
            for i in range(1,num_group-2):
                group_plots_transient = np.array([plots[0], plots[2 * i + 1], plots[2 * i + 2], plots[2 * i + 3]])
                group_plots_transient = np.vstack((group_plots_init, group_plots_transient))
                group_plots_init = group_plots_transient.copy()
            plots = np.array([plots[0],plots[-4],plots[-3],plots[-2],plots[-1]])
            ploti = (plots[2] + plots[3]) / 2
            group_plots_transient = np.array([plots[0], plots[1], plots[2], ploti])
            group_plots_transient = np.vstack((group_plots_init, group_plots_transient))
            group_plots_init = group_plots_transient.copy()
            group_plots_transient = np.array([plots[0], ploti, plots[2], plots[4]])
            group_plots_transient = np.vstack((group_plots_init, group_plots_transient))
            group_plots_init = group_plots_transient.copy()
            group_plots_init = group_plots_init.reshape((num_group, 4, 2))
            return group_plots_init, num_group
        else:
            ploti = (plots[2] + plots[3])/2
            group_plots_init = np.array([plots[0],plots[1],plots[2],ploti])
            group_plots_transient = np.array([plots[0],ploti,plots[3],plots[4]])
            group_plots_transient = np.vstack((group_plots_init, group_plots_transient))
            group_plots_init = group_plots_transient.copy()
            group_plots_init = group_plots_init.reshape((num_group, 4, 2))
            return group_plots_init,num_group

def ementqulity(arx,ary):
    x_areas = np.array([])
    y_areas = np.array([[]])
    for j in range(0,arx.shape[0]-1):
        x_areas = np.array([])
        for i in range(0,arx.shape[1]-1):

            print(i)
            a = np.sqrt((arx[j][i]-arx[j][i+1])**2+(ary[j][i]-ary[j][i+1])**2)
            c = np.sqrt((arx[j+1][i]-arx[j+1][i+1])**2+(ary[j+1][i]-ary[j+1][i+1])**2)
            b = np.sqrt((arx[j+1][i]-arx[j][i])**2+(ary[j+1][i]-ary[j][i])**2)
            d = np.sqrt((arx[j+1][i+1]-arx[j][i+1])**2+(ary[j+1][i+1]-ary[j][i+1])**2)
            e = np.sqrt((arx[j][i]-arx[j+1][i+1])**2+(ary[j][i]-ary[j+1][i+1])**2)
            f = np.sqrt((arx[j][i+1]-arx[j+1][i])**2+(ary[j][i+1]-ary[j+1][i])**2)
            tem_x_areas = np.sqrt(4*e**2*f**2-(a**2-b**2+c**2-d**2)**2)/4
            x_areas = np.hstack((x_areas,tem_x_areas))
            # print(tem_x_areas)

        if j == 0:
            areas = copy.copy(x_areas)
        else:
            areas = np.vstack((areas,x_areas))

        # print('1')
    return areas

#图形重绘
def drawing(jiedian):
    arx = jiedian[:int(jiedian.shape[0]/2)]
    ary = jiedian[int(jiedian.shape[0]/2):]
    plt.plot(arx, ary, color='r')
    plt.plot(np.transpose(arx), np.transpose(ary), color='b')
    plt.show()






