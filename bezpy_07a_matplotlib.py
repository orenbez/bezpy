### TRY ME  https://towardsdatascience.com/an-ultimate-cheat-sheet-for-data-visualization-in-pandas-f7bc239c9937
# https://python-graph-gallery.com/199-matplotlib-style-sheets/

# SEE notebooks/graphs.ipynb

import pandas_datareader.data as pdr  # pip install pandas-datareader
import matplotlib.pyplot as plt       # p
import matplotlib as mpl
from datetime import datetime as dt

mpl.rcParams['font.size'] = 9.0

#=======================================================================================================================
#   Scatter Vs. Plot
#=======================================================================================================================
x_values = [0, 1, 2, 3, 4, 5]
squares = [0, 1, 4, 9, 16, 25]
plt.style.available # lists all available background styles
plt.style.use('seaborn-darkgrid') #sets nice default style
plt.plot(x_values, squares)   # 'plot' will connect dots as best it can
plt.show()


x_values2 = list(range(-1000,1000))
squares2 = [x**2 for x in x_values2]
#'scatter' will only draw points of size '8'
plt.style.use(u'seaborn-dark-palette') #sets nice checked background
plt.scatter(x_values2, squares2, s=8)  # scatter won't connect the dots s = marker point size
plt.title("Y = X**2", fontsize=24)
plt.xlabel("x-axis", fontsize=18)
plt.ylabel("y-axis", fontsize=18)
plt.tick_params(axis='both', which='major', labelsize=12)  # sets size of the labeled numbers on the axis
plt.axis([-1100, 1100, -500, 1100000])     # sets axis range
plt.show()


plt.figure(dpi=128, figsize=(5, 3)) # Open new figure to specific size
plt.scatter(x_values2, squares2, c='orange', cmap=plt.cm.rainbow, edgecolor='none', s=10)
plt.scatter(x_values2[0], squares2[0], c='green', edgecolor='none', s=20)
plt.scatter(x_values2[-1], squares2[-1], c='red', edgecolor='none', s=20)
plt.title("Y = X\u00B2", fontsize=16)
plt.show()


# Filling the space between data sets
x_values3 = list(range(-100,100))
squares3 = [x**2 for x in x_values3]
cubes3 = [x**3 for x in x_values3]
plt.plot(x_values3, squares3, c='blue')
plt.plot(x_values3, cubes3, c='red')
plt.axis([-100, 100, -2000, 2000])
plt.fill_between(x_values3, cubes3, squares3, facecolor='pink', alpha=0.25)
plt.show()


# SHARING AN X-AXIS
x_vals4 = list(range(11))
squares4 = [x**2 for x in x_vals4]
cubes4 = [x**3 for x in x_vals4]
fig, axarr = plt.subplots(2, 1, sharex=True)
axarr[0].plot(x_vals4, squares4)
axarr[0].set_title('Squares')
axarr[1].plot(x_vals4, cubes4, c='red')
axarr[1].set_title('Cubes')
plt.show()

# SHARING A Y-AXIS
x_vals5 = list(range(11))
squares5 = [x**2 for x in x_vals5]
cubes5 = [x**3 for x in x_vals5]
fig, axarr = plt.subplots(1, 2, sharey=True)
axarr[0].plot(x_vals5, squares5)
axarr[0].set_title('Squares')
axarr[1].plot(x_vals5, cubes5, c='red')
axarr[1].set_title('Cubes')
plt.show()

from matplotlib import dates as mdates
plt.style.use(u'seaborn-dark-palette')
dates = [dt(2016, 6, 21), dt(2016, 6, 22),dt(2016, 6, 23), dt(2016, 6, 24)]
highs = [57, 68, 64, 59]
fig = plt.figure(dpi=128, figsize=(10,6))
plt.plot(dates, highs, c='red')
plt.title("Daily High Temps", fontsize=24)
plt.ylabel("Temp (F)", fontsize=16)

# x_axis = plt.axes().get_xaxis()
# x_axis.set_major_formatter(mdates.DateFormatter('%B %d %Y'))
# fig.autofmt_xdate()

plt.show()



#=======================================================================================================================
#   Plot data from PANDAS (see bezpy_06b_pandas_plots.py)
#=======================================================================================================================
start = dt(2018, 1, 1)
end = dt.now()

df2 = pdr.DataReader("GOOG","yahoo", start, end)
df2 = df2.drop(columns = ['Open','Close','Volume'])  # This drops columns from data_frame
df2.columns # lists columns  Index(['High', 'Low', 'Adj Close'], dtype='object')

print(df2.head())


plt.style.use('fivethirtyeight')
df2['High'].plot()  # Plots against index which is the data column
df2['Low'].plot()   # Plots against index which is the data column
plt.legend()        # this will generate the legend in the graph
plt.show()          # displays the image




# Data to plot
labels = 'Python', 'C++', 'Ruby', 'Java'
sizes = [215, 130, 245, 210]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0.1, 0, 0, 0)  # explode 1st slice
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')
plt.show()


#=======================================================================================================================
# 2nd CHART
#=======================================================================================================================
labels = ['Cookies', 'Jellybean', 'Milkshake', 'Cheesecake']
sizes = [38.4, 40.6, 20.7, 10.3]
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
patches, texts = plt.pie(sizes, colors=colors, shadow=True, startangle=90)


#Or you can modify the labels after they have been created. When you call ax.pie it returns a tuple of (patches, texts, autotexts). As an example, modify your final few lines of code as follows:
#patches, texts, autotexts = ax.pie(frac, colors=colors, labels=labels, autopct='%1.1f%%')
#texts[0].set_fontsize(4)

#plt.title('TITLE')
plt.legend(patches, labels, loc="best")
plt.axis('equal')
plt.tight_layout()
plt.show()
plt.savefig('myfiles\\chart.png', bbox_inches='tight', transparent=True)



