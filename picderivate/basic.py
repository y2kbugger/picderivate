'''
Created on Sep 4, 2012

@author: y2k
'''

from time import sleep
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#canvasb size setup
dpi = 513
inches = np.array([1, 1])
dots = dpi * inches

#======Initial Pic Setup=================
#draw 2d zero matrix
if True:
    imageIn = np.zeros(shape=dots, dtype=np.uint8)

#draw square
if False:
    rect = (100, 100)
    amplitude = 240  # of color
    shift = (0, 0)

    edgeNear = (dots - rect) / 2 + shift
    edgeFar = (dots + rect) / 2 + shift
    imageIn[edgeNear[0]:edgeFar[0], edgeNear[1]:edgeFar[1]] = amplitude

#set this one to true to initiate it with an image
if False:
    imageIn = np.uint8(255 * mpimg.imread('t.png'))

#draw single pixel
if True:
    amplitude = 100   # of color
    imageIn[(dots[0] - 1) / 2, (dots[1] - 1) / 2] = amplitude
#==========================================

#setup the figure
fig = plt.figure(figsize=[inches[1], inches[0]], dpi=dpi)
im = plt.figimage(imageIn)

plt.ion()
plt.show()

for i in range(10000):
    imageShift = np.roll(imageIn, 1, 0)
    imageOut = (imageShift - imageIn)
    imageShift = np.roll(imageIn, -1, 0)
    imageOut = imageOut + (imageShift - imageIn)
    imageShift = np.roll(imageIn, 1, 1)
    imageOut = imageOut + (imageShift - imageIn)
    imageShift = np.roll(imageIn, -1, -1)
    imageOut = imageOut + (imageShift - imageIn)
    imageIn = imageOut
    im.set_array(imageOut)

    #sleep(5) #optionaly slow down the loop a bit
    plt.draw()
