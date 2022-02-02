import matplotlib.patches
import matplotlib.pyplot as plt
import math
import numpy as np

def calc_radius(base, rad):
    return 25*math.sin(5*rad) + base

radius = 100.0
center_x = 0
center_y = 0
step = (2*math.pi)/360
x_points = []
y_points = []
i = -math.pi/5
x0 = calc_radius(radius, i) * math.sin(i)
y0 = calc_radius(radius, i) * math.cos(i)
x_points.append(x0)
y_points.append(y0)


fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

# Move left y-axis and bottim x-axis to centre, passing through (0,0)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')

# Eliminate upper and right axes
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# Show ticks in the left and lower axes only
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')





while i < math.pi/5:
    i = i + step
    x1 = calc_radius(radius, i) * math.sin(i)
    y1 = calc_radius(radius, i) * math.cos(i)
    x_points.append(x1)
    y_points.append(y1)
plt.plot(x_points, y_points)

x_points = []
y_points = []
i = -math.pi/5
x0 = calc_radius(radius, i-math.pi/6) * math.sin(i)
y0 = calc_radius(radius, i-math.pi/6) * math.cos(i)
x_points.append(x0)
y_points.append(y0)
while i < math.pi/5:
    i = i + step
    x1 = calc_radius(radius, i-math.pi/6) * math.sin(i)
    y1 = calc_radius(radius, i-math.pi/6) * math.cos(i)
    x_points.append(x1)
    y_points.append(y1)
plt.plot(x_points, y_points)

x_points = []
y_points = []
i = -math.pi/5
x0 = calc_radius(radius, i-math.pi/6-math.pi/6) * math.sin(i)
y0 = calc_radius(radius, i-math.pi/6-math.pi/6) * math.cos(i)
x_points.append(x0)
y_points.append(y0)
while i < math.pi/5:
    i = i + step
    x1 = calc_radius(radius, i-math.pi/6-math.pi/6) * math.sin(i)
    y1 = calc_radius(radius, i-math.pi/6-math.pi/6) * math.cos(i)
    x_points.append(x1)
    y_points.append(y1)
plt.plot(x_points, y_points)

angle = np.linspace( 0 , 2 * np.pi , 150 )

radius = 100
x_circle = radius * np.cos(angle)
y_circle = radius * np.sin(angle)
plt.plot(x_circle, y_circle)

radius = 125
x_circle = radius * np.cos(angle)
y_circle = radius * np.sin(angle)
plt.plot(x_circle, y_circle)

radius = 75
x_circle = radius * np.cos(angle)
y_circle = radius * np.sin(angle)
plt.plot(x_circle, y_circle)




ax.set_aspect('equal')
plt.show()