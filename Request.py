# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 14:51:02 2020

@author: Hengheng Zhang

E-Mail: hengheng.zhang@kit.edu

Function：

"""
import requests

response = requests.get('https://httpbin.org/ip')

print('Your IP is {0}'.format(response.json()['origin']))