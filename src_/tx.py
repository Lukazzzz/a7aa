import math
import matplotlib.pyplot as plt


def draw_arc(r, ds, theta_rad):

    current_theta = theta_rad
    d_theta = ds / r
    start_x = r * math.cos(current_theta)
    start_y = r * math.sin(current_theta)
    end_x = -start_x
    end_y = start_y
    current_x = start_x
    current_y = start_y

    while current_x > end_x:
        current_theta = current_theta + d_theta
        next_x = r * math.cos(current_theta)
        next_y = r * math.sin(current_theta)
        plt.scatter([current_x, next_x], [current_y, next_y])
        current_x = next_x
        current_x = next_y

    return

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

draw_arc(15.7, 0.02, math.radians(24))
plt.show()
