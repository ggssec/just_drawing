# -*- coding:utf-8 -*-
"""
作者：陈昊卓
日期：2021年04月13日
"""
import numpy as np
import cv2
import json
import tkinter as tk
from tkinter import filedialog
import os
import copy

import looking_for_vertices


# 读取中文路径文件
def cv_imread(file_path):
    root_dir, file_name = os.path.split(file_path)
    pwd = os.getcwd()
    if root_dir:
        os.chdir(root_dir)
    cv_img = cv2.imread(file_name, 0)
    os.chdir(pwd)
    return cv_img


# 降低像素密度
def Decrease_pixel_density(image):
    image2 = np.zeros((int(len(image) / 3), int(len(image[0]) / 3)), np.uint8)  # image2 是降低像素后的图片矩阵
    for i_2, i in enumerate(range(1, len(image) - 1, 3)):
        for j_2, j in enumerate(range(1, len(image[0]) - 1, 3)):
            if int(image[i, j]) + int(image[i, j - 1]) + int(image[i, j + 1]) + int(image[i - 1, j - 1]) + int(
                    image[i - 1, j]) + int(image[i - 1, j + 1]) + int(image[i + 1, j - 1]) + int(image[i + 1, j]) + int(
                image[i + 1, j + 1]) >= 255 * 2:
                image2[i_2, j_2] = 255
            else:
                image2[i_2, j_2] = 0
    # cv2.imshow("image2", image2)
    return image2


# 打开选择文件的对话框
root = tk.Tk()
root.withdraw()
Filepath = filedialog.askopenfilename()  # 获得选好的文件

image = cv_imread(Filepath)
# cv2.imshow("image", image)
h, w = image.shape[:]
boundary_coordinates = [[]]
num_edges = 1  # 多边形的边数

# 手动输入图形类别
while True:
    print("请选择图形类别：\n", "\tA:正放矩形\n", "\tB:正放椭圆形（圆形）\n", "\tC:多边形\n", "\tD:斜放矩形\n")
    select = input()
    if select == "A":
        print("图形为矩形")
        break
    elif select == "B":
        print("图形为正放椭圆形（圆形）")
        break
    elif select == "C":
        print("请输入边数：")
        num_edges = input()  # 多边形的边数
        print("图形为" + str(num_edges) + "边形")
        num_edges = int(num_edges)
        break
    elif select == "D":
        print("图形为斜放矩形")
        break
    else:
        print("输入内容有误，请重新输入！")

# 针对不同图形进行顶点获取
if select == "A":  # 正放矩形
    image = Decrease_pixel_density(image)  # 降低像素密度
    looking_for_vertices1 = looking_for_vertices.LookingForVertices(image)  # 新对象
    boundary_coordinates = looking_for_vertices1.Extract_rectangular_1(image)  # 获取顶点坐标信息
elif select == "B":  # 圆形矩形
    image = Decrease_pixel_density(image)  # 降低像素密度
    looking_for_vertices1 = looking_for_vertices.LookingForVertices(image)  # 新对象
    boundary_coordinates = looking_for_vertices1.Extract_circle(image)  # 获取顶点坐标信息
elif select == "C":  # 多边形
    image = Decrease_pixel_density(image)  # 降低像素密度
    looking_for_vertices1 = looking_for_vertices.LookingForVertices(image)  # 新对象
    import image_segmentation

    a, b = image_segmentation.ImageSegmentation(num_edges, image)  # 根据边数切割图像
    boundary_coordinates = looking_for_vertices1.Extract_polygon(image)  # 获取顶点坐标信息
elif select == "D":  # 斜放矩形
    image = Decrease_pixel_density(image)  # 降低像素密度
    looking_for_vertices1 = looking_for_vertices.LookingForVertices(image)  # 新对象
    boundary_coordinates = looking_for_vertices1.Extract_rectangular_2_fast(image)  # 获取顶点坐标信息

del boundary_coordinates[0]  # 删除坐标列表中的第一个元素
filename = 'boundary_coordinates.json'  # 建立存储坐标值的json文件
with open(filename, 'w') as f_obj:  # 以能够写入的方式打开该json文件
    json.dump(boundary_coordinates, f_obj)  # 将坐标列表写入该json文件


def change_coordinate(h, boundary_coordinates):
    boundary_coordinates1 = copy.deepcopy(boundary_coordinates)
    for i in range(len(boundary_coordinates)):
       # print(boundary_coordinates[i,0])
        boundary_coordinates1[i][0] = h - boundary_coordinates[i][0]

    filename1 = 'boundary_coordinates1.json'
    with open(filename1, 'w') as f_obj1:
        json.dump(boundary_coordinates1, f_obj1)
    return boundary_coordinates1


boundary_coordinates1 = change_coordinate(h, boundary_coordinates)

# cv2.waitKey(0)

# # 测试使用
# filename = 'boundary_coordinates.json'
# with open(filename) as f:
#     plot = json.load(f)
# print(len(plot))
# arplot = np.array(plot)
# [arx, ary] = np.hsplit(arplot, 2)
# print(arx.transpose())
# print()
# plt.plot(ary, -arx, 'b*')
# plt.show()
