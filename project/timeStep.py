

from particle import Particle
import numpy as np
import pandas as pd

# Main time loop, particleList is the Data list used, steps is the index range we can go and interaction is the logic for elastic collision or repulsion
def timeStep(particleList=[], steps=1000, interaction=0):

    for i in range(steps):

        for p in particleList:

            p.update(Particles=particleList, interaction=interaction)

        step = int(steps/100)

        if i % step == 0:

            print("{}% Done".format(round(i*100/steps, 2)))

    Data = []


    for p in particleList:

        Data += p.positionlog

    db = pd.DataFrame(Data, columns=['index', 'name', 'x', 'y', 'z', 'Ek', 'U', 'V'])

    return db
