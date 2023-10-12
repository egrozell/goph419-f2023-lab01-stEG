from rockettrajectory import launch as lnch

def main ():
    ve_v0=2
    alpha=0.25
    tol_alpha= 0.02
    expected = 0.5931997761496287
    test = lnch.launch_angle(ve_v0,alpha)
    print(f'expected {expected}\ntested   {test}\npass {test==expected}')

if __name__ == "__main__":
    main()
