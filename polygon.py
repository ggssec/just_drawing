import numpy as np
import matplotlib.pyplot as plt
from functions import iteration,rank,block
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
        for i in range(0, k):
            # print(i)
            block_meshing.iteration(self,arrx,arry)
        block_meshing.picture(self,arrx,arry)
        # end_time = datetime.datetime.now()
        # print("迭代用时" + str(end_time - start_time))
        return arrx, arry

    def group(self):
        plots = rank(self.plots)
        return plots


    def iteration(self, arx, ary):
        n = arx.shape[0]
        m = arx.shape[1]
        # print(arx.shape)
        # print(n, m)
        a = np.random.random((n, m))
        r = np.random.random((n, m))
        for k in range(0, m * n):
            for i in range(1, n - 1):
                for j in range(1, m - 1):
                    a[i][j] = ((arx[i][j + 1] - arx[i][j - 1]) ** 2 + (ary[i][j + 1] - ary[i][j - 1]) ** 2) / 4
                    r[i][j] = ((arx[i + 1][j] - arx[i - 1][j]) ** 2 + (ary[i + 1][j] - ary[i - 1][j]) ** 2) / 4
                    arx[i][j] = 1 / (2 * (a[i][j] + r[i][j])) * (
                                a[i][j] * (arx[i + 1][j] + arx[i - 1][j]) + r[i][j] * (arx[i][j + 1] + arx[i][j - 1]))
                    ary[i][j] = 1 / (2 * (a[i][j] + r[i][j])) * (
                                a[i][j] * (ary[i + 1][j] + ary[i - 1][j]) + r[i][j] * (ary[i][j + 1] + ary[i][j - 1]))
        return arx, ary

    def picture(self,arx,ary):
        plt.plot(arx, ary, color='r')
        plt.plot(np.transpose(arx), np.transpose(ary), color='b')
        plt.show()
# def main():
# plots = np.array(Physical_boundary_acquisition_test.boundary_coordinates1)
# mesh1 = block_meshing(plots,10,10)
# mesh1.mesh(10)
# if __name__ == '__main__':
#     k = 10
#     m = n = 10
#     plots = np.array(Physical_boundary_acquisition.boundary_coordinates)
#     # plots = rank(plots)
#     # plots = block(plots)
#     if plots.shape[0] == 4:
#         mesh1 = block_meshing(plots,m,n)
#         arrx,arry = mesh1.mesh()
#         print(arrx)
#         plt.plot(arrx,arry,color = 'r')
#         plt.plot(np.transpose(arrx),np.transpose(arry),color = 'b')
#         plt.show()