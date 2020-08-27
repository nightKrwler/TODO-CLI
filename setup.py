import codecs
import os
from setuptools import setup, find_packages

def read(*parts):
    return codecs.open(os.path.join(os.path.abspath(os.path.dirname(__file__)), *parts), 'r').read()
setup(
    name='todo',
    version='0.0.1',
    description='Command-line tool to manage Todo lists',
    long_description=read('README.md'),
    author='Srujana B',
    author_email='batchu.srujana@gmail.com',
    url='https://github.com/nightKrwler/TODO-CLI', 
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'todo=todo:main'
        ]
    }

)
