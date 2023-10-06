from rockettrajectory import launch as lnch
import numpy as np
import matplotlib.pyplot as plt

def main ():
    ve_v0 = 2.0
    tol_alpha = 0.04

    range_alpha = np.arange(0,0.450,0.025)

    min_lnch_angles= []
    max_lnch_angles= []
    phi1 =[]
    phi2 =[]

    for alpha in range_alpha:
        x = lnch.launch_angle_range(ve_v0,alpha, tol_alpha)
        max_lnch_angles.append(x[0])
        min_lnch_angles.append(x[1])
        phi1.append(x[2])
        phi2.append(x[3])
    print (f'1 {list(phi1)},2 {list(phi2)}')

    plt.figure(1)
    plt.plot(range_alpha, min_lnch_angles, label = 'minimum launch angles')
    plt.plot(range_alpha, max_lnch_angles, label = 'maximum launch angles')
    plt.legend()
    plt.ylabel("Launch Angle")
    plt.xlabel("Desired Maximum Altitude")
    plt.title("Maximum and Minimum Launch Angles for a Range of Alpha Values")
    plt.savefig("Launch_Alpha_Range")

    #make a range of velocities
    v_range = np.arange(1.22,6.21,0.25)
    #set tolerance and alpha to be held constant
    tol_alpha= 0.04
    alpha = 0.25

    #clear  previously used arrays
    min_lnch_angles1= []
    max_lnch_angles1= []

    # calculate the min and max for the range of velocityes using launch module

    for v in v_range:
        x = lnch.launch_angle_range(v,alpha, tol_alpha)
        max_lnch_angles1.append(x[0])
        min_lnch_angles1.append(x[1])
        phi1.append(x[2])
        phi2.append(x[3])
    print (f'3 {list(max_lnch_angles1)},4 {list(min_lnch_angles1)}')

    plt.figure(2)
    plt.plot(v_range, min_lnch_angles1, label = 'minimum launch angles')
    plt.plot(v_range, max_lnch_angles1, label = 'maximum launch angles')
    plt.legend()
    plt.ylabel("Launch Angle")
    plt.xlabel("Escape Velocity to Terminal Velocity Ratio")
    plt.title("Maximum and Minimum Launch Angles for a Range of Velocity Values")
    plt.savefig("Launch_Velocity_Range")

if __name__ == "__main__":
    main()
