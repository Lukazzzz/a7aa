import matplotlib.patches
import matplotlib.pyplot as plt
import math
import numpy as np

def calc_radius(base, rad, no_periods, open_angle, amp):
    waves_per_complete_circle = (360/open_angle) * no_periods
    curve_angle = waves_per_complete_circle*rad
    while curve_angle < 0:
        curve_angle = curve_angle + 2*math.pi
    while curve_angle > 2*math.pi:
        curve_angle = curve_angle - 2*math.pi
    print(math.degrees(curve_angle))
    return amp*math.sin(waves_per_complete_circle*rad) + base

max_radius = 23.6
min_radius = 17.6
# This is the radius which the sine waves go around
radius = (max_radius+min_radius)/2

open_angle = 72
open_angle_rad = math.radians(open_angle)
phase_shift = 120

amplitude = (max_radius-min_radius)/2

# The coordinates of the center point
center_x = 0
center_y = 0
# The step the change in the angle
step = (2*math.pi)/360

start_angle = -open_angle_rad/2
end_angle = open_angle_rad/2


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
ax.set_aspect('equal')

for i in range(0, 360, phase_shift):
    x_points = []
    y_points = []
    angle = start_angle
    x_start = calc_radius(radius, start_angle-math.radians(i), 1, open_angle, amplitude) * math.sin(start_angle)
    y_start = calc_radius(radius, start_angle-math.radians(i), 1, open_angle, amplitude) * math.cos(start_angle)
    x_points.append(x_start)
    y_points.append(y_start)

    while angle < end_angle:
        angle = angle + step
        x_new = calc_radius(radius, angle-math.radians(i), 1, open_angle, amplitude) * math.sin(angle)
        y_new = calc_radius(radius, angle-math.radians(i), 1, open_angle, amplitude) * math.cos(angle)
        x_points.append(x_new)
        y_points.append(y_new)
        #print(math.degrees(angle-math.radians(i)))
        #print(x_new, y_new)
    print('\n\n')
    plt.plot(x_points, y_points)
    #plt.show()



angle = np.linspace(0, 2 * np.pi , 150)

circle_radius = radius
x_circle = circle_radius * np.cos(angle)
y_circle = circle_radius * np.sin(angle)
plt.plot(x_circle, y_circle)

# circle_radius = max_radius
# x_circle = circle_radius * np.cos(angle)
# y_circle = circle_radius * np.sin(angle)
# plt.plot(x_circle, y_circle)
#
# circle_radius = min_radius
# x_circle = circle_radius * np.cos(angle)
# y_circle = circle_radius * np.sin(angle)
# plt.plot(x_circle, y_circle)

plt.show()