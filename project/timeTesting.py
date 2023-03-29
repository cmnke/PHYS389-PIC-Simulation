import numpy as np
import math
import timeit
from scipy.spatial.distance import euclidean


[x1, y1, z1] = [1,2,3]
[x2, y2, z2] = [1,2,3]

def distance(list1, list2):
    return math.sqrt((list2[0]-list1[0])**2 + (list2[1]-list1[1])**2 + (list2[2]-list1[2])**2)


# Define the two points as NumPy arrays and tuples/lists
p1_arr = np.array([x1, y1, z1])
p2_arr = np.array([x2, y2, z2])
p1_tup = (x1, y1, z1)
p2_tup = (x2, y2, z2)

# Define the number of times to repeat the calculation
num_repeats = 100000

# Test the np.linalg.norm() function
start_time = timeit.default_timer()
for i in range(num_repeats):
    distance_np = np.linalg.norm(p2_arr - p1_arr)
end_time = timeit.default_timer()
print("np.linalg.norm() time:", end_time - start_time)

# Test the manual calculation function
start_time = timeit.default_timer()
for i in range(num_repeats):
    distance_man = math.sqrt((p2_tup[0]-p1_tup[0])**2 + (p2_tup[1]-p1_tup[1])**2 + (p2_tup[2]-p1_tup[2])**2)
end_time = timeit.default_timer()
print("Manual MATH calculation time:", end_time - start_time)

# Test the manual calculation function
start_time = timeit.default_timer()
for i in range(num_repeats):
    distance_man = np.sqrt((p2_tup[0]-p1_tup[0])**2 + (p2_tup[1]-p1_tup[1])**2 + (p2_tup[2]-p1_tup[2])**2)
end_time = timeit.default_timer()
print("Manual NUMPY calculation time:", end_time - start_time)

start_time = timeit.default_timer()
for i in range(num_repeats):
    distance_man = distance(p1_tup, p2_tup)
end_time = timeit.default_timer()
print("Manual function time:", end_time - start_time)


start_time = timeit.default_timer()
for i in range(num_repeats):
    distance = euclidean(p1_tup, p2_tup)
end_time = timeit.default_timer()
print("Scipy Calculation time:", end_time - start_time)

start_time = timeit.default_timer()
for i in range(num_repeats):
    distance = math.sqrt((p1_arr-p2_arr)@(p1_arr-p2_arr))
end_time = timeit.default_timer()
print("Emilio's fake method time:", end_time - start_time)



# Test the manual calculation function
start_time = timeit.default_timer()
for i in range(num_repeats):
    distance_man = math.sqrt((p2_tup[0]-p1_tup[0])**2 + (p2_tup[1]-p1_tup[1])**2 + (p2_tup[2]-p1_tup[2])**2)
end_time = timeit.default_timer()
print("Manual MATH calculation time:", end_time - start_time)

start_time = timeit.default_timer()
for i in range(num_repeats):
    distance_man = np.ceil(p1_arr)
end_time = timeit.default_timer()
print("Numpy Ceil calculation time:", end_time - start_time)

start_time = timeit.default_timer()
for i in range(num_repeats):
    distance_man = [math.ceil(p1_arr[0]), math.ceil(p1_arr[1]), math.ceil(p1_arr[2])]
end_time = timeit.default_timer()
print("Math Ceil calculation time:", end_time - start_time)