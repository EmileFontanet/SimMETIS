#!/usr/bin/env python3
"""
SimMETIS: A python package to simulate METIS, based on SimCADO
"""

## BEFORE importing distutils, remove MANIFEST. distutils doesn't properly
## update it when the contents of directories change.

#import os
#if os.path.exists('MANIFEST'):
#    os.remove('MANIFEST')

# setuptools to allow 'python setup.py develop'. Not necessary for user.
try:
    from setuptools import setup
except ImportError:
    pass

from datetime import datetime

def get_old_version(filename='simcado/version.py'):
    '''Get previous version for auto-update'''
    with open(filename, "r") as f:
        for i in range(3):
            vers = f.readline()
    print(vers)
    vers = vers.replace("dev", "").replace("'","").split(".")[-1]
    return int(float(vers))



# Is this the version number scheme that we want?
MAJOR = 0
MINOR = 4
ATTR = 'dev-METIS'
VERSION = '%d.%d%s' % (MAJOR, MINOR, ATTR)

## This updates TINY every time setup.py is run - doesn't work if
## used by more than one user
#TINY = get_old_version() + 1
#VERSION = '%d.%d.%d%s' % (MAJOR, MINOR, TINY, ATTR)




## Is this needed?
def write_version_py(filename='simcado/version.py'):
    cnt = """
# THIS FILE GENERATED BY SIMCADO SETUP.PY
version = '{}'
date    = '{}'
"""
    timestamp = datetime.utcnow().strftime('%Y-%m-%d %T GMT')
    with open(filename, 'w') as fd:
        fd.write(cnt.format(VERSION, timestamp))

from distutils.core import setup

def setup_package():
    # Rewrite the version file every time
    write_version_py()

    setup(name = 'SimCADO',
          version = VERSION,
          description = "MICADO Instrument simulator",
          author = "Kieran Leschinski, Oliver Czoske",
          author_email = """kieran.leschinski@unive.ac.at,
                            oliver.czoske@univie.ac.at""",
          url = "http://homepage.univie.ac.at/kieran.leschinski/",
          package_dir={'simcado': 'simcado'},
          packages=['simcado', 'simcado.tests', 'simcado.sandbox'],
          # for some reason include_package_data can be temperamental
          #include_package_data=True,
          package_data = {'simcado': ['data/*']},
          )


if __name__ == '__main__':
    setup_package()