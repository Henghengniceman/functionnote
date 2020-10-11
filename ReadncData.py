# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 12:55:40 2020

@author: Hengheng Zhang

E-Mail: hengheng.zhang@kit.edu

Function：

"""
import numpy
from netCDF4 import Dataset
f = Dataset("complex.nc","w")

size = 3
datac = numpy.exp(1j*(1.+numpy.linspace(0, numpy.pi, size)))
complex128 = numpy.dtype([("real",numpy.float64),("imag",numpy.float64)])
omplex128_t = f.createCompoundType(complex128,"complex128")