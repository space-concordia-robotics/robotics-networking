from setuptools import setup, find_packages

import roboticsnet

setup(
    name=roboticsnet.__appname__,
    version=roboticsnet.__version__,

    description='Common network code for Rover',
    long_description=open('README.rst').read(),
    # url='http://www.github.com/psyomn/pypsylbm',
    license='MIT',

    author='Simon Symeonidis, George Gonis',

    packages=['roboticsnet', 'roboticsnet.commands'],
    scripts=['roboticsnet/bin/roboticsnet-test']
)
