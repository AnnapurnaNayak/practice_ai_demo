from setuptools import setup

setup(
    name='pdf-generator',
    version='0.1',
    install_requires=[
        'Flask',
        'fpdf'
    ],
    py_modules=['main'],
    entry_points={
        'console_scripts': [
            'pdf-generator = main:main',
        ],
    },
)
