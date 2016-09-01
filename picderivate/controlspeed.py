'''
Created on Sep 4, 2012

@author: y2k
'''


from time import sleep
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.animation as animation


class plotter:
    def __init__(self, dpi=101, x=5, y=5, image=False, imagelocation='t.png'):
        # canvas
        self.dpi = dpi
        self.inches = np.array([x, y])
        self.dots = self.dpi * self.inches
        self.iterations = 0
        self.speed = -3  # pause = 2^speed

        if image:
            # import png
            print(mpimg.imread(imagelocation).shape[0:2])
            self.dots = np.array(mpimg.imread(imagelocation).shape[0:2])
            self.imageIn = np.uint8(255 * mpimg.imread(imagelocation))
            self.fig = plt.figure(figsize=[self.dots[1], self.dots[0]], dpi=1)
        else:
            # draw 2d zero matrix
            self.imageIn = np.zeros(shape=self.dots, dtype=np.uint8)
            self.fig = plt.figure(figsize=[self.inches[1], self.inches[0]], dpi=self.dpi)

        # display array as image figure
        # self.fig = plt.figure(figsize=[self.inches[1], self.inches[0]], dpi=self.dpi)
        # self.fig = plt.figure(figsize=self.dots, dpi=self.dpi)
        self.im = self.fig.figimage(self.imageIn)

        self.cid = self.fig.canvas.mpl_connect('scroll_event', self.onscroll)

    def start(self):
        self.ani = animation.FuncAnimation(self.fig, self.plottt, 25, interval=0)
        plt.show()

    def solidRect(self, rect=(50, 50), shift=(0, 0), magnitude=1):
        edgeNear = (self.dots - rect) / 2 + shift
        edgeFar = (self.dots + rect) / 2 + shift
        self.imageIn[edgeNear[0]:edgeFar[0], edgeNear[1]:edgeFar[1]] = magnitude

    # draw a pixel in each corner
    def corners(self, magnitude=1):
        for i in (0, self.dots[0] - 1):
            for j in (0, self.dots[1] - 1):
                self.imageIn[i, j] = magnitude

    # draw a vertical line at a certain x value
    def vertLine(self, magnitude=1, x=128):
        for j in range(int(self.dots[0])):
            self.imageIn[j, x] = magnitude

    # draw single pixel in 0,0
    def origin(self, magnitude=1):
        self.imageIn[0, 0] = magnitude

    # draw single pixel in center
    def center(self, magnitude=1):
        self.imageIn[(self.dots[0] - 1) / 2, (self.dots[1] - 1) / 2] = magnitude

    def onscroll(self, event):
        print('button={}, x={}, y={}'.format(event.button, event.x, event.y))
        if event.button == 'up':
            self.speed += 1
        elif event.button == 'down':
            self.speed -= 1

    def plottt(self, j):
        self.iterations += 1

        # self.fig.suptitle('bold figure subtitle', fontsize=14, fontweight='bold')
        self.imageShift = np.roll(self.imageIn, 1, 0)
        self.imageOut = (self.imageShift - self.imageIn)
        self.imageShift = np.roll(self.imageIn, -1, 0)
        self.imageOut = self.imageOut + (self.imageShift - self.imageIn)
        self.imageShift = np.roll(self.imageIn, 1, 1)
        self.imageOut = self.imageOut + (self.imageShift - self.imageIn)
        self.imageShift = np.roll(self.imageIn, -1, -1)
        self.imageOut = self.imageOut + (self.imageShift - self.imageIn)
        self.imageIn = self.imageOut

        print(2 ** self.speed)
        sleep(2 ** self.speed)

        self.fig.canvas.draw()
        self.im.set_array(self.imageIn)


tehplotter = plotter(dpi=513, x=1, y=1, image=False)
# tehplotter.vertLine()
# tehplotter.solidRect()
tehplotter.corners(100)
tehplotter.start()

