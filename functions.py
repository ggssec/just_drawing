import numpy as np

#迭代
def iteration(arx,ary):
    n = arx.shape[0]
    m = arx.shape[1]
    # print(arx.shape)
    # print(n,m)
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


#逆时针排列点
def rank(plots):
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
    plot = plots[np.argsort(jiaodu,axis=0)]
    plot_sque = np.squeeze(plot)
    # print(np.hstack((plots,jiaodu)))
    # print(plot_sque)
    return plot_sque

#顶点分块划分
def block(plots):
    num_plots = np.shape(plots)[0]

    if num_plots == 4:
        return plots

    if num_plots%2 ==0 & num_plots == 4:
        num_group = int ((num_plots-4)/2+1)
        group_plots_init = plots[:4].copy()
        for i in range(1,num_group):
            group_plots_transient = np.array([plots[0],plots[2*i+1],plots[2*i+2],plots[2*i+3]])
            group_plots_transient = np.vstack((group_plots_init, group_plots_transient))
            group_plots_init = group_plots_transient.copy()
        group_plots_init = group_plots_init.reshape((num_group,4,2))
        return group_plots_init,num_group

    if num_plots%2 != 0:
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


# plots = np.array([[1,1],[2,2],[3,3],[4,4],[5,5],[6,6],[7,7],[8,8],[9,9]])
# plots,num_group = block(plots)
#
# # print(np.vstack((plots,plots)))
# print(plots)
# print(num_group)
