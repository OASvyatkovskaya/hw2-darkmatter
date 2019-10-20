import numpy as np
from scipy import integrate, math
def f(t, H0, O):  # function mu=
    theoreticaldata = np.empty(len(t))
    integral = lambda x: 1 / math.sqrt((1 - O) * ((1 + x) ** 3) + O)
    for i in range(len(t)):
        theoreticaldata[i] = (
                    5 * np.log10(((3 * 10 ** 11) / H0) * (1 + t[i]) * integrate.quad(integral, 0, t[i])[0]) - 5)
    return theoreticaldata


def j(t, H0, O):  # handmade jacobian
    jac = np.empty((len(t), 2), dtype=float)
    intder = lambda x: 0.5 * ((1 + x) ** 3 - 1) / (np.sqrt((1 - O) * (1 + x) ** 3 + O)) ** 3
    integral = lambda x: 1 / math.sqrt((1 - O) * ((1 + x) ** 3) + O)
    for i in range(len(t)):
        jac[i, 0] = -5 / H0 / np.log(10)
        jac[i, 1] = 5 * integrate.quad(intder, 0, t[i])[0] / integrate.quad(integral, 0, t[i])[0] / np.log(10)
    return jac
