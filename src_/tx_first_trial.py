import matplotlib.patches
import matplotlib.pyplot as plt
import math

def get_arc_points(r, angle, dx, center=(0, 0)):
    l = 2*r*math.cos(math.radians((180-angle)/2))
    x_start = center[0] + l/2
    x_end = center[0] - l/2
    y_start = math.sqrt(r * r - x_start * x_start) + center[1]
    y_end = y_start
    theta = math.degrees(math.asin(y_start / r))
    d_theta = (dx / r) * (180 / math.pi)

    x_points = [x_start]
    y_points = [y_start]
    current_x = x_start

    while current_x > x_end:
        theta = theta + d_theta
        next_x = r*math.cos(math.radians(theta))
        next_y = r*math.sin(math.radians(theta))
        x_points.append(next_x)
        y_points.append(next_y)
        current_x = next_x

    x_points.append(x_end)
    y_points.append(y_end)

    return x_points, y_points

def draw_tx(x_points, y_points):
    global s_append
    for i in range(len(x_points)-2):
        start_x = x_points[i]
        end_x = x_points[i+1]
        start_y = y_points[i]
        end_y = y_points[i + 1]

        s_append = s_append + '\n' + ("(segment (start %0.3f %0.3f) (end %0.3f %0.3f) (width %0.4f) (layer %s) (net %d))" % (
            start_x, start_y, end_x, end_y, TXCoilTrackWidth, tx_layers[0], netclass))

        s_append = s_append + '\n' + ("(segment (start %0.3f %0.3f) (end %0.3f %0.3f) (width %0.4f) (layer %s) (net %d))" % (
            start_x, start_y, end_x, end_y, TXCoilTrackWidth, tx_layers[1], netclass))

rx_layers=['F.Cu','In1.Cu']
tx_layers=['In2.Cu','B.Cu']
netclass = 0
TXCoilTrackWidth=0.4
TXCoilDisTrack=0.15
ds = TXCoilTrackWidth + TXCoilDisTrack
d_alpha = (ds / 15.7) * (180 / math.pi)
s_append=''


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

x1, y1 = get_arc_points(15.7, 132, 0.02)
plt.plot(x1, y1, color='b')

x2, y2 = get_arc_points(25.6, 132, 0.02)
plt.plot(x2, y2, color='b')

plt.plot([x1[-1], x2[-1]], [y1[-1], y2[-1]], color='b')
plt.show()

x3, y3 = get_arc_points(15.7, 132, 0.02, center=(0, TXCoilDisTrack+TXCoilTrackWidth))
plt.plot(x3, y3, color='r')

x4, y4 = get_arc_points(25.6, 132, 0.02, center=(0, -TXCoilDisTrack-TXCoilTrackWidth))
plt.plot(x4, y4, color='r')

plt.plot([x3[-1], x4[-1]], [y3[-1], y4[-1]], color='r')
plt.show()

x5, y5 = get_arc_points(15.7, 132, 0.02, center=(0, 2*(TXCoilDisTrack+TXCoilTrackWidth)))
plt.plot(x5, y5, color='g')

x6, y6 = get_arc_points(25.6, 132, 0.02, center=(0, -2*(TXCoilDisTrack+TXCoilTrackWidth)))
plt.plot(x6, y6, color='g')

plt.plot([x5[-1], x6[-1]], [y5[-1], y6[-1]], color='g')
plt.show()
# x, y = get_arc_points(15.7, 132, 0.02)
# draw_tx(x, y)
# startX3 = x[-1]
# startY3 = y[-1]
#
# x, y = get_arc_points(15.7+TXCoilDisTrack+TXCoilTrackWidth, 132-d_alpha, 0.02)
# draw_tx(x, y)
#
# startX2 = x[-1]
# startY2 = y[-1]
#
# x, y = get_arc_points(15.7+2*TXCoilDisTrack+2*TXCoilTrackWidth, 132-2*d_alpha, 0.02)
# draw_tx(x, y)
#
# startX1 = x[-1]
# startY1 = y[-1]
#
#
# x, y = get_arc_points(25.6, 132, 0.02)
# draw_tx(x, y)
#
# endX3 = x[-1]
# endY3 = y[-1]
#
# x, y = get_arc_points(25.6-TXCoilDisTrack-TXCoilTrackWidth, 132-d_alpha, 0.02)
# draw_tx(x, y)
#
# endX2 = x[-1]
# endY2 = y[-1]
#
# x, y = get_arc_points(25.6-2*TXCoilDisTrack-2*TXCoilTrackWidth, 132-2*d_alpha, 0.02)
# draw_tx(x, y)
#
# endX1 = x[-1]
# endY1 = y[-1]
#
# s_append = s_append + '\n' + ("(segment (start %0.3f %0.3f) (end %0.3f %0.3f) (width %0.4f) (layer %s) (net %d))" % (
#     startX1, startY1, endX1, endY1, TXCoilTrackWidth, tx_layers[0], netclass))
#
# s_append = s_append + '\n' + ("(segment (start %0.3f %0.3f) (end %0.3f %0.3f) (width %0.4f) (layer %s) (net %d))" % (
#     startX1, startY1, endX1, endY1, TXCoilTrackWidth, tx_layers[1], netclass))
#
#
# s_append = s_append + '\n' + ("(segment (start %0.3f %0.3f) (end %0.3f %0.3f) (width %0.4f) (layer %s) (net %d))" % (
#     startX2, startY2, endX2, endY2, TXCoilTrackWidth, tx_layers[0], netclass))
#
# s_append = s_append + '\n' + ("(segment (start %0.3f %0.3f) (end %0.3f %0.3f) (width %0.4f) (layer %s) (net %d))" % (
#     startX2, startY2, endX2, endY2, TXCoilTrackWidth, tx_layers[1], netclass))
#
#
# s_append = s_append + '\n' + ("(segment (start %0.3f %0.3f) (end %0.3f %0.3f) (width %0.4f) (layer %s) (net %d))" % (
#     startX3, startY3, endX3, endY3, TXCoilTrackWidth, tx_layers[0], netclass))
#
# s_append = s_append + '\n' + ("(segment (start %0.3f %0.3f) (end %0.3f %0.3f) (width %0.4f) (layer %s) (net %d))" % (
#     startX3, startY3, endX3, endY3, TXCoilTrackWidth, tx_layers[1], netclass))
#
# f=open('kiCad_code.txt','w')
# f.write(s_append)
# f.close()