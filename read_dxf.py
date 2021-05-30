# -*- coding:utf-8 -*-
"""
作者：陈昊卓
日期：2021年04月26日
"""
import dxfgrabber

# def read_dxf(dxf_name):
#     dxf  = dxfgrabber.readfile(dxf_name)
#
#     for entities in dxf.entities:
#         # return entities.dxftype
#         if entities.dxftype == 'LINE':
#             print(entities.start, entities.end)
#         if entities.dxftype == 'CIRCLE':
#             print(entities.center, entities.radius)
#         if entities.dxftype == 'ARC':
#             print(entities.center, entities.radius, entities.start_angle, entities.end_angle)
#         if entities.dxftype == 'LWPOLYLINE':
#             print(entities.points)
#         if entities.dxftype == 'POINT':
#             print(entities.point)
#         if entities.dxftype == 'Ellipse':
#             print(entities.center, entities.major_axis, entities.ratio, entities.start_param, entities.end_param)

dxf = dxfgrabber.readfile("dxf\zuhe.dxf")

for entities in dxf.entities:

    print(entities.dxftype, entities.layer)
    if entities.dxftype == 'LINE':
        print(entities.start, entities.end)
    if entities.dxftype == 'CIRCLE':
        print(entities.center, entities.radius)
    if entities.dxftype == 'ARC':
        print(entities.center, entities.radius, entities.start_angle, entities.end_angle)
    if entities.dxftype == 'LWPOLYLINE':
        print(entities.points)
    if entities.dxftype == 'POINT':
        print(entities.point)
    if entities.dxftype == 'Ellipse':
        print(entities.center, entities.major_axis, entities.ratio, entities.start_param, entities.end_param)

# read_dxf("dxf\zuhe.dxf")