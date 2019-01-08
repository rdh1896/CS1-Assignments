"""
Quadratic Root Calculator
Name: Russell Harvey
File: hw02
"""

import math 


def quadratic_roots(a,b,c):
    """
    Calculates the roots of a given quadratic equation (ax^2+bx+c),
    then returns the values of the root(s) to the console.
    """

    d = (b**2) - (4*a*c) # Calculating the discriminant
    if(a == 0 and b == 0):
        """
        If plugged into the following elif statements, the equation
        0x^2+0x+c = 0 (c can be any real number including negatives and 0)
        will return a error to the console. To mitigate this, 
        before running the following logic the function checks for
        the above equation and prints to the console...
        'Quadratic Equation: 0x^2+0x+0 = 0
         All real numbers are roots of the equation'
        """
        print("Quadratic Equation: 0x^2+0x+",c,"= 0",sep="")
        print("All real numbers are roots of the equation")
    elif(d > 0):
        """
        Cases when d is greater than 0 will result in two roots, requiring
        two variables to store each root.
        """
        ans1 = (-b + math.sqrt(d))/(2*a) # Solves for the roots of equation, uses quadratic formula.
        ans2 = (-b - math.sqrt(d))/(2*a) # Does the same as above, but the negative version.
        """
        The following print statements will show as follows.
        'Quadratic Equation: ax^2+bx+c = 0
         Two roots.
         x = ans1
         x = ans2' 
        """
        print("Quadratic Equation: ",a,"x^2+",b,"x+",c,"= 0",sep="")
        print("Two roots.")
        print("x = " + str(ans1))
        print("x = " + str(ans2))
    elif(d == 0):
        """
        If the discriminant is equal to zero, only one root will exist.
        No need to add and subtract because d is 0 and will result in the
        same root either way.
        """
        ans1 = (-b + math.sqrt(d))/(2*a) 
        """
        The following print statments will show as follows
        'Quadratic Equation: ax^2+bx+c = 0
         One root
         x = ans1'
        """
        print("Quadratic Equation: ",a,"x^2+",b, "x+",c,"= 0",sep="")
        print("One root.")
        print("x = " + str(ans1))
    else:
        """
        The quadratic will have no roots if the discriminant is less than 0.
        This else statement is for these scenarios. You can't take the square root
        of a negative number unless we involved imaginaries.
        The print statements will show as follows
        'Quadratic Equation: ax^2+bx+c = 0
         No roots.'
        """
        print("Quadratic Equation: ",a,"x^2+",b,"x+",c,"= 0",sep="")
        print("No roots.")

quadratic_roots(1,5,4) 
quadratic_roots(4,-2,8)
quadratic_roots(6.5,7.2,8.9)
quadratic_roots(-4,-8,-3)
quadratic_roots(-3,-4.5,9)
quadratic_roots(0,0,0)
quadratic_roots(4,8,4)
quadratic_roots(0,0,7)
quadratic_roots(3.141592,2.718281,1.618033) # a = pi, b = e, c = golden ratio... obiviously truncated to 6 decimal places cause why not, turns out no roots.
quadratic_roots(math.sqrt(3),math.sqrt(6),math.log(11))
quadratic_roots(-5,-26,100)
quadratic_roots(3,6,3)
