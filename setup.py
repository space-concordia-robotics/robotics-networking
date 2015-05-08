from setuptools import setup, find_packages

import roboticsnet

setup(
    name='roboticsnet',
    version=roboticsnet.__version__,

    description='',
    long_description=open('README.rst').read(),
    # url='http://www.github.com/psyomn/pypsylbm',
    license='MIT',

    author='TBD',

    packages=['roboticsnet'],
    zip_safe=False,
    scripts=['roboticsnet/bin/roboticsnet-test']
)
