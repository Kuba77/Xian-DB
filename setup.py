from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='xiandb',
    version='0.2.0',

    description='A database model for Xian',
    long_description=long_description,


    url='https://github.com/Kuba77/Xian-DB',

    author='Jakub Chronowski',
    author_email='jakub@chronow.ski',

    license='MIT',


    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: XIAN Collaborators',
        'Topic :: Software Development :: Database',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 2.7'
    ],

    keywords='xian database db',
    packages=['xiandb', 'xiandb.models'],

    install_requires=['mongokat', 'pyyaml', 'bcrypt'],
    extras_require={}
)
