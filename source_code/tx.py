import math
import matplotlib.pyplot as plt


def draw_arc(r, ds, theta_rad):

    current_theta = theta_rad
    d_theta = ds / r
    start_x = r * math.cos(current_theta)
    start_y = r * math.sin(current_theta)
    end_x = -start_x
    current_x = start_x
    current_y = start_y
    cad_code = ''
    while current_x > end_x:
        current_theta = current_theta + d_theta
        next_x = r * math.cos(current_theta)
        next_y = r * math.sin(current_theta)
        cad_code = cad_code + '\n'+("(segment (start %0.3f %0.3f) (end %0.3f %0.3f) (width %0.4f) (layer %s) (net %d))"
                                    % (current_x, current_y, next_x, next_y, TXCoilTrackWidth, tx_layers[0], netclass))
        cad_code = cad_code + '\n'+("(segment (start %0.3f %0.3f) (end %0.3f %0.3f) (width %0.4f) (layer %s) (net %d))"
                                    % (current_x, current_y, next_x, next_y, TXCoilTrackWidth, tx_layers[1], netclass))

        # uncomment next line for drawing
        # plt.plot([current_x, next_x], [current_y, next_y])

        current_x = next_x
        current_y = next_y

    return current_x, current_y, cad_code


tx_layers = ['In2.Cu','B.Cu']
netclass = 0
TXCoilTrackWidth = 0.4
TXCoilDisTrack = 0.15
tx_ds = 0.02
delta = TXCoilTrackWidth + TXCoilDisTrack
tx_min_radius = 15.7
tx_max_radius = 25.6
open_angle = 132
tx_angle = math.radians(open_angle)
# tx_max_d_angle = tx_ds / tx_max_radius
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

arc1_x, arc1_y, code = draw_arc(tx_min_radius, tx_ds, (math.pi-tx_angle)/2)
s_append = s_append + code
arc2_x, arc2_y, code = draw_arc(tx_min_radius + delta, tx_ds, (math.pi-tx_angle)/2 + delta/tx_min_radius)
s_append = s_append + code
arc3_x, arc3_y, code = draw_arc(tx_min_radius + 2*delta, tx_ds, (math.pi-tx_angle)/2 + 2*delta/tx_min_radius)
s_append = s_append + code

arc4_x, arc4_y, code = draw_arc(tx_max_radius - 2*delta, tx_ds, (math.pi-tx_angle)/2 + 2*delta/tx_max_radius)
s_append = s_append + code
arc5_x, arc5_y, code = draw_arc(tx_max_radius - delta, tx_ds, (math.pi-tx_angle)/2 + delta/tx_max_radius)
s_append = s_append + code
arc6_x, arc6_y, code = draw_arc(tx_max_radius, tx_ds, (math.pi-tx_angle)/2)
s_append = s_append + code

s_append = s_append + '\n'+("(segment (start %0.3f %0.3f) (end %0.3f %0.3f) (width %0.4f) (layer %s) (net %d))"
                            % (arc1_x, arc1_y, arc6_x, arc6_y, TXCoilTrackWidth, tx_layers[0], netclass))

s_append = s_append + '\n'+("(segment (start %0.3f %0.3f) (end %0.3f %0.3f) (width %0.4f) (layer %s) (net %d))"
                            % (arc2_x, arc2_y, arc5_x, arc5_y, TXCoilTrackWidth, tx_layers[0], netclass))

s_append = s_append + '\n'+("(segment (start %0.3f %0.3f) (end %0.3f %0.3f) (width %0.4f) (layer %s) (net %d))"
                            % (arc3_x, arc3_y, arc4_x, arc4_y, TXCoilTrackWidth, tx_layers[0], netclass))


f = open('kiCad_code_tx.txt', 'w')
f.write(s_append)
f.close()

# uncomment next lines to show the drawing
# plt.plot([arc1_x, arc6_x], [arc1_y, arc6_y])
# plt.plot([arc2_x, arc5_x], [arc2_y, arc5_y])
# plt.plot([arc3_x, arc4_x], [arc3_y, arc4_y])
# plt.show()
