import numpy as np
e = 59.5409
e = 60.5
kappa = e/511
def e_of_theta(theta):
    return e / (1 + kappa*(1-np.cos(theta * np.pi / 180)))

e_of_theta(90)
