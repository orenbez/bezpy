# http://matplotlib.org/
# https://www.youtube.com/watch?v=UO98lJQ3QGI&list=PL-osiE80TeTvipOqomVEeZ1HRrcEvtZB_
# Color Pallette: https://matplotlib.org/gallery/color/named_colors.html#sphx-glr-gallery-color-named-colors-py


# plt.cla()   #clears an axes, i.e. the currently active axes in the current figure. It leaves the other axes untouched.
# plt.clf()   #clears the entire current figure with all its axes, but leaves the window opened, such that it may be reused for other plots.
# plt.close() #closes a window, which will be the current window, if not specified otherwise.
# plt.show(block=True)  defaults to true when you are running program which will pause program and
#                      require you to exit to continue
# plt.show(block=False) defaults to false in 'interactive/debug' mode where the image doesn not require you
#                       to exit to continue program

# plt.pause() #  pause for interval seconds

# import matplotlib.pyplot as plt
# import numpy as np
#
# # Data for plotting
# t = np.arange(0.0, 2.0, 0.01)
# s = 1 + np.sin(2 * np.pi * t)
#
# fig, ax = plt.subplots()
# ax.plot(t, s)
#
# ax.set(xlabel='time (s)', ylabel='voltage (mV)',
#        title='About as simple as it gets, folks')
# ax.grid()
#
# fig.savefig("test.png")
# plt.show()

import matplotlib.pyplot as plt
from random import choice

class RandomWalk():
    def __init__(self, num_points=500):
        self.num_points = num_points
        self.x_values = [0]  # All walks start at (0, 0).
        self.y_values = [0]

    def fill_walk(self):
        while len(self.x_values) < self.num_points:
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance
            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance
            if x_step == 0 and y_step == 0:
                continue             # Reject moves that go nowhere.
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step
            self.x_values.append(next_x)
            self.y_values.append(next_y)




plt.title("Plot Title", fontsize=24, fontweight=0, color='grey', loc='left')    # Set chart title
plt.xlabel("X-Values", fontsize=14)            # Set axis label
plt.ylabel("Y-Values", fontsize=14)
plt.tick_params(axis='both', labelsize=14)  # Set Values font-size

# plt.style.available # lists all available background styles
# plt.style.use('ggplot') # sets nice default style
# plt.xkcd()  # built-in cartoon style

x_values = list(range(1, 101))
y_values1 = [x**2 for x in x_values]
y_values2 = [x**3 for x in x_values]
plt.axis([0, 40, 0, 2000]) # Sets range for both axes
plt.grid(True) # sets background grid
plt.plot(x_values, y_values1, color='#5a7d9a', linestyle='--', linewidth=5, label='Squared')
plt.plot(x_values, y_values2, color='red', linewidth=2, marker='x',  label='Cubed')   # s gives diameter of the dot
plt.legend()   # from the label values in your plots,  OR provide a list of labels in the order they were plotted plt.legend(['Squared','Cubed'])
plt.tight_layout()   # May improve the padding of the figure
plt.show()
plt.clf()




plt.scatter(1,1, s=100)
plt.scatter(2,1, c='red', edgecolor='blue', s=300)  # set dot to red color with blue edge
axes = plt.gca()      # Returns axes object
axes.set_ylim([0, 1.5]) # Set Range for y-axis only
plt.show()
plt.clf()

x_values = list(range(101))
y_values = [x**2 for x in x_values]

# Sets output blue color as a function of the y_values
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor='none', s=40)
plt.savefig(r'.\myfiles\squares_plot.png')
plt.close()


rw = RandomWalk(100000)
rw.fill_walk()
plt.figure(dpi=128, figsize=(10, 6))  # Open new figure to specific size
# gradients stronger blue increasing by y-value
#plt.scatter(rw.x_values, rw.y_values, c=rw.y_values, cmap=plt.cm.Blues, edgecolor='none',  s=15)
point_numbers = list(range(rw.num_points))

# gradients blue increasing by 'step'
plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.rainbow, edgecolor='none', s=1)
plt.scatter(0, 0, c='green', edgecolors='none', s=50)  # Start Position Green Dot
plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=50) # Last Position  Green dot
plt.show()




