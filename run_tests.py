# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 11:51:11 2019

@author: Shreya.Chatterjee
"""

import pytest
import sys,os

#sys.path.append(os.getcwd())
pytest.main(["--cov","petpy"])

#pytest -mpl