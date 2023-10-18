from setuptools import find_packages
from setuptools import setup

setup(
    name='shared_msgs',
    version='0.0.0',
    packages=find_packages(
        include=('shared_msgs', 'shared_msgs.*')),
)
