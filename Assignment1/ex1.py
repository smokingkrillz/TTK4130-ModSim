import numpy as np
import matplotlib.pyplot as plt
#               x0, c, k
coefficients = [1, 0.0, 5.0]


def u_dot(t, y, coefficients):
    y1, y2 = y
    dudt_1 = y2
    #dudt_2 = (-coefficients[0] * y2 - coefficients[1]) / coefficients[2]
    dudt_2 = - ((coefficients[2] * y1) - (coefficients[1] * y2)) / coefficients[0]
    return [dudt_1, dudt_2]

def run_sim():
    dt = 0.01
    t_start = 0
    t_end = 10

    t = np.arange(t_start, t_end + dt, dt)


    # position
    y_1 = np.zeros([len(t)])

    # velocity
    y_2 = np.zeros([len(t)])

    y_1[0] = 1


    for i in range(len(t) - 1):
        y = [y_1[i], y_2[i]]
        derivatives = u_dot(t, y, coefficients)
        print("derivatives", derivatives)
        y_1[i+1] = y_1[i] + derivatives[0]* dt
        y_2[i+1] = y_2[i] + derivatives[1]* dt
    
    #return y_1, y_2, t
    return y_1

"""
y_1, y_2, t = run_sim()    
plt.figure()
plt.plot(t, y_1, label="Position x1")
plt.plot(t, y_2, label="Velocity x2")
plt.xlabel("Time [s]")
plt.ylabel("State")
plt.legend()
plt.show()
    """
