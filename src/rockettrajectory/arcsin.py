import numpy as np

def arcsin(x):
    """Computes the inverse sine of x on the range [-pi/2 to pi/2]

    inputs
    float phi

    returns
    float
        a radian as a float.

    """
    for n in range (10):
        n+=1
        top=(2*x)**(2*n)
        bot=(n**2)*(np.math.factorial(2*n)/((np.math.factorial(n))**2))
        arcsin_sqrt=arcsin_sqrt+.5*top/bot
    arcsin=np.sqrt(arcsin_sqrt)
    return arcsin

