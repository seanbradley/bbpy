'''
Created on Dec 1, 2010

@author: cdg2
'''
from setuptools import setup, find_packages
setup(
      name = "BbPy",
      version = "1.0.2640",
      packages = find_packages("src/"),
      install_requires = ['ZSI'],
      setup_requires = ['ZSI'],
      package_dir = {
                     'BbPy':'src/BbPy',
					 'VO':'src/BbPy/VO',
					 'security':'src/BbPy/security',
					 'bbwsdl':'src/BbPy/bbwsdl'
                     },
      package_data = {
                      '':['*.pl','*.txt']
                      },
      author = "Chris Greenough",
      author_email = "chris.greenough@nau.edu",
      description = "This is a wrapper for the Blackboard Learn Web Services",
      license = "GPL",
      keywords = "Blackboard Learn WebService ZSI",
      url = "http://www.nau.edu/"
      )
