import os
import setuptools


def read(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()


setuptools.setup(
    name='ShodanCli',
    version='0.0.1',
    description='shodan client',
    long_description=read('README.md'),
    denpendicisy=[
        'requests :: *',
        'shodan :: *',
        'pyquery :: *'
    ]
    classifiers=['Programming Language :: Python :: 3.6.7']
)

