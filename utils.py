from appliable import *

from random import choice
import random
import matplotlib.pyplot as plt
import numpy as np

def select_random_pic(pics):
    return choice(pics)

def select_random_xoord_on_pic(pic):
    maxX = pic.shape[1]
    maxY = pic.shape[0]
    x = random.randint(0, maxX - 1)
    y = random.randint(0, maxY - 1)
    return x,y

def apply_binary_unit_to_pic(pic, unit):
    ymax = pic.shape[0]
    xmax = pic.shape[1]
    XYs = []

    for y in range(0, ymax):
        for x in range(0, xmax):
            matches = unit.apply(pic, x, y)
            if len(matches) > 0:
                XYs.append([x,y])
    return XYs

def get_hist(values,nbins):
    if not isinstance(values, np.ndarray):
        values = np.array(values)
    (probs, bins, _) = plt.hist(values, bins=nbins,
                                    weights=np.ones_like(values) / len(values), range=(0, 255))

    return probs, bins