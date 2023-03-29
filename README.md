
# PIC (Particle in container) Simulation using different techniques


## Installation:
Run the command:
```
python3 -m pip install [Package Name from requirements.txt]
```
No need to dockerize the application as the libraries used are windows/macos/linux compatible.

## Usage
Run:
```
python3 runTHIS.py
```
If any errors for missing packages arise, return to Installation step and add the package.

## Running the code

Upon first running the code, a prompt in the terminal appears to insert either 0, 1, 2 or 3 as options for various simulation models.
Error checks are put in place as to ensure those are the only possible modes that can be chosen. 

After loading is complete, the 3D animation will play and simulate particles inside a closed container. Values for the container have been hard coded as well for the particles due to physical constraints of the systems, but number of particles and the length of simulation can be manually edited in the runTHIS.py file at the top of it.

After the animation is closed, a plot for energy conservation is shown and afterwards a histogram for the distribution of speeds at the last iteration of the simulation for each particle.

## Physics used

This simulation involves two basic PIC models:

1. Electrostatic Repulsion
2. Elastic Collision

Both implementations have been done using a Forward Euler method where the position of a particle is calculated by the velocity multiplied by a timestep. 

The simulation can also provide a combined simulation where both effects are simulatiosly working, which produces the most consistent energy conservation plots. 

Elastic collision simulation also includes a simple Uniform Grid Spacing Partitioning system, where particles have a corresponding grid coordinates and any calculations between particles happen only if the are in the same or adjacent grid cell. This only works for elastic collision, as the Repulsion method relies on particles further away for the potential energy and superposition of forces from every particle (There are Partitioning systems for a repulsion model, however they rely on real values for every particle, approximations and huge computing power ).


## Equations

### Elastic Colisions
Using conservation of momentum and energy for a 2D system and the assumption that when a sphere hits another sphere, the first one moves tangentially to the normal where it connects to the other sphere, which continues on the normal vector. 

$$
\vec{v}_1^{new} = \vec{v}_1 - \dfrac{2m_2}{m_1+ m_2} \dfrac{(\vec{v_1}-\vec{v_2})\cdot (\vec{x_1}-\vec{x_2})}{||\vec{x_2}-\vec{x_1}||^2}(\vec{x_1}-\vec{x_2})
$$

$$
\vec{v}_2^{new} = \vec{v}_2 - \dfrac{2m_1}{m_1+ m_2} \dfrac{(\vec{v_2}-\vec{v_1})\cdot (\vec{x_2}-\vec{x_1})}{||\vec{x_1}-\vec{x_2}||^2}(\vec{x_2}-\vec{x_1})
$$
The values $\vec{v}_1^{new}, \vec{v}_2^{new}$ are the resulting velocities, while the $m$ is the mass and $x$ is the position vectors. These equations work for 2D and 3D systems.

### Electrostatic Repulsion

The force superposition calculated follows:

$$
F = \Sigma_n^i F_i = \Sigma \dfrac{k}{r^3} \hat{r}
$$

The electrostatic potential is:

$$
U = \Sigma_n^i U_i = \dfrac{k}{r} 
$$

where $F$ is the force, $k$ is Coulomb's constant, however this simulation is unitless and as such this value is subject to hard coded trial and error. Mostly due to the size of the box and radius of the particles. $r$ is the distance between two particles.

## Attempts at implementations

This project began as a test area for testing equations, however numerous bugs and slow code made me focus on improving this before starting any of my other ideas, which resulted in no time left and a decent performing code.

### Units
The code is unitless due to the fact that it can simulate gasses but particles to be visible have a radius that is 1/50th of the total visible area. Another problem was the Coulomb constant which if high enough, would force particles in the corners where they would stack, creating extremely high potential energy which randomly would explode and cause conservation of energy to cease. If the value is too low, it also doesn't cause any "collision" to happen. Another problem was the elastic collision detection system, which had a rubber banding effect happen where particles would overlap, but then start spinning and not detach. Numerous fixes were implemented to try to aleviate the problem, but the only solution was adjusting the time step, radius size and starting velocities. This is the main improvement that can be made to the code for real physics simulations.


### Multithreading
Python is a notoriously bad language for multithreading and an attempt was made for an asynchronous for loop, where each particle in the main Particle class gets iterated by a different thread, however this didn't work due to the bad optimization of python partitioning resources and resulted in longer waiting times. 

### Complex checks for Partitioning

The Uniform Grid Space Partitioning system that is implemented is currently an ID system where each particle's ID gets updated based on their position. This works great for optimizing the number of calculations made and shrinking down the size of the grid cells improves performance as more checks for empty cells are made, but less total distance calculations. In a complex model this becomes more important. 

However the current implementation is insufficient for complex systems, where the grid partitioning requires itself to be its own entity as then, threads can be assigned to different cells to improve performance up to 1000x better. This should be done in another language.


## Unfinished goals
Originally as based on the Week 1 Report, the main goal of the module was simulating an interesting system as a cyclotron and a cloud chamber, but as predicted by the lecturer, the time constraint was too much, so early on I focused on making this system work. While basic in the physics calculations, more time was spent researching optimization methods as the original check every particle with every other one is incredibly slow and inefficient. This however is an advanced topic in graphic simulations, but nevertheless I advise the lecturer for next years to mention briefly a simple implementations of such algorhitms, as most code found on the internet is extremely slow.