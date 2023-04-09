import matplotlib.pyplot as plt
import random
import numpy as np

counter = 0
iterations = 10000
triangle_points = [[-1, 1, 0],[0, 0, 1]]
triangle_points = np.array(triangle_points)
x_triangle_points = triangle_points[0,:]
y_triangle_points = triangle_points[1,:]
plt.scatter(x_triangle_points, y_triangle_points, s = 3)

x_min = -1
x_max = 1

x_rand = (x_max-x_min)*random.uniform(0, 1) + x_min

y_min = 0

if x_rand < 0:
    y_max = x_rand + 1
elif x_rand > 0:
    y_max = -x_rand + 1
else:
    print('error')

y_rand = (y_max-y_min)*random.uniform(0,1) + y_min

plt.scatter(x_rand, y_rand, s = 3)

X = [];
X = np.array(X)
Y = [];
Y = np.array(Y)

while counter < iterations:
    random_corner = random.randint(0,2)
    corner  = triangle_points[:,random_corner]
    counter = counter + 1
    x_new = (x_rand + corner[0]) / 2
    y_new = (y_rand + corner[1]) / 2
    X = np.hstack((X, x_new))
    Y = np.hstack((Y, y_new))
    x_rand = x_new
    y_rand = y_new

plt.scatter(X,Y, s = 3)
plt.show()
