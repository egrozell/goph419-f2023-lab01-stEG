import numpy as np

def arcsin(x):
    """Computes the inverse sine of x on the range [-pi/2 to pi/2]

    inputs
    float phi

    returns
    float
        a radian as a float.

    """
    if x==0 :
        return 0
    tol = 0.5e-5
    x = float(x)
    eps_a = 2*tol
    n=1
    fact_n=1
    fact_2n=2
    sum =0.0
    term=0.0
    while eps_a > tol:
        term = ((2*x)**(2*n)) / ((n**2)*((fact_2n)/((fact_n)**2)))
        sum += term
        eps_a = np.abs(term/sum)
        n += 1
        fact_n *= n
        for j in range (2*(n-1),2*n,1):
            fact_2n *= j+1
    arcsin=np.sqrt(0.5*sum)
    return arcsin

