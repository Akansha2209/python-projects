# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 22:03:00 2019

@author: kailash
"""

import math
import matplotlib.pyplot as plt
# generate a sinusoid
nbsamples=256
xrange=(-math.pi,math.pi)
x,y=[],[]
for n in xrange(nbsamples):
    k=(n+0.5)/nbsamples
    x.append(xrange[0]+(xrange[1]-xrange[0])*k)
    y.appeplt.show( )and(math.sinx[-1])
#   plot the sinusoid
plt.plot(x,y)
plt.show( )    
    
