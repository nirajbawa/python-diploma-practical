import numpy as np
import matplotlib.pyplot as plt

def plot_line():
    a = np.array([5, 10, 15, 20, 25])
    plt.plot(a)
    plt.show()

def plot_bar():
    x = [2,4,6]
    y = [5,10,8]
    plt.bar(x,y)
    plt.show()
    
def plot_scattered():
    x = [2,4,6,8]
    y = [5,10,8,5]
    plt.scatter(x,y)
    plt.show()
    
def plot_parabloa():
    t = np.linspace(0, 1, 100)
    plt.plot(t, t**2)
    plt.show()
    

plot_line()
plot_bar()
plot_scattered()
plot_parabloa()
