import numpy as np
from math import sqrt, ceil

class Particle:
    # def __init__(self, mass=1, name=0, radius=0.1):
    def __init__(self, mass=1.7e-27, name=0, radius=1e-18):
        self.position = np.array([0,0,0], dtype= float)
        self.velocity = np.array([0,0,0], dtype= float)
        self.positionlog = []
        self.mass = mass
        self.potential = 0
        self.kinetic = 0
        self.iteration = 0
        self.name = name
        self.radius = radius

        self.grid = np.ceil(self.position)
        


    # def update(self, Particles, k=0.01, dT=0.1, Xlimit=5, Ylimit=5, Zlimit=5, interaction=0, gravity=0):
    def update(self, Particles, k=9e9, dT=1e-10, Xlimit=5, Ylimit=5, Zlimit=5, interaction=0, gravity=0):

        self.kinetic = 0.5*self.mass*sqrt(self.velocity[0]**2+self.velocity[1]**2+self.velocity[2]**2)**2

        force = np.array([0, 0, 0], dtype=float)


        self.potential = 0


        test = 0

        for particle in Particles:
            # if particle.name != self.name:

            distance = distanceBetween(self.position, particle.position)

            # Check if points are different or hit

            if particle.name != self.name:

                # Elastic Collision Only
                if interaction == 1:
                    
                    if gridCheck(self,particle):
                    # if True:
                        collision(self, particle, distance)

                # Electrostatic Repulsion Only
                elif interaction == 2:

                    # if gridCheck(self,particle):
                    if True:
                        force, self.potential = electroStaticForce(self, particle, distance, k, force)

                # Combined Collision and Repulsion 
                elif interaction == 3:

                    if gridCheck(self,particle):
                    # if True:

                        collision(self, particle, distance)

                        force, self.potential = electroStaticForce(self, particle, distance, k, force)


        # If gravity enabled ( for fun )
        self.velocity[2] += gravity*dT

        # Acceleration required for electrostatic repulsion
        Acc = force/self.mass

        self.velocity += Acc*dT

        # Forward Euler 
        self.position += self.velocity*dT

        boundaryCheck(self, Xlimit, 0)

        boundaryCheck(self, Ylimit, 1)

        boundaryCheck(self, Zlimit, 2)

        data = np.array([self.iteration, self.name, self.position[0], self.position[1], self.position[2], self.kinetic, self.potential, sqrt(self.velocity@self.velocity) ], dtype=float)

        self.positionlog.append(data)

        self.iteration += 1


# 10x faster than np.linalg.norm

def distanceBetween(list1, list2):

    return sqrt((list2[0]-list1[0])**2 + (list2[1]-list1[1])**2 + (list2[2]-list1[2])**2)



def boundaryCheck(Object, Limit, index):

    if Object.position[index] >= Limit:

        Object.position[index] = Limit

        Object.velocity[index] = -Object.velocity[index]

    if Object.position[index] <= 0:

        Object.position[index] = 0

        Object.velocity[index] = -Object.velocity[index]



def electroStaticForce(p1, p2, distance, k, force):

    if distance != 0:

        # force += k*(p1.position - p2.position)/distance**3
    
        # p1.potential += (k)/distance

        force += k*(p1.position - p2.position)*(1.6e-19)/distance**3
    
        p1.potential += (k)/distance

        # print(force)

    return force, p1.potential


def collision(p1, p2, distance):

    direction = (p2.position - p1.position)/distance

    if distance <= p1.radius + p2.radius:

        #Collision

        totalMass = p1.mass + p2.mass

        massDifference = p1.mass - p2.mass

        selfTempVelocity = np.array([p1.velocity[0], p1.velocity[1], p1.velocity[2]])

        selfTempPos = np.array(p1.position)

        particleTempPos = np.array(p2.position)

        particleTempVelocity = np.array([p2.velocity[0], p2.velocity[1], p2.velocity[2]])

        # wikipedia collision for 2D (vectors so 3D) Velocity Adjustment

        p1.velocity = selfTempVelocity - ( 2*p2.mass/totalMass )*(np.dot(selfTempVelocity - particleTempVelocity, p1.position - p2.position))*(p1.position - p2.position)/distance**2

        p2.velocity = particleTempVelocity - ( 2*p1.mass/totalMass )*(np.dot(particleTempVelocity- selfTempVelocity,  p2.position- p1.position))*(p2.position- p1.position)/distance**2

        # https://stackoverflow.com/questions/62864205/sometimes-the-ball-doesnt-bounce-off-the-paddle-in-pong-game Error attempt fix? doesnt work yet

        # if p1.radius + p2.radius > distance:

        #     p1.position = selfTempPos - 0.5*(distance-p1.radius-p2.radius)*direction

        #     p2.position = particleTempPos - 0.5*(distance-p1.radius-p2.radius)*direction


def gridCheck(self, particle):
    
    # if self.grid[0] == particle.grid[0] and self.grid[1] == particle.grid[1] and self.grid[2] == particle.grid[2]: 
        # return True
    if abs(self.grid[0] - particle.grid[0]) <= 1 and abs(self.grid[1] - particle.grid[1]) <= 1 and abs(self.grid[2] - particle.grid[2]) <= 1:

        return True


