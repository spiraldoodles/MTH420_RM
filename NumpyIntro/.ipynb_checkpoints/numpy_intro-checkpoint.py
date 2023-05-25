# numpy_intro.py
"""Python Essentials: Intro to NumPy.
<Name> Rebecca Munk
<Class> MTH 420
<Date> 4/21/23
"""
import numpy as np

def prob1():
    """ Define the matrices A and B as arrays. Return the matrix product AB. """
    A=np.array([[3, -1, 4],[1, 5, -9]])
    B=np.array([[2, 6, -5, 3], [5, -8, 9, 7], [9, -3, -2, -3]])
    return np.dot(A,B)


def prob2():
    """ Define the matrix A as an array. Return the matrix -A^3 + 9A^2 - 15A. """
    A=np.array([[3, 1, 4],[1, 5, 9], [-5, 3, 1]])
    return -1*np.dot(np.dot(A, A), A)+9*np.dot(A, A)-15*A


def prob3():
    """ Define the matrices A and B as arrays using the functions presented in
    this section of the manual (not np.array()). Calculate the matrix product ABA,
    change its data type to np.int64, and return it.
    """
    A=np.ones((7, 7))
    A=np.triu(A)
    Bl=-1*np.ones((7, 7))
    Bu=np.full((7, 7), 5)
    B=np.triu(Bu,1)+np.tril(Bl)
    print(B)
    Prod=np.matmul(np.matmul(A, B), A)
    return np.int64(Prod)
    
    
def prob4(A):
    """ Make a copy of 'A' and use fancy indexing to set all negative entries of
    the copy to 0. Return the resulting array.

    Example:
        >>> A = np.array([-3,-1,3])
        >>> prob4(A)
        array([0, 0, 3])
    """
    B=np.copy(A)
    mask=B<0
    B[mask]=0
    return B
    

def prob5():
    """ Define the matrices A, B, and C as arrays. Use NumPy's stacking functions
    to create and return the block matrix:
                                | 0 A^T I |
                                | A  0  0 |
                                | B  0  C |
    where I is the 3x3 identity matrix and each 0 is a matrix of all zeros
    of the appropriate size.
    """
    A=np.array([[0, 2, 4],[1, 3, 5]])
    # print(A)
    B=np.tril(np.full((3, 3), 3))
    # print(B)
    C=-2*np.identity(3)
    # print(C)
    R1=np.hstack((np.zeros((3, 3)), A.T, np.identity(3)))
    # print(R1)
    R2=np.hstack((A, np.zeros((2, 2)), np.zeros((2, 3))))
    # print(R2)
    R3=np.hstack((B, np.zeros((3, 2)), C))
    # print(R3)
    return np.vstack((R1, R2, R3))


def prob6(A):
    """ Divide each row of 'A' by the row sum and return the resulting array.
    Use array broadcasting and the axis argument instead of a loop.

    Example:
        >>> A = np.array([[1,1,0],[0,1,0],[1,1,1]])
        >>> prob6(A)
        array([[ 0.5       ,  0.5       ,  0.        ],
               [ 0.        ,  1.        ,  0.        ],
               [ 0.33333333,  0.33333333,  0.33333333]])
    """
    sums=A.sum(axis=1)
    sums=np.vstack(sums)
    # print(sums)
    A=A/sums
    return A
    


# def prob7():
#     """ Given the array stored in grid.npy, return the greatest product of four
#     adjacent numbers in the same direction (up, down, left, right, or
#     diagonally) in the grid. Use slicing, as specified in the manual.
#     """
#     raise NotImplementedError("Problem 7 Incomplete")

if __name__ == "__main__":
    print(prob1())
    print(prob2())
    print(prob3())
    print(prob4(np.array([[3, -1, 4],[1, 5, -9]])))
    print(prob5())
    print(prob6(np.array([[1,1,0],[0,1,0],[1,1,1]])))