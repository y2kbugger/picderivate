#! /usr/bin/env python3

'''
Created on Sep 4, 2012

@author: y2k
'''

from time import sleep
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from  matplotlib.animation import FuncAnimation

#canvasb size setup
dpi = 512
inches = np.array([1, 1])
dots = dpi * inches
#dots += np.array([0, -111])

#======Initial Pic Setup=================
#draw 2d zero matrix
if True:
    imageIn = np.zeros(shape=dots, dtype=np.uint8)

#draw square
if False:
    rect = (20, 350)
    amplitude = 255  # of color
    shift = (0, 0)

    edgeNear = (dots - rect) / 2 + shift
    edgeFar = (dots + rect) / 2 + shift
    imageIn[edgeNear[0]:edgeFar[0], edgeNear[1]:edgeFar[1]] = amplitude

#set this one to true to initiate it with an image
if False:
    imageIn = np.uint8(255 * mpimg.imread('t.png'))
    imageIn = np.uint8(255 * mpimg.imread('mario.png'))

#draw single pixel
if True:
    amplitude = 150   # of color
    imageIn[(dots[0] - 1) / 2, (dots[1] - 1) / 2] = amplitude

#give an exact array
if False:
    imageIn=np.array([[ 128, 128,   0, 128, 128,   0, 128, 128,   0, 128, 128,   0, 128, 128,   0, 128, 128,   0, 128, 128,   0, 128, 128,   0],
                      [ 128,   0, 128, 128,   0, 128, 128,   0, 128, 128,   0, 128, 128,   0, 128, 128,   0, 128, 128,   0, 128, 128,   0, 128],
                      [   0, 128, 128,   0, 128, 128,   0, 128, 128,   0, 128, 128,   0, 128, 128,   0, 128, 128,   0, 128, 128,   0, 128, 128],
                      [ 128, 128,   0, 128, 128,   0, 128, 128,   0, 128, 128,   0, 128, 128,   0, 128, 128,   0, 128, 128,   0, 128, 128,   0],                     
                      [ 128,   0, 128, 128,   0, 128, 128,   0, 128, 128,   0, 128, 128,   0, 128, 128,   0, 128, 128,   0, 128, 128,   0, 128],
                      [   0, 128, 128,   0, 128, 128,   0, 128, 128,   0, 128, 128,   0, 128, 128,   0, 128, 128,   0, 128, 128,   0, 128, 128]],dtype=np.uint8)

#==========================================

#setup the figure
fig = plt.figure(figsize=[inches[1], inches[0]], dpi=dpi)
im = plt.figimage(imageIn)

# plt.ion()

def update(i):
    global imageIn
    imageOut = np.roll(imageIn, 1, 0) - imageIn
    imageOut += np.roll(imageIn, -1, 0) - imageIn
    imageOut += np.roll(imageIn, 1, 1) - imageIn
    imageOut += np.roll(imageIn, -1, -1) - imageIn
    imageIn = imageOut
    im.set_array(imageOut)

    sleep(.051) #optionaly slow down the loop a bit
    # print(imageIn)
animation = FuncAnimation(fig, update, interval=1)
print('end')
plt.show()

