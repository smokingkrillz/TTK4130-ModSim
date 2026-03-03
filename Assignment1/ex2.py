import numpy as np
import matplotlib.pyplot as plt
import ex1

def analytical_function(t, x_0, v_0, params):

    undamped_natural_f = np.sqrt(params["k"] / params["m"])

    damping_ratio = params["c"] / (2 * np.sqrt(params["k"] * params["m"]))

    #underdamped case
    if damping_ratio >= 0 and damping_ratio < 1:
        natural_damped_f = undamped_natural_f * np.sqrt(1 - damping_ratio**2)

        a = x_0 * np.cos(natural_damped_f * t)
        b = (
            v_0
            + damping_ratio * undamped_natural_f * x_0 * np.sin(
                natural_damped_f * t)
        ) / natural_damped_f

        return (np.e) ** (-damping_ratio * undamped_natural_f * t) * (a + b)

    #critically damped case
    if damping_ratio == 1 or round(damping_ratio, 5) == 1:
        return (x_0 + (v_0 + undamped_natural_f * x_0) * t) * (np.e) ** (
            -undamped_natural_f * t
        )
    
    #overdamped case
    if  damping_ratio > 1:
        r_1 = -damping_ratio * undamped_natural_f + undamped_natural_f*np.sqrt(damping_ratio**2 -1)
        r_2 = -damping_ratio * undamped_natural_f - undamped_natural_f*np.sqrt(damping_ratio**2 -1)

        c1 = (v_0 - (r_2 * x_0)) / (r_1 - r_2)
        c2 = x_0 - c1

        return c1 * np.exp(r_1 * t) + c2 * np.exp(r_2 * t)


params = {"k": 5.0, "m": 1, "c": 0.0}

dt = 0.01
t_start = 0
t_end = 10

t = np.arange(t_start, t_end + dt, dt)

# position
s = np.zeros([len(t)])

s[0] = 1

y_1 = ex1.run_sim()

for i in range(len(t) -1):
    s[i] = analytical_function(t[i], 1, 0, params)
    
plt.figure()
plt.plot(t, s)
plt.plot(t, y_1, label="Position x1")
plt.xlabel("time")
plt.ylabel("position")
plt.legend()
plt.show()