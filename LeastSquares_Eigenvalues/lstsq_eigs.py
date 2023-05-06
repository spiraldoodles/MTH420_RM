# lstsq_eigs.py
"""Volume 1: Least Squares and Computing Eigenvalues.
<Name> Rebecca Munk
<Class> MTH 420
<Date> 5/5/23
"""

# (Optional) Import functions from your QR Decomposition lab.
# import sys
# sys.path.insert(1, "../QR_Decomposition")
# from qr_decomposition import qr_gram_schmidt, qr_householder, hessenberg

import numpy as np
from matplotlib import pyplot as plt
from scipy import linalg as la


# Problem 1
def least_squares(A, b):
    """Calculate the least squares solutions to Ax = b by using the QR
    decomposition.

    Parameters:
        A ((m,n) ndarray): A matrix of rank n <= m.
        b ((m, ) ndarray): A vector of length m.

    Returns:
        x ((n, ) ndarray): The solution to the normal equations.
    """
    Q, R = la.qr(A, mode='economic')
    x=la.solve_triangular(R,np.matmul(np.transpose(Q), b))
    return x
    

# Problem 2
def line_fit():
    """Find the least squares line that relates the year to the housing price
    index for the data in housing.npy. Plot both the data points and the least
    squares line.
    """
    data=np.load('housing.npy')
    x=np.zeros((33,1))
    y=np.zeros((33,1))
    for row in range(len(data)):
        xval, yval=np.split(data[row],2)
        x[row]=xval
        y[row]=yval
    plt.scatter(x,y)
    A=np.hstack((x,np.ones((len(data[:,0]),1))))
    b=y
    x_hat=least_squares(A, b)
    plt.plot(x, x_hat[0]*x+x_hat[1])
    plt.show()
    
# Problem 3
def polynomial_fit():
    """Find the least squares polynomials of degree 3, 6, 9, and 12 that relate
    the year to the housing price index for the data in housing.npy. Plot both
    the data points and the least squares polynomials in individual subplots.
    """
    plt.figure()
    data=np.load('housing.npy')
    x=np.zeros((33,1))
    y=np.zeros((33,1))
    for row in range(len(data)):
        xval, yval=np.split(data[row],2)
        x[row]=xval
        y[row]=yval
    plt.scatter(x,y)
    ones=np.ones((len(data[:,0]),1))
    b=y
    #Deg 3
    A3=np.hstack((x**3,x**2,x,ones))
    x3=la.lstsq(A3, b)[0]
    print(A3)
    print(x3)
    plt.plot(x, x3[0]*x**3+x3[1]*x**2+x3[2]*x+x3[3])
    #Deg 6
    A6=np.hstack((x**6,x**5,x**4,x**3,x**2,x,ones))
    x6=la.lstsq(A6, b)[0]
    plt.plot(x, x6[0]*x**6+x6[1]*x**5+x6[2]*x**4+x6[3]*x**3+x6[4]*x**2+x6[5]*x+x6[6])
    # #Deg 9
    A9=np.hstack((x**9,x**8,x**7,x**6,x**5,x**4,x**3,x**2,x,ones))
    x9=la.lstsq(A9, b)[0]
    plt.plot(x, x9[0]*x**9+x9[1]*x**8+x9[2]*x**7+x9[3]*x**6+x9[4]*x**5+x9[5]*x**4+x9[6]*x**3+x9[7]*x**2+x9[8]*x+x9[9])



# def plot_ellipse(a, b, c, d, e):
#     """Plot an ellipse of the form ax^2 + bx + cxy + dy + ey^2 = 1."""
#     theta = np.linspace(0, 2*np.pi, 200)
#     cos_t, sin_t = np.cos(theta), np.sin(theta)
#     A = a*(cos_t**2) + c*cos_t*sin_t + e*(sin_t**2)
#     B = b*cos_t + d*sin_t
#     r = (-B + np.sqrt(B**2 + 4*A)) / (2*A)

#     plt.plot(r*cos_t, r*sin_t)
#     plt.gca().set_aspect("equal", "datalim")

# # Problem 4
# def ellipse_fit():
#     """Calculate the parameters for the ellipse that best fits the data in
#     ellipse.npy. Plot the original data points and the ellipse together, using
#     plot_ellipse() to plot the ellipse.
#     """
#     raise NotImplementedError("Problem 4 Incomplete")


# # Problem 5
# def power_method(A, N=20, tol=1e-12):
#     """Compute the dominant eigenvalue of A and a corresponding eigenvector
#     via the power method.

#     Parameters:
#         A ((n,n) ndarray): A square matrix.
#         N (int): The maximum number of iterations.
#         tol (float): The stopping tolerance.

#     Returns:
#         (float): The dominant eigenvalue of A.
#         ((n,) ndarray): An eigenvector corresponding to the dominant
#             eigenvalue of A.
#     """
#     raise NotImplementedError("Problem 5 Incomplete")


# # Problem 6
# def qr_algorithm(A, N=50, tol=1e-12):
#     """Compute the eigenvalues of A via the QR algorithm.

#     Parameters:
#         A ((n,n) ndarray): A square matrix.
#         N (int): The number of iterations to run the QR algorithm.
#         tol (float): The threshold value for determining if a diagonal S_i
#             block is 1x1 or 2x2.

#     Returns:
#         ((n,) ndarray): The eigenvalues of A.
#     """
#     raise NotImplementedError("Problem 6 Incomplete")

if __name__ == "__main__":
    print(least_squares(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),np.array([[1], [2], [3]])))
    line_fit()
    polynomial_fit()