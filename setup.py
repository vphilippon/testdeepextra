from setuptools import setup

setup(
    name='testdeepextra',
    version='0.0.1',
    extras_require={
        'foobar': ['requests[security]'],
    },
)
