import numpy as np
import matplotlib.pyplot as plt
import math
import copy
import time
class tuoyuan():
    def __init__(self,center,plot_long,b,n,m):
        self.center = center
        self.plot_long = plot_long
        self.a = math.sqrt((center[0]-plot_long[0])**2+(center[1]-plot_long[1])**2)
        self.b = b
        self.n = n
        self.m = m
    def iteration(self, arx, ary, k):
        n = arx.shape[0]
        m = arx.shape[1]
        a = np.random.random((n, m))
        r = np.random.random((n, m))

        start = time.perf_counter()

        fig = plt.figure()
        plt.title('error')

        ax = fig.add_subplot(1, 1, 1)
        ax.set_title('title test', fontsize=12, color='r')

        y1 = []
        x1 = []

        for z in range(0, k * 100):
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
            y1.append((arx_precision.max() + ary_precision.max()) / 2)
            x1.append(z)
            ax.cla()  # 清除键
            ax.bar(x1, label='error', height=y1, width=1)
            ax.legend()
            plt.pause(0.001)
            # print(arx_precision.mean(),ary_precision.mean())
            if arx_precision.max() < 0.001 and ary_precision.max() < 0.001:
                print(arx_precision.max())
                print(ary_precision.max())
                end = time.perf_counter()
                print(end - start)
                break

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
        tuoyuan.picture(self, arx, ary)
        arx = np.vstack((arx, arx))
        ary = np.vstack((ary, 2 * center[1] - ary))
        jiedian_infor = np.vstack((arx, ary))
        return jiedian_infor
    def picture(self, arx, ary):
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        arx_ = arx
        ary_ = 2 * self.center[1] - ary
        plt.plot(arx, ary, color='r')
        plt.plot(arx_, ary_, color='r')
        plt.plot(np.transpose(arx), np.transpose(ary), color='b')
        plt.plot(np.transpose(arx_), np.transpose(ary_), color='b')
        plt.show()