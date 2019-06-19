# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 09:55:28 2019

@author: Shreya.Chatterjee
"""

"""
Process utilities

"""
import numpy as np

def smooth_curve(curve, length):
    """
    Smooth a curve with boxcar of length 11 elements
    """
    boxcar = np.ones(length)/ length
    return np.convolve(np.ones(11)/11, curve, mode='same')