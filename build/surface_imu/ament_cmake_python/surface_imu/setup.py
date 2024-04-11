from setuptools import find_packages
from setuptools import setup

setup(
    name='surface_imu',
    version='0.0.0',
    packages=find_packages(
        include=('surface_imu', 'surface_imu.*')),
)
