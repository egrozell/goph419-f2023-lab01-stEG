import numpy as np
from rockettrajectory import arcsin_while as arc

def launch_angle(ve_v0, alpha):
    """launch angle from vertical given velocity ratio and target altitude ratio

    inputs
    float velocity ratio and alpha

    returns
    float phi in radians
    """
    alpha1= 1+alpha
    sqrt = np.sqrt(1-(alpha/alpha1)*(ve_v0**2))
    phi0 =arc.arcsin((alpha1)*sqrt)
    return phi0

def launch_angle_range(ve_v0, alpha, tol_alpha):
    """Calculate the range of launch angles for a given velocity ration, target altitude ration, and tolerance
    inputs
    float ve_v0, alpha, tol_alpha

    returns max_angle, min_angle
    """
    min_alpha = (1 - tol_alpha)*alpha
    max_alpha = (1 + tol_alpha)*alpha
    temp=1 - ((min_alpha/(1+min_alpha))*ve_v0**2)
    if temp>0:
        sin_phi=(1+min_alpha)*np.sqrt(temp)
        sin_phi1=sin_phi
        max_angle=arc.arcsin(sin_phi)
        if max_angle>np.pi/2 or max_angle<0:
            max_angle=None
    else:
        max_angle = None
        sin_phi1=0
    temp=1 - ((max_alpha/(1+max_alpha))*ve_v0**2)
    if temp>0:
        sin_phi=(1+max_alpha)*np.sqrt(temp)
        sin_phi2=sin_phi
        min_angle=arc.arcsin(sin_phi)
        if min_angle>np.pi/2 or min_angle<0:
            min_angle = None
    else:
        min_angle=None
        sin_phi2=0
    return max_angle, min_angle, sin_phi1, sin_phi2

def min_altitude_ratio(ve_v0):
    pass

def max_altitude_ratio(ve_v0):
    pass

def min_velocity_ratio(alpha):
    """Computes minimum possible velocity ratio for a given target peak altitude.
    """
    pass

def min_velocity_ratio(alpha):
    """Computes minimum possible velocity ratio for a given target peak altitude.
    """
    pass
