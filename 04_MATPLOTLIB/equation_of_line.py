import matplotlib.pyplot as plt
from matplotlib import style
from math import sqrt

# m = gradient, c = constant (y-intercept)
def draw_line(m, c, color):
    x_values = list(range(-500,500))
    line = [m*x + c for x in x_values]
    plt.plot(x_values, line, c=color)
    set_axis()

def draw_circle(r, color):
    x_values2 = list(range(-1*r,r+1))
    line1 = [sqrt(r**2 - x**2) for x in x_values2]
    line2 = [-sqrt(r**2 - x**2) for x in x_values2]
    plt.plot(x_values2, line1, c=color)
    plt.plot(x_values2, line2, c=color)
    set_axis()

def set_axis():
    plt.axis('scaled')   # draw graph with x-y to scale
    plt.axhline(0, color='black')   # draw x-axis
    plt.axvline(0, color='black')   # draw y-axis
    plt.xlabel("x-axis", fontsize=12) #label x-axis
    plt.ylabel("y-axis", fontsize=12) #label y-axis    


if __name__ == '__main__':

    plt.style.use(u'seaborn-darkgrid')
    
    

    draw_line(1, 100, 'red')
    draw_line(2, 200, 'orange')
    draw_line(3, 300, 'yellow')
    draw_circle(50, 'green')

    
    #a = [0.5 , 1, 2, 3, 4, 5, 6]
    #col = ['red', 'yellow', 'orange', 'green', 'blue', 'indigo', 'violet']
    #for i in range(0,7):
    #draw_line(a[i],0, col[i])

    plt.show()    
