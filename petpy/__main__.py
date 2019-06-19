# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 13:02:54 2019

@author: Shreya.Chatterjee
"""
import sys
from petpy import gardner


def main():
    vp = float(sys.argv[1])
    print(gardner(vp))
    return 

if __name__ == '__main__':
    main()