
import numpy as np
import matplotlib.pyplot as plt
from functions import iteration,rank,block
import copy
import datetime
# import Physical_boundary_acquisition_test

class block_meshing:
    def __init__(self, plots, m, n):
        self.plots = plots
        self.m = m
        self.n = n
        # self.k = k
        self.ctem_num = m * n

    def mesh(self,k):
        # start_time = datetime.datetime.now()
        m = self.m
        n = self.n
        plots = self.plots
        plots = block_meshing.group(self)
        arrx = np.random.random((m, n))
        arry = np.random.random((m, n))

        arrx[0] = np.linspace(plots[0][0], plots[1][0], m)
        arry[0] = np.linspace(plots[0][1], plots[1][1], n)
        for j in range(0, m):
            arrx[j][-1] = np.linspace(plots[1][0], plots[2][0], m)[j]
            arry[j][-1] = np.linspace(plots[1][1], plots[2][1], n)[j]

        arrx[-1][:] = np.linspace(plots[3][0], plots[2][0], m)
        arry[-1][:] = np.linspace(plots[3][1], plots[2][1], n)
        for j in range(0, m):
            arrx[j][0] = np.linspace(plots[0][0], plots[3][0], m)[j]
            arry[j][0] = np.linspace(plots[0][1], plots[3][1], n)[j]

        self.iteration(arrx,arry,k)
        self.picture(arrx,arry)
        # end_time = datetime.datetime.now()
        # print("迭代用时" + str(end_time - start_time))
        jiedian_infor = np.vstack((arrx, arry))
        return jiedian_infor

    def group(self):
        plots = rank(self.plots)
        return plots


    def iteration(self, arx, ary,k):

        canshu = 0

        n = arx.shape[0]
        m = arx.shape[1]
        # print(arx.shape)
        # print(n, m)
        a = np.random.random((n, m))
        r = np.random.random((n, m))

        #绘制动态图
        fig = plt.figure()
        plt.title('error')

        ax = fig.add_subplot(1, 1, 1)
        ax.set_title('title test', fontsize=12, color='r')

        plt.xlabel('迭代次数')
        plt.ylabel('error')

        y1 = []
        x1 = []

        for z in range(0, k*100):

            arx_before = copy.deepcopy(arx[1:n - 1, 1:m - 1])
            ary_before = copy.deepcopy(ary[1:n - 1, 1:m - 1])

            for i in range(1, n - 1):
                for j in range(1, m - 1):
                    a[i][j] = ((arx[i][j + 1] - arx[i][j - 1]) ** 2 + (ary[i][j + 1] - ary[i][j - 1]) ** 2) / 4
                    r[i][j] = ((arx[i + 1][j] - arx[i - 1][j]) ** 2 + (ary[i + 1][j] - ary[i - 1][j]) ** 2) / 4
                    arx[i][j] = 1 / (2 * (a[i][j] + r[i][j])) * (
                                a[i][j] * (arx[i + 1][j] + arx[i - 1][j]) + r[i][j] * (arx[i][j + 1] + arx[i][j - 1]))
                    ary[i][j] = 1 / (2 * (a[i][j] + r[i][j])) * (
                                a[i][j] * (ary[i + 1][j] + ary[i - 1][j]) + r[i][j] * (ary[i][j + 1] + ary[i][j - 1]))

             # 判断迭代收敛，终止循环
            arx_precision = abs((arx_before - arx[1:n - 1, 1:m - 1]) / arx_before)
            ary_precision = abs((ary_before - ary[1:n - 1, 1:m - 1]) / ary_before)

            # arx_precision.mean()
            # ary_precision.mean()

            print(arx_precision.mean(), ary_precision.mean())
            if arx_precision.max() < 0.0001 and ary_precision.max() < 0.0001:
                canshu += 1

            if z!=0:
                y1.append((arx_precision.max() + ary_precision.max()) / 2)
                x1.append(z)
                ax.cla()  # 清除键
                ax.bar(x1, label='error', height=y1, width=1)
                ax.legend()
                plt.pause(0.001)

            if canshu ==1:
                print(z)
                # end = time.perf_counter()
                # print(end - start)
                break


        return arx, ary

    def picture(self,arx,ary):
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        plt.plot(arx, ary, color='r')
        plt.plot(np.transpose(arx), np.transpose(ary), color='b')
        plt.show()



# plots = [[0,1],[1,0],[1,1],[0,0]]
# plots = np.array(plots)
# a = block_meshing(plots,10,10)
# a.mesh(10)
# def main():
# plots = np.array(Physical_boundary_acquisition_test.boundary_coordinates1)
# mesh1 = block_meshing(plots,10,10)
# mesh1.mesh(10)
# if __name__ == '__main__':
#     k = 10
#     m = n = 10
# plots = np.array(Physical_boundary_acquisition.boundary_coordinates)
#     # plots = rank(plots)
#     # plots = block(plots)
#     if plots.shape[0] == 4:
#         mesh1 = block_meshing(plots,m,n)
#         arrx,arry = mesh1.mesh()
#         print(arrx)
#         plt.plot(arrx,arry,color = 'r')
#         plt.plot(np.transpose(arrx),np.transpose(arry),color = 'b')
#         plt.show()