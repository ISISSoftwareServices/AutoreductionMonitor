# pylint:skip-file
"""
Wrapper for the functionality for various installation and project setup commands
see:
    `python setup.py help`
for more details
"""

from setuptools import setup

import platform

# Place Setup requirements in here
setup_requires = []

if platform.system() == 'Windows':
    setup_requires.append('pypiwin32')
else:
    setup_requires.append('python-daemon')

setup(name='AutoReduction_System_Monitoring',
      version='1.0',
      description='ISIS AutoReduction System Monitoring Tools',
      author='ISIS Autoreduction Team',
      url='https://github.com/ISISSoftwareServices/AutoreductionMonitor/',
      install_requires=setup_requires
      )
