# -*- coding:utf-8 -*-
"""
作者：陈昊卓
日期：2021年04月26日
"""
import dxfgrabber

line = []
circle = []
lwpolyline = []
ellipse = []
def read_dxf(dxf_name):
    dxf = dxfgrabber.readfile(dxf_name)


    for entities in dxf.entities:
        if entities.dxftype == 'LINE':
            print('LINE')
            line.append(entities.start)
            line.append(entities.end)
            print(entities.start, entities.end)
        if entities.dxftype == 'CIRCLE':
            print('CIRCLE')
            circle.append(entities.center)
            circle.append(entities.ratius)
            print(entities.center, entities.radius)
        if entities.dxftype == 'LWPOLYLINE':
            print('LWPOLYLINE')
            lwpolyline.append(entities.points)
            print(entities.points)
        if entities.dxftype == 'Ellipse':
            print('Ellipse')
            print(entities.center, entities.major_axis, entities.ratio, entities.start_param, entities.end_param)



read_dxf("dxf\\rectangular.dxf")
print("line " + str(line))
print("circle " + str(circle))
print("lwpolyline " + str(lwpolyline))
