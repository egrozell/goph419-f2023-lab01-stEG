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
        if sin_phi <= 1:
            max_angle=arc.arcsin(sin_phi)
            if max_angle>np.pi/2 or max_angle<0:
                max_angle=None
        else:
            max_angle=None

    else:
        max_angle = None
        sin_phi1=0
    temp=1 - ((max_alpha/(1+max_alpha))*ve_v0**2)
    if temp>0:
        sin_phi=(1+max_alpha)*np.sqrt(temp)
        if sin_phi <=1:
            min_angle=arc.arcsin(sin_phi)
            if min_angle>np.pi/2 or min_angle<0:
                min_angle = None
        else:
            min_angle=None
    else:
        min_angle=None
        sin_phi2=0
    return max_angle, min_angle

def equation_17(ve_v0,alpha):
    """gives the partial dirivatives for equation 17
    input float ve_v0 and alpha
    output partial derivative with respect to both
    pv palpha
    """
    pv= (-alpha*ve_v0)/(np.sqrt(1-((alpha*ve_v0)/(alpha+1))))

    palpha = (2-ve_v0**2 - 2*alpha*(-1+ve_v0**2))/(2*(1+alpha)*np.sqrt(((1+alpha)-alpha*ve_v0**2)/(1+alpha)))
    return pv, palpha

def uncertainty(ve_v0,alpha,delta_ve_v0,delta_alpha):
    """computes the error in sin_phi and the condition number
    input floats ve_v0,alpha,delta_ve_v0,delta_alpha
    outputs
    """
    pv,palpha = equation_17(ve_v0,alpha)
    delta_sin_phi=abs(palpha)*delta_alpha+abs(pv)*delta_ve_v0

    norm=np.sqrt(ve_v0**2+alpha**2)
    jacob=np.sqrt(palpha**2+pv**2)
    condition_number=(norm*jacob)/launch_angle(ve_v0, alpha)
    return condition_number

def min_altitude_ratio(alpha,angle):
    index = [i for i, value in enumerate(angle) if value == None]
    for j in range(len(index)):
        x = index[j]
        np.put(alpha,x,1000)
    xi=np.argmin(alpha)
    x=alpha[xi]
    angle1 = angle[xi]
    return x,angle1

def max_altitude_ratio(alpha,angle):
    index = [i for i, value in enumerate(angle) if value == None]
    for j in range(len(index)):
        x = index[j]
        np.put(alpha,x,-1)
    xi=np.argmax(alpha)
    x=alpha[xi]
    angle1 = angle[xi]
    return x,angle1

def min_velocity_ratio(v,angle):
    """Computes minimum possible velocity ratio for a given target peak altitude.
    """
    index = [i for i, value in enumerate(angle) if value == None]
    for j in range(len(index)):
        x = index[j]
        np.put(v,x,1000)
    xi=np.argmin(v)
    x=v[xi]
    angle1 = angle[xi]
    return x,angle1

def max_velocity_ratio(v,angle):
    """Computes minimum possible velocity ratio for a given target peak altitude.
    """
    index = [i for i, value in enumerate(angle) if value == None]
    for j in range(len(index)):
        x = index[j]
        np.put(v,x,-1)
    xi=np.argmax(v)
    x=v[xi]
    angle1 = angle[xi]
    return x,angle1
