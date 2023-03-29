from xyzGen import xyzGen
from timeStep import timeStep
from plotting import Plot
import matplotlib.pyplot as plt
import timeit
import numpy as np

version =  input("Input 0, for no collision between particles, 1 for Elastic collision, 2 for Electrostatic repulsion and 3 for both: ")

particleCount = 50

steps = 1000

def collisionPlot():

    start_time = timeit.default_timer()

    Allpoints = xyzGen(particleCount)

    Data = timeStep(particleList=Allpoints,steps=steps, interaction=int(version))

    end_time = timeit.default_timer()

    print("Rendering Time:", end_time - start_time)

    Plot(Data=Data)

    kineticEnergy = []

    stepRange = list(range(0,steps))

    for n in range(0,steps):

        sum = 0

        for i in range(0,particleCount):

            energy = Data.Ek[i*steps+n]

            sum += energy

        kineticEnergy.append(sum)

    plt.plot(stepRange, kineticEnergy, label='Kinetic Energy')

    plt.legend()

    plt.title('Multiple Lines Plot')

    plt.xlabel('Time [steps]')

    plt.ylabel('Energy')  

    plt.show()

    histogram(Data)


def repulsionPlot():

    start_time = timeit.default_timer()

    Allpoints = xyzGen(particleCount)

    Data = timeStep(particleList=Allpoints,steps=steps, interaction=int(version))

    end_time = timeit.default_timer()

    print("Rendering Time:", end_time - start_time)

    Plot(Data=Data)

    kineticEnergy, potentialEnergy = [], []

    for n in range(0,steps):
        sum = 0
        for i in range(0,particleCount):
            energy = Data.Ek[i*steps+n]
            sum += energy
        kineticEnergy.append(sum)

    for n in range(0,steps):
        sum = 0
        for i in range(0,particleCount):
            energy = Data.U[i*steps+n]
            sum += energy
        potentialEnergy.append(sum)    

    stepRange = list(range(0,steps))


    plt.plot(stepRange, kineticEnergy, label='Kinetic Energy')

    plt.plot(stepRange, potentialEnergy, label='Potential Energy')

    plt.plot(stepRange, (np.array(kineticEnergy) + np.array(potentialEnergy))/2, label='Total Energy/2')

    plt.legend(bbox_to_anchor=(0.6, 0.2), loc='lower left', borderaxespad=0)

    plt.title('Multiple Lines Plot')

    plt.xlabel('Time [steps]')

    plt.ylabel('Energy')  

    plt.show()

    histogram(Data)


def histogram(Data):

    data = []
    for n in range(0,particleCount):
        sum = 0
        test = Data.V[(n+1)*steps-1]
        # print(test)
        sum += test
        data.append(sum)


    plt.hist(data, bins=10 , alpha=0.7,edgecolor='black', color='green')
    plt.title('Histogram of speed distribution')
    plt.xlabel('Speed')
    plt.ylabel('Frequency')
    plt.show()


try:

    version

except ValueError:

    raise ValueError("Wrong input detected")

version = int(version)


if version == 1:

    collisionPlot()

elif version == 2:

    repulsionPlot()

elif version == 3:

    repulsionPlot()

elif version == 0:
    
    collisionPlot()

else:
    
    raise ValueError("Wrong input detected")


