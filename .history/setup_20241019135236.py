# setup.py
from setuptools import setup, find_packages

setup(
    name='cell_runner',
    version='0.1',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'cell_runner=cell_runner.runner:main',  # Command to run in CLI
        ],
    },author='Your Name',
    author_email='your.email@example.com',
    description='A package to run Jupyter notebook cells from the command line.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/jupyter-cell-runner',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)