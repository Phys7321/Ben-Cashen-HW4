# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 16:07:25 2018

@author: Ben
"""

import numpy as np
from matplotlib import pyplot

sigma = 1.0
sigma2 = sigma**2

def metropolis(xold,delta,sigma2,accCount):
    xtrial = np.random.random()    
    xtrial = xold+(2*xtrial-1)*delta
    weight = np.exp(-0.5*(xtrial**2-xold**2)/sigma2)
    xnew = xold
    if(weight >= 1): # Accept
        xnew = xtrial
        accCount += 1   # Keeping track of number of accepted values
    else:
        r = np.random.random()
        if(r <= weight): # Accept
            xnew = xtrial
            accCount += 1
    return [xnew,accCount]

deltaVals = np.arange(0.1,3.5,0.1)
accRatio = np.zeros(deltaVals.size)
eqlTime = np.zeros(deltaVals.size)

deltaCount = 0
binwidth = sigma/10
windowSize = 1000 

for delta in deltaVals:
    N = 10000
    x = np.zeros(N)
    xwalker = 10.0
    
    accCount = 0
    trialCount = 0
    x[0] = xwalker
    for i in range(1,N):
        x0 = x[i-1]
        for j in range(9):
            [x0,accCount] = metropolis(x0,delta,sigma2,accCount)
        [x[i],accCount] = metropolis(x[i-1],delta,sigma2,accCount)
        trialCount += 10            # Keeping track of number of trials
    accRatio[deltaCount] = accCount/trialCount
    
    windowMid = windowSize/2 
    midptlist = [] # Midpoint of the window
    avgx2 = []
    logcheckratio = 1.0 # We calculate the log of <x^2>/sigma. At equilbrium this ratio should be zero.
    while((windowMid + (windowSize/2) < N) and (logcheckratio > 0.01)):
        # This loop continues until we reach the end of the x array 
        # or if <x^2> is within 1% order of magnitude of sigma
        temp = 0
        for i in range(windowSize):
            temp += x[int(windowMid + i - (windowSize/2))]**2
        temp = temp/windowSize
        midptlist.append(windowMid) # The value of <x^2> is assigned to the middle of the averging window.
        avgx2.append(temp)
        windowMid += int(windowSize/10) # We move the window forward by windowSize/10. You can play with the denominator
        logcheckratio = np.log10(temp/sigma) 
        
    eqlTime[deltaCount] = midptlist[-1]
    
    deltaCount += 1
    
f = pyplot.figure(1)   
pyplot.plot(deltaVals,eqlTime)
pyplot.xlabel(r'$\delta$')
pyplot.ylabel('Equilibration time (steps)')
pyplot.title('Equilibration time vs. $\delta$')
f.show()

g = pyplot.figure(2)
pyplot.plot(deltaVals,accRatio)
pyplot.xlabel(r'$\delta$')
pyplot.ylabel('Acceptance ratio')
pyplot.title('Acceptance ratio vs. $\delta\$')
g.show()

"""
Figure 2 consistently shows that the acceptance rate decreases as larger step 
sizes are taken.

Figure 1 is a bit erratic, but generally shows that equilibration time decreases 
as the step size is increased.

A choice of delta = 3 gives the minimum acceptable acceptance rate of ~ 0.5 and
ensures a relatively low equilibration time. 
"""