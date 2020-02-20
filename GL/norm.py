import numpy as np

def norm(array):
    return (array - array.min())/ (array.max()-array.min())
