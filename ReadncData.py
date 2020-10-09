# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 12:55:40 2020

@author: Hengheng Zhang

E-Mail: hengheng.zhang@kit.edu

Function：

"""
import netCDF4 as nc
import numpy as np

FileDataSet=nc.Dataset('../result/test2.nc')
# print(FileDataSet)
all_vars = FileDataSet.variables.keys()  
print(all_vars)
temp = np.array(FileDataSet['temp'][:])   # read lon
temp1=temp[0,0,:,:]