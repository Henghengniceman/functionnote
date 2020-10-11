# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 11:13:03 2020

@author: Hengheng Zhang

E-Mail: hengheng.zhang@kit.edu

Function：Netcdf 4 tutorial

"""
## creat nc files 
from  netCDF4 import Dataset
import time
import numpy
from datetime import datetime, timedelta
from netCDF4 import num2date, date2num
Path='../result/test3.nc'

rootgrp = Dataset(Path,'w',format='NETCDF4')
# print(rootgrp)
rootgrp =Dataset(Path,'a')
fcstgrp = rootgrp.createGroup('forecasts')
analgrp = rootgrp.createGroup('analyses')
# print(rootgrp.groups)
fcstgrp1 = rootgrp.createGroup('/forecasts/model1')
fcstgrp2 = rootgrp.createGroup('/forecasts/model2')
# avigate all the groups 
def walktree(top):
      values = top.groups.values()
      yield values
      for value in top.groups.values():
        for children in walktree(value):
              yield children
# print(rootgrp)
# for children in walktree(rootgrp):
#     for child in children:
#         print(child)
# Create dimensions in file
level = rootgrp.createDimension("level", None)
timeD = rootgrp.createDimension("timeD", None)
lat = rootgrp.createDimension("lat", 73)
lon = rootgrp.createDimension("lon", 144)

# Creat variables 
times = rootgrp.createVariable("time","f8",("timeD",))
levels = rootgrp.createVariable("level","i4",("level",))
latitudes = rootgrp.createVariable("lat","f4",("lat",))
longitudes = rootgrp.createVariable("lon","f4",("lon",))
temp = rootgrp.createVariable("temp","f4",("timeD","level","lat","lon",))
temp.units = 'K'
# # # print(temp)
# # # add path
# # ftemp = rootgrp.createVariable("/forecasts/model1/temp","f4",("time","level","lat","lon",))
# # ftemp.units ='K'
# # attributes
rootgrp.description = "bogus example script"
rootgrp.history = "Created "+ time.ctime(time.time())
rootgrp.source = "netCDF4 python module tutorial"
latitudes.units = "degrees north"
longitudes.units = "degrees east"
levels.units = "hPa"
temp.units = "K"
times.units = "hours since 0001-01-01 00:00:00.0"
times.calendar = "gregorian"

lats =  numpy.arange(-90,91,2.5)
lons =  numpy.arange(-180,180,2.5)
latitudes[:] = lats
longitudes[:] = lons

nlats = len(rootgrp.dimensions["lat"])
nlons = len(rootgrp.dimensions["lon"])
from numpy.random import uniform
temp[0:5, 0:10, :, :] = uniform(size=(5, 10, nlats, nlons))
levels[:] =  [1000.,850.,700.,500.,300.,250.,200.,150.,100.,50.]

dates = [datetime(2001,3,1)+n*timedelta(hours=12) for n in range(temp.shape[0])]
times[:] = date2num(dates,units=times.units,calendar=times.calendar)
# from numpy.random import uniform
# temp[0:5, 0:10, :, :] = uniform(size=(5, 10, nlats, nlons))
# # append along two unlimited dimensions by assigning to slice.

# # get all netCDF attributes
# # for name in rootgrp.ncattrs():
# #      print("Global attr {} = {}".format(name, getattr(rootgrp, name)))

# # print(rootgrp["/forecasts/model1"])  # a Group instance
# # print(rootgrp["/forecasts/model1/temp"])  # a Variable instance
# # print dimension object
# # for dimobj  in rootgrp.dimensions.values():
# #     print(dimobj)

