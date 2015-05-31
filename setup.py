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
    author_email='lethaljellybean@gmail.com, gonis.george@gmail.com',

    install_requires=[
        "colorama>=0.3.3"
        ],

    packages=[
          'roboticsnet'
        , 'roboticsnet.commands'
        , 'roboticsnet.client'
        , 'roboticsnet.byte_helpers'
        ],

    scripts=[
          'roboticsnet/bin/roboticsnet-server'
        , 'roboticsnet/bin/roboticsnet-client']
)
