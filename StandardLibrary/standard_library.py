# standard_library.py
"""Python Essentials: The Standard Library.
<Name> Rebecca Munk
<Class> MTH 338
<Date> 4/7/23
"""
import calculator as cl
from itertools import combinations, chain

# Problem 1
def prob1(L):
    """Return the minimum, maximum, and average of the entries of L
    (in that order, separated by a comma).
    """
    return min(L), max(L), sum(L)/len(L) 

# Problem 2
def prob2():
    """Determine which Python objects are mutable and which are immutable.
    Test integers, strings, lists, tuples, and sets. Print your results.
    """
    #Integer Test
    i=2
    i1=i
    i1+=1
    if i1==i:
        print("Integers are mutable")
    else:
        print("Integers are not mutable")
    
    #String Test
    s="Howdy"
    s1=s
    s1="Howdy!"
    if s1==s:
        print("Strings are mutable")
    else:
        print("Strings are not mutable")
    
    #List Test
    L=[1, 2, 3]
    L1=L
    L1[0]=0
    if L1==L:
        print("Lists are mutable")
    else:
        print("Lists are not mutable")
    
    #Tuple Test
    t= (1, 2)
    t1=t
    t1+=(1,)
    if t1==t:
        print("Tuples are mutable")
    else:
        print("Tuples are not mutable")
    
    
    #Set Test
    st=set((True, "Howdy", 1))
    st1=st
    st1.remove("Howdy")
    if st1==st:
        print("Sets are mutable")
    else:
        print("Sets are not mutable")  



# Problem 3
def hypot(a, b):
    """Calculate and return the length of the hypotenuse of a right triangle.
    Do not use any functions other than sum(), product() and sqrt() that are
    imported from your 'calculator' module.

    Parameters:
        a: the length one of the sides of the triangle.
        b: the length the other non-hypotenuse side of the triangle.
    Returns:
        The length of the triangle's hypotenuse.
    """
    return cl.sqrt(cl.sum(cl.product(a,a), cl.product(b, b)))


# Problem 4
def power_set(A):
    """Use itertools to compute the power set of A.

    Parameters:
        A (iterable): a str, list, set, tuple, or other iterable collection.

    Returns:
        (list(sets)): The power set of A as a list of sets.
    """
    #subsets
    L=[]
    for i in range(1, len(A)):
        ah=chain(combinations(A,i))
        for element in ah:
            element=set(element)
            L.append(element)
        
    L.append(A)
    L.append(set(A))
    return L


# Problem 5: Implement shut the box.
def shut_the_box(player, timelimit):
    """Play a single game of shut the box."""
    raise NotImplementedError("Problem 5 Incomplete")

if __name__ == "__main__":
    print(prob1([1,2,3,4]))
    prob2()
    print(hypot(3, 4))
    print(power_set({1,2,3,4}))