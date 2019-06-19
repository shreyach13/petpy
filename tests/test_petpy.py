# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 11:09:28 2019

@author: Shreya.Chatterjee
"""
from petpy import gardner

#EPSILON = 1e-6
import numpy as np

def test_gardner():
    rhob = gardner(2000) #2073
    #assert abs(rhob - 2073.0949454 ) < EPSILON
    assert np.testing.assert_allclose(rhob, 2073.0949454)
    