import math
# import matplotlib.pyplot as plt


def calc_radius(base, rad, no_periods, open_angle, amp):
    waves_per_complete_circle = (360/open_angle) * no_periods
    curve_angle = waves_per_complete_circle*rad
    while curve_angle < 0:
        curve_angle = curve_angle + 2*math.pi
    while curve_angle > 2*math.pi:
        curve_angle = curve_angle - 2*math.pi

    return amp*math.sin(waves_per_complete_circle*rad) + base, curve_angle


rx_max_radius = 23.6
rx_min_radius = 17.6
# This is the radius which the sine waves go around
rx_radius = (rx_max_radius + rx_min_radius) / 2

rx_open_angle = 72
rx_open_angle_rad = math.radians(rx_open_angle)
rx_phase_shift = 60

amplitude = (rx_max_radius - rx_min_radius) / 2

# The coordinates of the center point
center_x = 0
center_y = 0
# The step the change in the angle
step = (2*math.pi)/360

rx_start_angle = -rx_open_angle_rad / 2
rx_end_angle = rx_open_angle_rad / 2

rx_layers = ['F.Cu', 'In1.Cu']
RXCoilTrackWidth = 0.2
netclass = 0

s_append = ''

########################## Uncomment for drawing ##########################
# fig = plt.figure()
# ax = fig.add_subplot(1, 1, 1)
#
# # Move left y-axis and bottim x-axis to centre, passing through (0,0)
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
#############################################################################

for i in range(0, 360, rx_phase_shift):
    angle = rx_start_angle
    current_x, current_angle = calc_radius(rx_radius, rx_start_angle - math.radians(i), 1, rx_open_angle, amplitude)
    current_x = current_x * math.sin(rx_start_angle)
    current_y, current_angle = calc_radius(rx_radius, rx_start_angle - math.radians(i), 1, rx_open_angle, amplitude)
    current_y = current_y * math.cos(rx_start_angle)
    if math.pi/2 <= current_angle < (3 * math.pi)/2:
        current_layer = rx_layers[0]
    else:
        current_layer = rx_layers[1]

    while angle < rx_end_angle:
        angle = angle + step
        next_x, next_angle = calc_radius(rx_radius, angle - math.radians(i), 1, rx_open_angle, amplitude)
        next_x = next_x * math.sin(angle)
        next_y, next_angle = calc_radius(rx_radius, angle - math.radians(i), 1, rx_open_angle, amplitude)
        next_y = next_y * math.cos(angle)
        if math.pi/2 <= next_angle < (3 * math.pi)/2:
            next_layer = rx_layers[0]
        else:
            next_layer = rx_layers[1]

        s_append = s_append + '\n'+("(segment (start %0.3f %0.3f) (end %0.3f %0.3f) (width %0.4f) (layer %s) (net %d))"
                                    % (current_x, current_y, next_x, next_y, RXCoilTrackWidth, current_layer, netclass))
        # uncomment next line for drawing
        # plt.plot([current_x, next_x], [current_y, next_y])

        current_x = next_x
        current_y = next_y
        current_layer = next_layer

f = open('kiCad_code_rx.txt', 'w')
f.write(s_append)
f.close()

# uncomment next line to show the drawing
# plt.show()
