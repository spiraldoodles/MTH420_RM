# cvxpy_intro.py
"""Volume 2: Intro to CVXPY.
<Name> Rebecca Munk
<Class> MTH 420
<Date> 5/26/23
"""
import cvxpy as cp
import numpy as np

def prob1():
    """Solve the following convex optimization problem:

    minimize        2x + y + 3z
    subject to      x  + 2y         <= 3
                         y   - 4z   <= 1
                    2x + 10y + 3z   >= 12
                    x               >= 0
                          y         >= 0
                                z   >= 0

    Returns (in order):
        The optimizer x (ndarray)
        The optimal value (float)
    """
    x = cp.Variable(3, nonneg = True)
    c = np.array([2, 1, 3])
    objective = cp.Minimize(c @ x)
    A= np.array([1, 2, 0])
    B= np.array([0, 1, -4])
    C= np.array([2, 10, 3])
    constraints = [A @ x <= 3, B @ x <= 1, C @ x >= 12]
    problem = cp.Problem(objective, constraints)
    ans = problem.solve()
    return x.value, ans


# Problem 2
def l1Min(A, b):
    """Calculate the solution to the optimization problem

        minimize    ||x||_1
        subject to  Ax = b

    Parameters:
        A ((m,n) ndarray)
        b ((m, ) ndarray)

    Returns:
        The optimizer x (ndarray)
        The optimal value (float)
    """
#    x = cp.Variable((len(A[1]),1))
    n = A.shape[1]
    x = cp.Variable(n)

    print(x.shape)
    objective = cp.Minimize(cp.norm(x, 1))
    constraints = [A @ x == b]
    problem = cp.Problem(objective, constraints)
    ans = problem.solve()
    return x.value, ans


# Problem 3
def prob3():
    """Solve the transportation problem by converting the last equality constraint
    into inequality constraints.

    Returns (in order):
        The optimizer x (ndarray)
        The optimal value (float)
    """
    raise NotImplementedError("Problem 3 Incomplete")


# Problem 4
def prob4():
    """Find the minimizer and minimum of

    g(x,y,z) = (3/2)x^2 + 2xy + xz + 2y^2 + 2yz + (3/2)z^2 + 3x + z
    Returns (in order):
        The optimizer x (ndarray)
        The optimal value (float)
    """
    Q = np.array([[3, 1, 1],[1, 2, 1], [1,1,3]])
    r = np.array([3, 0, 1])
    x = cp.Variable(3)
    prob = cp.Problem(cp.Minimize(.5 * cp.quad_form(x, Q) + r.T @ x))
    ans = prob.solve()

    return x.value, ans


# Problem 5
def prob5(A, b):
    """Calculate the solution to the optimization problem
        minimize    ||Ax - b||_2
        subject to  ||x||_1 == 1
                    x >= 0
    Parameters:
        A ((m,n), ndarray)
        b ((m,), ndarray)
        
    Returns (in order):
        The optimizer x (ndarray)
        The optimal value (float)
    """
    n = A.shape[1]
    x = cp.Variable(n, nonneg=True)
#    x = cp.Variable((len(A[1]),1), nonneg = True)
    print(x.shape)
    objective = cp.Minimize(cp.norm(A @ x-b, 2))
    #constraints = [cp.sum(cp.sqrt(cp.square(x))) == 1]
    constraints = [cp.sum(x) == 1]
    problem = cp.Problem(objective, constraints)
    ans = problem.solve()
    return x.value, ans

    

#print(prob1())

#A=np.array([[1,2,1,1],[0,3,-2,-1]])
#b=np.array([[7],[4]])
#print(l1Min(A, b))

#print(prob4())

#print(prob5(A, b))

# # Problem 6
# def prob6():
#     """Solve the college student food problem. Read the data in the file 
#     food.npy to create a convex optimization problem. The first column is 
#     the price, second is the number of servings, and the rest contain
#     nutritional information. Use cvxpy to find the minimizer and primal 
#     objective.
    
#     Returns (in order):
#         The optimizer x (ndarray)
#         The optimal value (float)
#     """	 
#     raise NotImplementedError("Problem 6 Incomplete")
