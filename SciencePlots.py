# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 18:59:47 2020

@author: Hengheng Zhang

E-Mail: hengheng.zhang@kit.edu

Function： Science Plot

"""
import numpy as np 
import matplotlib.pyplot as plt 
def model(x, p):
    return x ** (2 * p + 1) / (1 + x ** (2 * p))
x = np.linspace(0.75, 1.25, 201)
#%% origin
fig, ax = plt.subplots(figsize=(4,3),dpi=200)
for p in [10, 15, 20, 30, 50, 100]:
    ax.plot(x, model(x, p), label=p)
ax.legend(title='Order')
ax.set(xlabel='Voltage (mV)')
ax.set(ylabel='Current ($\mu$A)')
ax.autoscale(tight=True)
#%% science plot
with plt.style.context(['science','no-latex']):
    fig, ax = plt.subplots(figsize=(4,3),dpi=200)
    for p in [10, 15, 20, 30, 50, 100]:
        ax.plot(x, model(x, p), label=p)
    ax.legend(title='Order')
    ax.set(xlabel='Voltage (mV)')
    ax.set(ylabel='Current ($\mu$A)')
    ax.autoscale(tight=True)
#%% IEEE
with plt.style.context(['ieee','no-latex']):
    fig, ax = plt.subplots(figsize=(4,3),dpi=200)
    for p in [10, 15, 20, 30, 50, 100]:
        ax.plot(x, model(x, p), label=p)
    ax.legend(title='Order')
    ax.set(xlabel='Voltage (mV)')
    ax.set(ylabel='Current ($\mu$A)')
    ax.autoscale(tight=True)
#%%dark_background+science+high-vis
with plt.style.context(['dark_background', 'science', 'high-vis','no-latex']):
    fig, ax = plt.subplots(figsize=(4,3),dpi=200)
    for p in [10, 15, 20, 30, 50, 100]:
        ax.plot(x, model(x, p), label=p)
    ax.legend(title='Order')
    ax.set(xlabel='Voltage (mV)')
    ax.set(ylabel='Current ($\mu$A)')
    ax.autoscale(tight=True)
