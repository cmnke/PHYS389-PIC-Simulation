

from particle import Particle
import numpy as np
import random


def xyzGen(N=5, X=5, Y=5, Z=5):
    particleList = []

    for i in range(N):
        particleList.append(Particle(name=i))

    for p in particleList:

        x = random.randint(1, X*100 - 1)/100
        y = random.randint(1, Y*100 - 1)/100
        z = random.randint(1, Z*100 - 1)/100


        xv = random.random()*random.randint(-1, 1)
        yv = random.random()*random.randint(-1, 1)
        zv = random.random()* random.randint(-1, 1)

        # xv, yv, zv = random.randint(-1, 1), random.randint(-1, 1), random.randint(-1, 1)

        #2D
        # z = Z
        # zv = 0

        p.position = np.array([x, y, z], dtype=float)
        p.velocity = np.array([xv, yv, zv], dtype=float)
    return particleList
