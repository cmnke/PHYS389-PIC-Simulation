
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D

# Class that takes the Data object and automatically plots the animation
class Plot(object):

    def __init__(self, Data, Interval=5, Clear=False):

        self.data = Data 
        self.Clear = Clear
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(projection='3d')
        self.ani = animation.FuncAnimation(self.fig, self.update, interval=Interval, init_func=self.setup_plot, blit=False, frames=int(self.data['index'].max()))
        
        # Initialize plot uppon call of the class
        plt.show()

    def setup_plot(self):
        # Clear all previous occurences (visible when index loops back to 0)
        self.ax.clear() 

        self.title = self.ax.set_title('PIC Simulation')
        initialPositions = self.data[self.data['index'] == 0]

        l = len(initialPositions)
        colourList = np.arange(l) #Give particles different colors
        self.graph = self.ax.scatter(initialPositions.x, initialPositions.y, initialPositions.z ,depthshade=False, c=colourList)

        return self.graph,

    def update(self, i):
        # Very fast slideshow (updates the position of every particle each frame)
        Positions = self.data[self.data['index'] == i]

        self.graph._offsets3d = (Positions.x, Positions.y, Positions.z)

        self.title.set_text('PIC Simulation \n Index = {} \n '.format(i))

        return self.graph
