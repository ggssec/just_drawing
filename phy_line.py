import looking_for_vertices
import numpy as np
import cv2
import json
import tkinter as tk
from tkinter import filedialog
import os
import copy
from Physical_boundary_acquisition import *

class Make_Boundary:
    def __init__(self):

    def bt_choice1(self,image):
        image = Decrease_pixel_density(image)  # 降低像素密度
        looking_for_vertices1 = looking_for_vertices.LookingForVertices(image)  # 新对象
        boundary_coordinates = looking_for_vertices1.Extract_rectangular_1(image)  # 获取顶点坐标信息