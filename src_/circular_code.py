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

    return amp*math.sin(waves_per_complete_circle*rad) + base, curve_angle

max_radius = 23.6
min_radius = 17.6
# This is the radius which the sine waves go around
radius = (max_radius+min_radius)/2

open_angle = 72
open_angle_rad = math.radians(open_angle)
phase_shift = 60

amplitude = (max_radius-min_radius)/2

# The coordinates of the center point
center_x = 0
center_y = 0
# The step the change in the angle
step = (2*math.pi)/360

start_angle = -open_angle_rad/2
end_angle = open_angle_rad/2

rx_layers=['F.Cu','In1.Cu']
RXCoilTrackWidth = 0.2
netclass = 0

# waves[0][j]:
# j=0 for x points of layer1 in wave 1
# j=1 for y points of layer1 in wave 1
# j=2 for x points of layer2 in wave 1
# j=3 for y points of layer2 in wave 1
waves = [[[], [], [], []], [[], [], [], []], [[], [], [], []], [[], [], [], []], [[], [], [], []], [[], [], [], []]]

s_append = ''

# fig = plt.figure()
# ax = fig.add_subplot(1, 1, 1)

# Move left y-axis and bottim x-axis to centre, passing through (0,0)
# ax.spines['left'].set_position('center')
# ax.spines['bottom'].set_position('center')
#
# # Eliminate upper and right axes
# ax.spines['right'].set_color('none')
# ax.spines['top'].set_color('none')
#
# # Show ticks in the left and lower axes only
# ax.xaxis.set_ticks_position('bottom')
# ax.yaxis.set_ticks_position('left')
# ax.set_aspect('equal')

for i in range(0, 360, phase_shift):
    x_points_layer1 = []
    y_points_layer1 = []
    x_points_layer2 = []
    y_points_layer2 = []
    angle = start_angle
    x_start, curve_angle = calc_radius(radius, start_angle-math.radians(i), 1, open_angle, amplitude)
    x_start = x_start * math.sin(start_angle)
    y_start, curve_angle = calc_radius(radius, start_angle-math.radians(i), 1, open_angle, amplitude)
    y_start = y_start * math.cos(start_angle)
    if math.pi/2 <= curve_angle < (3*math.pi)/2:
        x_points_layer1.append(x_start)
        y_points_layer1.append(y_start)
    else:
        x_points_layer2.append(x_start)
        y_points_layer2.append(y_start)

    while angle < end_angle:
        angle = angle + step
        x_new, curve_angle = calc_radius(radius, angle-math.radians(i), 1, open_angle, amplitude)
        x_new = x_new * math.sin(angle)
        y_new, curve_angle = calc_radius(radius, angle-math.radians(i), 1, open_angle, amplitude)
        y_new = y_new * math.cos(angle)
        if math.pi/2 <= curve_angle < (3*math.pi)/2:
            x_points_layer1.append(x_new)
            y_points_layer1.append(y_new)
        else:
            x_points_layer2.append(x_new)
            y_points_layer2.append(y_new)

    waves[i//60][0] = x_points_layer1
    waves[i//60][1] = y_points_layer1
    waves[i//60][2] = x_points_layer2
    waves[i//60][3] = y_points_layer2

    # plt.scatter(x_points_layer1, y_points_layer1, color="y")
    # plt.scatter(x_points_layer2, y_points_layer2, color="r")

for i in range(len(waves)):
    for j in range(len(waves[i][0]) - 1):
        start_x = waves[i][0][j]
        start_y = waves[i][1][j]
        end_x = waves[i][0][j+1]
        end_y = waves[i][1][j+1]
        if abs(start_x-end_x) > 1:
            continue
        else:
            s_append = s_append + '\n'+("(segment (start %0.3f %0.3f) (end %0.3f %0.3f) (width %0.4f) (layer %s) (net %d))"
                                    % (start_x, start_y, end_x, end_y, RXCoilTrackWidth, rx_layers[0], netclass))

    for k in range(len(waves[i][2]) - 1):
        start_x = waves[i][2][k]
        start_y = waves[i][3][k]
        end_x = waves[i][2][k+1]
        end_y = waves[i][3][k+1]
        if abs(start_x-end_x) > 1:
            continue
        else:
            s_append = s_append + '\n'+("(segment (start %0.3f %0.3f) (end %0.3f %0.3f) (width %0.4f) (layer %s) (net %d))"
                                    % (start_x, start_y, end_x, end_y, RXCoilTrackWidth, rx_layers[1], netclass))

f=open('kiCad_code.txt','w')
f.write(s_append)
f.close()


# angle = np.linspace(0, 2 * np.pi , 150)
#
# circle_radius = radius
# x_circle = circle_radius * np.cos(angle)
# y_circle = circle_radius * np.sin(angle)
# plt.plot(x_circle, y_circle)

# circle_radius = max_radius
# x_circle = circle_radius * np.cos(angle)
# y_circle = circle_radius * np.sin(angle)
# plt.plot(x_circle, y_circle)
#
# circle_radius = min_radius
# x_circle = circle_radius * np.cos(angle)
# y_circle = circle_radius * np.sin(angle)
# plt.plot(x_circle, y_circle)

# plt.show()