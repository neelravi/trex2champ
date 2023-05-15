from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='trex2champ',
    version='2.1.8',
    packages=['./'],
    install_requires=[
        'trexio>=1.3.2',
        'resultsFile>=2.4',
    ],
    entry_points={
        'console_scripts': [
            'trex2champ=trex2champ:main',
        ],
    },
    author='Ravindra Shinde',
    author_email='r.l.shinde@utwente.nl',
    description='A package to convert trexio files into various text input files for CHAMP code.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords='trexio quantum monte carlo champ converter',
    url='https://github.com/neelravi/trex2champ',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Operating System :: OS Independent',
        'Topic :: Scientific/Engineering',
        'Topic :: System :: Distributed Computing',
        'Topic :: Database :: Database Engines/Servers',
    ],
)
