# -*- coding:utf-8 -*-
"""
作者：陈昊卓
日期：2021年04月14日
"""
import numpy as np
import Physical_boundary_acquisition_test


class ImageSegmentation():
    def __init__(self, num_edges,image):
        self.num_edges = num_edges
        self.image = image

    def crack(self, num_edges):
        start = int(np.sqrt(num_edges))
        factor = num_edges / start
        while not ImageSegmentation.is_integer(self,factor):
            start += 1
            factor = num_edges / start
        return int(factor), start

    def is_integer(self, number):
        if int(number) == number:
            return True
        else:
            return False

imagesegmentation1 = ImageSegmentation(Physical_boundary_acquisition_test.num_edges, Physical_boundary_acquisition_test.image)
imagesegmentation1.crack(Physical_boundary_acquisition_test.num_edges)
print(imagesegmentation1.crack(Physical_boundary_acquisition_test.num_edges))
