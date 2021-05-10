import numpy as np
import matplotlib.pyplot as plt
from functions import iteration

# n = 100  #n：圆环份数
# m = 1000  #m: 直边份数
# r1 = 10
# r2 = 0
#
# # arrx = np.array([1]*m*n,dtype='f').reshape(m,n) #m行数
# # arry = np.array([1]*m*n,dtype='f').reshape(m,n)
#
# # arrx = np.random.random((m,n))
# # arry = np.random.random((m,n))
#
# arrx = np.linspace(-r1,r1,m*n).reshape(m,n)
# arry = np.linspace(0,r2,m*n).reshape(m,n)
#
# for i in range(0,m):
#     if i ==0:
#         for j in range(0,n):
#             jiaodu = np.pi/(n-1)*j
#             arrx[i][j] = np.cos(jiaodu)*r1
#             arry[i][j] = np.sin(jiaodu)*r1
#     elif i == m-1:
#         for j in range(0,n):
#             jiaodu = np.pi/(n-1)*j
#             arrx[i][j] = np.cos(jiaodu)*r2
#             arry[i][j] = np.sin(jiaodu)*r2
#     else:
#         arrx[i][0] = (r1-r2)/(m-1)*(m-1-i)+r2
#         arry[i][0] = 0
#         arrx[i][n-1] = -(r1-r2)/(m-1)*(m-1-i)-r2
#         arry[i][n-1] = 0
#
# # iteration(arrx, arry)
# for i in range(0,10):
#     iteration(arrx, arry)
#
# print(arrx)
# print(arry)
# plt.plot(arrx,arry,color = 'r')
# plt.plot(np.transpose(arrx),np.transpose(arry),color = 'b')
# plt.show()


class circular():

    def __init__(self,plots,m,n):
        self.plots = np.array(plots).reshape((4,2))
        self.m = m
        self.n = n

    def feature(self):
        center = self.plots.mean(axis=0)
        radius2 = self.plots[0]-center
        radius = np.sqrt((radius2[0]**2+radius2[1]**2))
        return center,radius

    def mesh(self,k):
        r2 = 0
        center,radius = circular.feature(self)
        n = self.n
        m = self.m

        arrx = np.linspace(-radius, radius, m * n).reshape(m, n) +center[0]
        arry = np.linspace(0, r2, m * n).reshape(m, n) +center[1]
        for i in range(0, m):
            if i == 0:
                for j in range(0, n):
                    jiaodu = np.pi / (n - 1) * j
                    arrx[i][j] = np.cos(jiaodu) * radius + center[0]
                    arry[i][j] = np.sin(jiaodu) * radius + center[1]
            elif i == m - 1:
                for j in range(0, n):
                    jiaodu = np.pi / (n - 1) * j
                    arrx[i][j] = np.cos(jiaodu) * r2+ center[0]
                    arry[i][j] = np.sin(jiaodu) * r2+ center[1]
            else:
                arrx[i][0] = (radius - r2) / (m - 1) * (m - 1 - i) + r2 +center[0]
                arry[i][0] = 0+center[1]
                arrx[i][n - 1] = -(radius - r2) / (m - 1) * (m - 1 - i) - r2 +center[0]
                arry[i][n - 1] = 0 +center[1]

        arx,ary = circular.iteration(self,arrx,arry,k)
        # arx_ = np.ones_like(arx)
        # ary_ = np.ones_like(ary)
        # arx_ = center[0] - arrx
        # ary_ = center[1] - arry
        # arx = np.vstack((arrx,arx_))
        # ary = np.vstack((arry, ary_))
        circular.picture(self,arx,ary)


    def iteration(self, arx, ary,k):
            n = arx.shape[0]
            m = arx.shape[1]
            # print(arx.shape)
            # print(n, m)
            a = np.random.random((n, m))
            r = np.random.random((n, m))
            for z in range(0, k*100):
                for i in range(1, n - 1):
                    for j in range(1, m - 1):
                        a[i][j] = ((arx[i][j + 1] - arx[i][j - 1]) ** 2 + (ary[i][j + 1] - ary[i][j - 1]) ** 2) / 4
                        r[i][j] = ((arx[i + 1][j] - arx[i - 1][j]) ** 2 + (ary[i + 1][j] - ary[i - 1][j]) ** 2) / 4
                        arx[i][j] = 1 / (2 * (a[i][j] + r[i][j])) * (
                                a[i][j] * (arx[i + 1][j] + arx[i - 1][j]) + r[i][j] * (arx[i][j + 1] + arx[i][j - 1]))
                        ary[i][j] = 1 / (2 * (a[i][j] + r[i][j])) * (
                                a[i][j] * (ary[i + 1][j] + ary[i - 1][j]) + r[i][j] * (ary[i][j + 1] + ary[i][j - 1]))
                # print(z)
            return arx, ary

    def picture(self,arx,ary):
        center, radius = circular.feature(self)
        arx_ =  arx
        ary_ = 2*center[1] - ary
        plt.plot(arx, ary, color='r')
        plt.plot(arx_,ary_,color = 'r')
        plt.plot(np.transpose(arx), np.transpose(ary), color='b')
        plt.plot(np.transpose(arx_), np.transpose(ary_), color='b')
        plt.show()

# plots = np.array([[3,2],[2,3],[1,2],[2,1]]).reshape((4,2))
# a = circular(plots,30,30)
# center,r2 = a.feature()
# print(center[0])
# a.mesh(3)