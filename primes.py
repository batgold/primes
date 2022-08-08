# -*- coding: utf-8 -*-
"""
Created on Fri Dec 31 11:07:50 2021

@author: bentg
"""

import numpy as np
import matplotlib.pyplot as plt
import sympy.ntheory as nt 


grid_size = 95400

grid_x = np.zeros(grid_size)
grid_y = np.zeros(grid_size)
prime_x = np.zeros(grid_size)
prime_y = np.zeros(grid_size)
comp_x = np.zeros(grid_size)
comp_y = np.zeros(grid_size)



# BUILD THE GRID
grid_x[1] = 1
grid_x[2] = 1
grid_y[1] = 0
grid_y[2] = 1


for n in np.arange(2,grid_size-1):
    if grid_x[n] == grid_y[n] and grid_x[n]+grid_y[n] > 0:  #top-right
        step_x = -1
        step_y = 0
    elif -grid_x[n] == grid_y[n] and grid_x[n] < 0:  #top-left
        step_x = 0
        step_y = -1
    elif grid_x[n] == grid_y[n] and grid_x[n]+grid_y[n] < 0:  #bottom-left
        step_x = 1
        step_y = 0
    elif -grid_x[n] + 1 == grid_y[n] and grid_x[n] > 0:  #bottom-right
        step_x = 0
        step_y = 1
    
    next_x = grid_x[n] + step_x    
    next_y = grid_y[n] + step_y
    
    grid_x[n+1] = grid_x[n] + step_x
    grid_y[n+1] = grid_y[n] + step_y



# COLLECT THE PRIMES & COMPOSITES
x_not = []
y_not = []

plt.figure(figsize=(10,10))

for n, val in enumerate(np.arange(0,grid_size*2,2)):
    if nt.isprime(val+1):
        prime_x[n] = grid_x[n]
        prime_y[n] = grid_y[n]       
    else:
        comp_x[n] = grid_x[n]
        comp_y[n] = grid_y[n]
    
    # plt.annotate(val+1,(grid_x[n],grid_y[n]-.2),fontsize=7,ha='center')
   

plt.scatter(prime_x,prime_y,marker='s',s=1,c='g')
# plt.scatter(x_not,y_not,marker='s',s=200,c='white')
plt.scatter(np.arange(-150,0),np.ones(150)*1,marker='s',s=1,c='#0000FF33')           #11, 23, 46
plt.scatter(np.arange(-150,0),np.ones(150)*11,marker='s',s=1,c='#0000FF33')           #11, 23, 46
plt.scatter(np.arange(-150,0),np.ones(150)*23,marker='s',s=1,c='#0000FF33')           #11, 23, 46
plt.scatter(np.arange(-150,0),np.ones(150)*46,marker='s',s=1,c='#0000FF33')           #11, 23, 46
plt.scatter(np.arange(-150,0),np.ones(150)*53,marker='s',s=1,c='#0000FF33')           #11, 23, 46
plt.scatter(np.ones(150)*2,np.arange(0,150),marker='s',s=1,c='#0000FF33')

ax = 160    
plt.xlim((-ax,ax))
plt.ylim((-ax,ax))
plt.gca().set_aspect('equal')