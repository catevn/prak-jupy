import numpy as np
from scipy.constants import physical_constants
r = physical_constants['classical electron radius'][0]

kappa = 60.5/511
def mu(theta):
    return np.cos(theta * np.pi / 180)
def kleinnishina(theta):
    return r**2/2 * (1/(1+ kappa*(1-mu(theta))))**2 * (kappa*(1-mu(theta)) + (1/(1+ kappa*(1-mu(theta)))) + mu(theta)**2)
