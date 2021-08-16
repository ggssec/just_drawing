import numpy as np
import cv2
import json
import os
import copy
import datetime
from cv2 import imread, resize, imshow, waitKey, INTER_AREA
from itertools import product
def cv_imread(file_path):
    root_dir, file_name = os.path.split(file_path)
    pwd = os.getcwd()
    if root_dir:
        os.chdir(root_dir)
    cv_img = cv2.imread(file_name, 0)
    os.chdir(pwd)
    return cv_img
def Decrease_pixel_density(image):
    image2 = np.zeros((int(len(image) / 3), int(len(image[0]) / 3)), np.uint8)
    for i_2, i in enumerate(range(1, len(image) - 1, 3)):
        for j_2, j in enumerate(range(1, len(image[0]) - 1, 3)):
            if int(image[i, j]) + int(image[i, j - 1]) + int(image[i, j + 1]) + int(image[i - 1, j - 1]) + int(image[i - 1, j]) + int(image[i - 1, j + 1]) + int(image[i + 1, j - 1]) + int(image[i + 1, j]) + int(image[i + 1, j + 1]) >= 255 * 2:
                image2[i_2, j_2] = 255
            else:
                image2[i_2, j_2] = 0
    return image2

def save_boundary_coordinates(boundary_coordinates):
    del boundary_coordinates[0]
    filename = 'boundary_coordinates.json'
    with open(filename, 'w') as f_obj:
        json.dump(boundary_coordinates, f_obj)
def change_coordinate(h, boundary_coordinates):
    start_time = datetime.datetime.now()
    boundary_coordinates1 = copy.deepcopy(boundary_coordinates)
    for i in range(len(boundary_coordinates)):
        boundary_coordinates1[i][0] = h - boundary_coordinates[i][0]
    end_time = datetime.datetime.now()
    print("坐标转换用时" + str(end_time - start_time))
    return boundary_coordinates1
def save_boundary_coordinates1(boundary_coordinates1):
    filename1 = 'boundary_coordinates1.json'
    with open(filename1, 'w') as f_obj1:
        json.dump(boundary_coordinates1, f_obj1)