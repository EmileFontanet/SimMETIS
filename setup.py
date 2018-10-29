#!/usr/bin/env python3
"""
SimMETIS: A python package to simulate METIS, based on SimCADO
"""

from datetime import datetime
from distutils.core import setup

# Version number
MAJOR = 0
MINOR = 1
ATTR = ''
VERSION = '%d.%d%s' % (MAJOR, MINOR, ATTR)


def write_version_py(filename='simmetis/version.py'):
    '''Write a file version.py'''
    cnt = """
# THIS FILE GENERATED BY SIMMETIS SETUP.PY
version = '{}'
date    = '{}'
"""
    timestamp = datetime.utcnow().strftime('%Y-%m-%d %T GMT')
    with open(filename, 'w') as fd:
        fd.write(cnt.format(VERSION, timestamp))


def setup_package():
    # Rewrite the version file every time
    write_version_py()

    setup(name = 'SimMETIS',
          version = VERSION,
          description = "METIS Instrument simulator",
          author = "Kieran Leschinski, Oliver Czoske, Leonard Burtscher, Roy van Boekel",
          author_email = """kieran.leschinski@unive.ac.at,
                            oliver.czoske@univie.ac.at,
                            burtscher@strw.leidenuniv.nl
                            boekel@mpia.de""",
          url = "http://metis.strw.leidenuniv.nl/wiki/doku.php?id=sim:simulator",
          packages=['simmetis'],
          package_data = {'simmetis': ['data/*']}
          )


if __name__ == '__main__':
    setup_package()
