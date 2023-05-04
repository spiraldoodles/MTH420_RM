# matplotlib_intro.py
"""Python Essentials: Intro to Matplotlib.
<Name> Rebecca Munk
<Class> MTH 420
<Date> 4/27/23
"""
import numpy as np
from matplotlib import pyplot as plt

# Problem 1
def var_of_means(n):
    """ Create an (n x n) array of values randomly sampled from the standard
    normal distribution. Compute the mean of each row of the array. Return the
    variance of these means.

    Parameters:
        n (int): The number of rows and columns in the matrix.

    Returns:
        (float) The variance of the means of each row.
    """
    A= np.random.normal(size=(n,n))
    Ameans= np.mean(A, axis=0)
    Avars= np.var(Ameans, axis=0)
    return Avars
        

def prob1():
    """ Create an array of the results of var_of_means() with inputs
    n = 100, 200, ..., 1000. Plot and show the resulting array.
    """
    ns= np.arange(100,1001,100)
    V=np.zeros(len(ns))
    for index in range(len(ns)):
        V[index]=var_of_means(ns[index])
    plt.plot(ns,V)

# Problem 2
def prob2():
    """ Plot the functions sin(x), cos(x), and arctan(x) on the domain
    [-2pi, 2pi]. Make sure the domain is refined enough to produce a figure
    with good resolution.
    """
    plt.figure()
    domain=np.linspace(-2*np.pi, 2*np.pi, 100)
    
    plt.plot(domain, np.sin(domain))
    plt.plot(domain, np.cos(domain))
    plt.plot(domain, np.arctan(domain))


# Problem 3
def prob3():
    """ Plot the curve f(x) = 1/(x-1) on the domain [-2,6].
        1. Split the domain so that the curve looks discontinuous.
        2. Plot both curves with a thick, dashed magenta line.
        3. Set the range of the x-axis to [-2,6] and the range of the
           y-axis to [-6,6].
    """
    plt.figure()
    domain1=np.linspace(-2, 1, 100, endpoint=False)
    domain2=np.linspace(1, 6, 100)[1:]
    
    plt.plot(domain1, 1/(domain1-1), linestyle="dashed", color="magenta", linewidth=4)
    plt.plot(domain2, 1/(domain2-1), linestyle="dashed", color="magenta", linewidth=4)
    plt.xlim(-2, 6)
    plt.ylim(-6, 6)




# Problem 4
def prob4():
    """ Plot the functions sin(x), sin(2x), 2sin(x), and 2sin(2x) on the
    domain [0, 2pi], each in a separate subplot of a single figure.
        1. Arrange the plots in a 2 x 2 grid of subplots.
        2. Set the limits of each subplot to [0, 2pi]x[-2, 2].
        3. Give each subplot an appropriate title.
        4. Give the overall figure a title.
        5. Use the following line colors and styles.
              sin(x): green solid line.
             sin(2x): red dashed line.
             2sin(x): blue dashed line.
            2sin(2x): magenta dotted line.
    """
    plt.figure()
    x=np.linspace(0, 2*np.pi, 100)
    
    sub1= plt.subplot(221)
    sub1.plot(x,np.sin(x), color="green")
    sub1.set_title("sin(x)")

    sub2= plt.subplot(222)
    sub2.plot(x,np.sin(2*x), color="red", linestyle="dashed")
    sub2.set_title("sin(2x)")

    sub3= plt.subplot(223)
    sub3.plot(x,2*np.sin(x), color="blue", linestyle="dashed")
    sub3.set_title("2sin(x)")

    sub4= plt.subplot(224)
    sub4.plot(x,2*np.sin(2*x), color="magenta", linestyle="dotted")
    sub4.set_title("2sin(2x)")

    plt.axis([0, 2*np.pi, -2, 2])
    plt.suptitle("Have some plots, take two they're small.")


# # Problem 5
# def prob5():
#     """ Visualize the data in FARS.npy. Use np.load() to load the data, then
#     create a single figure with two subplots:
#         1. A scatter plot of longitudes against latitudes. Because of the
#             large number of data points, use black pixel markers (use "k,"
#             as the third argument to plt.plot()). Label both axes.
#         2. A histogram of the hours of the day, with one bin per hour.
#             Label and set the limits of the x-axis.
#     """
#     raise NotImplementedError("Problem 5 Incomplete")


# Problem 6
def prob6():
    """ Plot the function g(x,y) = sin(x)sin(y)/xy on the domain
    [-2pi, 2pi]x[-2pi, 2pi].
        1. Create 2 subplots: one with a heat map of g, and one with a contour
            map of g. Choose an appropriate number of level curves, or specify
            the curves yourself.
        2. Set the limits of each subplot to [-2pi, 2pi]x[-2pi, 2pi].
        3. Choose a non-default color scheme.
        4. Include a color scale bar for each subplot.
    """
    plt.figure()
    x=np.linspace(-2*np.pi, 2*np.pi, 100)
    y=np.linspace(-2*np.pi, 2*np.pi, 100)
    X, Y = np.meshgrid(x,y)
    Z=np.sin(X)*np.sin(Y)/(X*Y)

    plt.subplot(121)
    plt.pcolormesh(X, Y, Z, cmap="viridis", shading="auto")
    plt.colorbar()

    plt.subplot(122)
    plt.contour(X, Y, Z, cmap="coolwarm", levels=10)
    plt.colorbar()

    
prob1()
prob2()
prob3()
prob4()
prob6()    

plt.show()