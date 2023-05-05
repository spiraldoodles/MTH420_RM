# python_intro.py
"""Python Essentials: Introduction to Python.
<Name> Rebecca Munk
<Class> MTH 338
<Date> 4/7/23
"""


# Problem 1 (write code below)
if __name__ == "__main__":
    print("Hello, world!") 

# Problem 2
def sphere_volume(r):
    """ Return the volume of the sphere of radius 'r'.
    Use 3.14159 for pi in your computation.
    """
    pi =  3.14159
    return pi*r**2
if __name__ == "__main__":
    print(str(sphere_volume(2)))



# Problem 3
def isolate(a, b, c, d, e):
    """ Print the arguments separated by spaces, but print 5 spaces on either
    side of b.
    """
    print(a,b,c, sep="     ", end=" ")
    print(d,e)
if __name__ == "__main__":
     print(isolate(1, 2, 3, 4, 5))



# Problem 4
def first_half(my_string):
    """ Return the first half of the string 'my_string'. Exclude the
    middle character if there are an odd number of characters.
    """
    if len(my_string)/2==0:
        return my_string[:int(len(my_string)/2)+1]
    else:
        return my_string[:int((len(my_string)-1)/2)+1]
        
def backward(my_string):
    """ Return the reverse of the string 'my_string'.
    """
    return my_string[-1::-1]
    
if __name__ == "__main__":
    print(first_half("yuck"))
    print(first_half("yyuck"))
    print(backward("yuck"))

# Problem 5
def list_ops():
    """ Define a list with the entries "bear", "ant", "cat", and "dog".
    Perform the following operations on the list:
        - Append "eagle".
        - Replace the entry at index 2 with "fox".
        - Remove (or pop) the entry at index 1.
        - Sort the list in reverse alphabetical order.
        - Replace "eagle" with "hawk".
        - Add the string "hunter" to the last entry in the list.
    Return the resulting list.
    """
    list = ["bear", "ant", "cat", "dog"]
    list.append("eagle")
    list[2]="fox"
    list.remove(list[1])
    list.sort(reverse=True)
    list[list.index("eagle")]="hawk"
    list[-1]=list[-1]+"hunter"
    return list
if __name__ == "__main__":
    print(list_ops())



# Problem 6
def pig_latin(word):
    """ Translate the string 'word' into Pig Latin, and return the new word.

    Examples:
        >>> pig_latin("apple")
        'applehay'
        >>> pig_latin("banana")
        'ananabay'
    """
    if word[0] in ("a", "e", "i", "o", "u"):
        return word+"hay"
    else:
        return word[1:]+word[0]+"ay"
if __name__ == "__main__":
    print(pig_latin("abe"))
    print(pig_latin("lincoln"))

# Problem 7
def palindrome():
    """ Find and retun the largest palindromic number made from the product
    of two 3-digit numbers.
    """
    pal=0
    for i, j in zip(range(0,1000, 1), range(0, 1000, 1)):
        if i*j>pal:
            if str(i*j)==str(i*j)[-1::-1]:
                pal=i*j
    return pal
if __name__ == "__main__":
    print(palindrome())

# Problem 8
def alt_harmonic(n):
    """ Return the partial sum of the first n terms of the alternating
    harmonic series, which approximates ln(2).
    """
    list= [float((-1)**(i+1)/i) for i in range(1,n)]
    total =sum(list)
    return total
if __name__ == "__main__":
    print(alt_harmonic(100))

