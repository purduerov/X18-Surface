from setuptools import find_packages
from setuptools import setup

setup(
    name='depth_comm',
    version='0.0.0',
    packages=find_packages(
        include=('depth_comm', 'depth_comm.*')),
)
