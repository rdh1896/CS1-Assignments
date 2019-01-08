import math


def quadratic_roots(a,b,c):
    d = (b**2) - (4*a*c)
    if(d > 0):
        ans1 = (-b + math.sqrt(d))/(2*a)
        ans2 = (-b - math.sqrt(d))/(2*a)
        print("Two roots.")
        print("x = " + str(ans1))
        print("x = " + str(ans2))
    elif(d == 0):
        ans1 = (-b + math.sqrt(d))/(2*a)
        print("One root.")
        print("x = " + str(ans1))
    else:
        print("No roots.")

quadratic_roots(1,5,4)
quadratic_roots(2,-11,-21)
quadratic_roots(4,1,4)