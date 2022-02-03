import matplotlib.patches
import matplotlib.pyplot as plt
import math
import numpy as np


def get_arc_points(r, angle, dx, center=(0, 0)):
    l = 2*r*math.cos(math.radians((180-angle)/2))
    x_start = center[0] + l/2
    x_end = center[0] - l/2
    y_start = math.sqrt(r * r - x_start * x_start) + center[1]
    y_end = y_start
    theta = math.degrees(math.asin((y_start-center[1]) / r))
    d_theta = (dx / r) * (180 / math.pi)

    x_points = [x_start]
    y_points = [y_start]
    current_x = x_start

    while current_x > x_end:
        theta = theta + d_theta
        next_x = r*math.cos(math.radians(theta))
        next_y = r*math.sin(math.radians(theta)) + center[1]
        x_points.append(next_x)
        y_points.append(next_y)
        current_x = next_x

    x_points.append(x_end)
    y_points.append(y_end)

    return x_points, y_points


tx_layers=['In2.Cu','B.Cu']
netclass = 0
TXCoilTrackWidth=0.4
TXCoilDisTrack=0.15
tx_max_radius = 25.6
tx_min_radius = 15.7
tx_open_angle = 132
tx_dx = 0.02
ds = TXCoilTrackWidth + TXCoilDisTrack
d_alpha = (ds / 15.7) * (180 / math.pi)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

# Move left y-axis and bottim x-axis to centre, passing through (0,0)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
#
# # Eliminate upper and right axes
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
#
# # Show ticks in the left and lower axes only
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.set_aspect('equal')

# arc1_x, arc1_y = get_arc_points(tx_min_radius, tx_open_angle, tx_dx)
# plt.plot(arc1_x, arc1_y, color='b')
#
# arc2_x, arc2_y = get_arc_points(tx_max_radius, tx_open_angle, tx_dx)
# plt.plot(arc2_x, arc2_y, color='b')
#
# #plt.plot([arc1_x[-1], arc2_x[-1]], [arc1_y[-1], arc2_y[-1]], color='b')
#
# arc3_x, arc3_y = get_arc_points(tx_min_radius-TXCoilDisTrack-TXCoilTrackWidth, tx_open_angle, tx_dx, center=(0, TXCoilDisTrack+TXCoilTrackWidth))
# plt.plot(arc3_x, arc3_y, color='r')
#
# arc4_x, arc4_y = get_arc_points(tx_max_radius-TXCoilDisTrack-TXCoilTrackWidth, tx_open_angle, tx_dx, center=(0, TXCoilDisTrack+TXCoilTrackWidth))
# plt.plot(arc4_x, arc4_y, color='r')

#plt.plot([arc3_x[-1], arc4_x[-1]], [arc3_y[-1], arc4_y[-1]], color='r')

angle = np.linspace(0, 2 * np.pi , 360)

circle_radius = tx_max_radius
x_circle = circle_radius * np.cos(angle)
y_circle = circle_radius * np.sin(angle)
plt.plot(x_circle, y_circle, color='b')

circle_radius = tx_max_radius - TXCoilTrackWidth-TXCoilDisTrack
x_circle = circle_radius * np.cos(angle)
y_circle = circle_radius * np.sin(angle)
plt.plot(x_circle, y_circle, color='r')

circle_radius = tx_min_radius
x_circle = circle_radius * np.cos(angle)
y_circle = circle_radius * np.sin(angle)
plt.plot(x_circle, y_circle, color='b')

circle_radius = tx_min_radius + TXCoilTrackWidth+TXCoilDisTrack
x_circle = circle_radius * np.cos(angle)
y_circle = circle_radius * np.sin(angle)
plt.plot(x_circle, y_circle, color='r')

x = tx_max_radius*math.cos(math.radians(24))
y = tx_max_radius*math.sin(math.radians(24))

plt.plot([0, tx_max_radius*math.cos(math.radians(24))], [0, tx_max_radius*math.sin(math.radians(24))], color='b')
plt.show()