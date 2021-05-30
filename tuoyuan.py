import numpy as np
import matplotlib.pyplot as plt

class tuoyuan():

    def __init__(self,center,a,b,n,m):
        self.center = center
        self.a = a
        self.b = b
        self.n = n
        self.m = m


    # def __int__(self,plots,m,n):
    #     self.plots = plots
    #     self.a = abs(plots[0,0]-plots[1,0])/2
    #     self.b = abs(plots[2,1]-plots[3,1])/2
    #     self.n = n
    #     self.m = m

    def iteration(self, arx, ary, k):
        n = arx.shape[0]
        m = arx.shape[1]
        # print(arx.shape)
        # print(n, m)
        a = np.random.random((n, m))
        r = np.random.random((n, m))
        for z in range(0, k * 100):
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

    def mesh(self, k):
        r2 = 0
        center, a, b = self.center,self.a,self.b
        n = self.n
        m = self.m

        arrx = np.linspace(-a, b, m * n).reshape(m, n) + center[0]
        arry = np.linspace(0, b, m * n).reshape(m, n) + center[1]
        for i in range(0, m):
            if i == 0:
                for j in range(0, n):
                    jiaodu = np.pi / (n - 1) * j
                    arrx[i][j] = np.cos(jiaodu) * a + center[0]
                    arry[i][j] = np.sin(jiaodu) * b + center[1]
            elif i == m - 1:
                for j in range(0, n):
                    jiaodu = np.pi / (n - 1) * j
                    arrx[i][j] = np.cos(jiaodu) * r2 + center[0]
                    arry[i][j] = np.sin(jiaodu) * r2 + center[1]
            else:
                arrx[i][0] = (a - r2) / (m - 1) * (m - 1 - i) + r2 + center[0]
                arry[i][0] = 0 + center[1]
                arrx[i][n - 1] = -(a - r2) / (m - 1) * (m - 1 - i) - r2 + center[0]
                arry[i][n - 1] = 0 + center[1]

        arx, ary = tuoyuan.iteration(self, arrx, arry, k)
        # arx_ = np.ones_like(arx)
        # ary_ = np.ones_like(ary)
        # arx_ = center[0] - arrx
        # ary_ = center[1] - arry
        # arx = np.vstack((arrx,arx_))
        # ary = np.vstack((arry, ary_))
        tuoyuan.picture(self, arx, ary)

    def picture(self, arx, ary):

        arx_ = arx
        ary_ = 2 * self.center[1] - ary
        plt.plot(arx, ary, color='r')
        plt.plot(arx_, ary_, color='r')
        plt.plot(np.transpose(arx), np.transpose(ary), color='b')
        plt.plot(np.transpose(arx_), np.transpose(ary_), color='b')
        plt.show()

# plots = np.array([[3,2],[2,3],[1,2],[2,1]]).reshape((4,2))
# a = circular(plots,30,30)
# center,r2 = a.feature()
# print(center[0])
# a.mesh(3)
# x = tuoyuan([1,2],2,1,50,50)
# x.mesh(5)
# plots = [[-2,0],[2,0],[0,1],[0,-1]]
# x = tuoyuan(plots,10,10)
# x.mesh(10)