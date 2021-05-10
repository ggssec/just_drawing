# -*- coding:utf-8 -*-
"""
作者：陈昊卓
日期：2021年04月23日
"""
import numpy as np
import cv2
import json
# import tkinter as tk
# from tkinter import filedialog
import os
import copy
import datetime
from itertools import product


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

    # start_time = datetime.datetime.now()

    for i_2, i in enumerate(range(1, len(image) - 1, 3)):
        for j_2, j in enumerate(range(1, len(image[0]) - 1, 3)):
            if int(image[i, j]) + int(image[i, j - 1]) + int(image[i, j + 1]) + int(image[i - 1, j - 1]) + int(image[i - 1, j]) + int(image[i - 1, j + 1]) + int(image[i + 1, j - 1]) + int(image[i + 1, j]) + int(image[i + 1, j + 1]) >= 255 * 2:
                image2[i_2, j_2] = 255
            else:
                image2[i_2, j_2] = 0
        # end_time = datetime.datetime.now()
        # print("降低像素密度用时" + str(end_time - start_time))
    return image2


# 生成boundary_coordinates文件
def save_boundary_coordinates(boundary_coordinates):
    del boundary_coordinates[0]
    filename = 'boundary_coordinates.json'
    with open(filename, 'w') as f_obj:
        json.dump(boundary_coordinates, f_obj)


# 转换boundary_coordinates to  boundary_coordinates1
def change_coordinate(h, boundary_coordinates):
    start_time = datetime.datetime.now()
    boundary_coordinates1 = copy.deepcopy(boundary_coordinates)
    for i in range(len(boundary_coordinates)):
        boundary_coordinates1[i][0] = h - boundary_coordinates[i][0]
    end_time = datetime.datetime.now()
    print("坐标转换用时" + str(end_time - start_time))
    return boundary_coordinates1


# 生成boundary_coordinates文件
def save_boundary_coordinates1(boundary_coordinates1):
    filename1 = 'boundary_coordinates1.json'
    with open(filename1, 'w') as f_obj1:
        json.dump(boundary_coordinates1, f_obj1)
