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