from rockettrajectory import launch as lnch
import numpy as np
import matplotlib.pyplot as plt

def main ():
    ve_v0 = 2.0
    tol_alpha = 0.04

    range_alpha = np.arange(0,0.450,0.025)

    min_lnch_angles= []
    max_lnch_angles= []

    for alpha in range_alpha:
        x = lnch.launch_angle_range(ve_v0,alpha, tol_alpha)
        max_lnch_angles.append(x[0])
        min_lnch_angles.append(x[1])

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

    plt.figure(2)
    plt.plot(v_range, min_lnch_angles1, label = 'minimum launch angles')
    plt.plot(v_range, max_lnch_angles1, label = 'maximum launch angles')
    plt.legend()
    plt.ylabel("Launch Angle")
    plt.xlabel("Escape Velocity to Terminal Velocity Ratio")
    plt.title("Maximum and Minimum Launch Angles for a Range of Velocity Values")
    plt.savefig("Launch_Velocity_Range")

    max_q2,min_q2= lnch.launch_angle_range(2,0.25,0.02)

    v_error,alpha_error= lnch.equation_17(2,0.25)
    v_error =abs(v_error)* 0.05
    alpha_error =abs(alpha_error)* 0.02
    alpha_max,amax_angle= lnch.max_altitude_ratio(range_alpha,max_lnch_angles)
    v_max,vmax_angle= lnch.max_velocity_ratio(v_range,max_lnch_angles1)

    print(f'Question 2:   max {max_q2} \n              min {min_q2} \nQuestion 3:max alpha {alpha_max} angle {amax_angle}\nQuestion 4: max velocity {v_max} angle {vmax_angle}\nQuestion 5: Error in ve_v0 {v_error}. Error in alpha {alpha_error}\nUncertanty for fun {lnch.uncertainty(2,0.25,0.05,0.02)}')



if __name__ == "__main__":
    main()
