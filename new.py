import numpy as np
import matplotlib.pyplot as plt
from functions import iteration,rank
import Physical_boundary_acquisition_test

k = 5
m = n =10
r = 4  # 点的个数
# plot1 = [16,201]
# plot2 = [103,268]
# plot3 = [227,108]
# plot4 = [139,41]
# plots = np.array([plot1,plot2,plot3,plot4])

plots = np.array(Physical_boundary_acquisition_test.boundary_coordinates)
plots = rank(plots)
print(plots)
# plots = np.random.random((4,2))
# plots = plots1[[0,3,1,2]]
# print(plots)
# plots[0] = plots1[0]
# plots[1] = plots1[3]
# plots[2] = plots1[1]
# plots[3] = plots1[2]

# print(plots[0][1])
# line1 = np.linspace(plots[3],plots[1],m)
# print(line1)
line = np.random.random((m,n))
arrx = np.random.random((m,n))
arry = np.random.random((m,n))
print(arrx[:][-1] )
arrx[0] = np.linspace(plots[0][0],plots[1][0],m)
arry[0] = np.linspace(plots[0][1], plots[1][1], n)
for j in range(0,m):
    arrx[j][-1] = np.linspace(plots[1][0],plots[2][0],m)[j]
    arry[j][-1] = np.linspace(plots[1][1], plots[2][1], n)[j]

arrx[-1][:] = np.linspace(plots[3][0], plots[2][0], m)
arry[-1][:] = np.linspace(plots[3][1], plots[2][1], n)
for j in range(0, m):
    arrx[j][0] = np.linspace(plots[0][0], plots[3][0], m)[j]
    arry[j][0] = np.linspace(plots[0][1], plots[3][1], n)[j]
print(arrx)
for i in range(0,5):
    print(i)
    iteration(arrx,arry)
plt.plot(arrx,arry,color = 'r')
plt.plot(np.transpose(arrx),np.transpose(arry),color = 'b')
plt.show()


# class block_meshing:
#     def __init__(self, plots,m,n):
#         self.plots = plots
#         self.m = m
#         self.n = n
#         self.interation_num = m*n
#
#     def mesh(self):
#         arrx = np.random.random((m, n))
#         arry = np.random.random((m, n))
#
#         arrx[0] = np.linspace(plots[0][0], plots[1][0], m)
#         arry[0] = np.linspace(plots[0][1], plots[1][1], n)
#         for j in range(0, m):
#             arrx[j][-1] = np.linspace(plots[1][0], plots[2][0], m)[j]
#             arry[j][-1] = np.linspace(plots[1][1], plots[2][1], n)[j]
#
#         arrx[-1][:] = np.linspace(plots[3][0], plots[2][0], m)
#         arry[-1][:] = np.linspace(plots[3][1], plots[2][1], n)
#         for j in range(0, m):
#             arrx[j][0] = np.linspace(plots[0][0], plots[3][0], m)[j]
#             arry[j][0] = np.linspace(plots[0][1], plots[3][1], n)[j]
#         for i in range(0, k):
#             print(i)
#             iteration(arrx, arry)
#         return arrx,arry


