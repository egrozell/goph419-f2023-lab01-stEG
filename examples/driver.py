from rockettrajectory import launch as lnch

def main ():
    ve_v0=2
    alpha=0.25
    tol_alpha= 0.02
    test = lnch.launch_angle(ve_v0,alpha)
    print("test launch",test)

if __name__ == "__main__":
    main()
