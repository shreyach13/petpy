# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 09:04:47 2019

@author: Shreya.Chatterjee
"""

from setuptools import setup 




setup(name='petpy',
      version='0.2',
      desription='Petrophysics utilities',
      url = 'https://google.co.in/',
      author='Shreya Hackathon',
      author_email='shreya.chatterjee@shell.com',
      license='Apacha 2',
      packages = ['petpy'],
      install_requries = ['numpy'],
      test_required = ['pytest', 'pytest-cov'],
      entry_points={'console_scripts': ['gardner=petpy.__main__:main']}
      )