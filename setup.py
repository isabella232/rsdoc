from setuptools import setup

setup(
    name='rsdoc',
    version='1.0',
    py_modules=['rsdoc'],
    install_requires=[
        'Click>=6.7',
        'requests>=2.18.1',
        'cookiecutter>=1.5.1',
    ],
    entry_points='''
        [console_scripts]
        rsdoc=rsdoc:cli
    ''',
)
