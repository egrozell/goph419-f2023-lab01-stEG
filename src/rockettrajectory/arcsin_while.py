import numpy as np

def arcsin(x):
    """Computes the inverse sine of x on the range [-pi/2 to pi/2]

    inputs
    float phi

    returns
    float
        a radian as a float.

    """
    tol = 1.0e-16
    x = float(x)
    eps_a = 1
    n=1
    fact_n=1
    fact_2n=1
    sum =0.0
    arcsin_sqrt=0
    while eps_a > tol:
        term=(2*x)**(2*n)/(n**2)*((fact_2n)/(fact_n**2))
     #  print (f"n {n} fact_2n {fact_2n} fact_n {fact_2n}")
        sum += term
        eps_a = np.abs(arcsin_sqrt/sum)
        n += 1
        fact_n *= n
        for j in range (2*(n-1),2*n,1):
            fact_2n *= j+1
    arcsin=np.sqrt(0.5*sum)
    return arcsin

