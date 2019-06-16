from __future__ import absolute_import, division, print_function
from os.path import join as pjoin

# Format expected by setup.py and doc/source/conf.py: string of form "X.Y.Z"
_version_major = 0
_version_minor = 1
_version_micro = ''  # use '' for first of series, number for 1 and above
_version_extra = 'dev'
# _version_extra = ''  # Uncomment this for full releases

# Construct full version string from these.
_ver = [_version_major, _version_minor]
if _version_micro:
    _ver.append(_version_micro)
if _version_extra:
    _ver.append(_version_extra)

__version__ = '.'.join(map(str, _ver))

CLASSIFIERS = ["Development Status :: 3 - Alpha",
               "Environment :: Console",
               "License :: OSI Approved :: MIT License",
               "Operating System :: OS Independent",
               "Programming Language :: Python"]

# Description should be a one-liner:
description = "A Discord bot for Urist McStation's community."
# Long description will go up on the pypi page
long_description = """

Urist McBot
========
TBD

License
=======
TBD

"""

NAME = "Urist McBot"
MAINTAINER = "Jan Malek"
MAINTAINER_EMAIL = "jan.k.malek@gmail.com"
DESCRIPTION = description
LONG_DESCRIPTION = long_description
URL = "http://github.com/uwescience/shablona"
DOWNLOAD_URL = ""
LICENSE = "GPLv3"
AUTHOR = "Jan Malek"
AUTHOR_EMAIL = "jan.k.malek@gmail.com"
PLATFORMS = "OS Independent"
MAJOR = _version_major
MINOR = _version_minor
MICRO = _version_micro
VERSION = __version__
PACKAGE_DATA = {'uristmcbot': [pjoin('data', '*')]}
REQUIRES = ["pytest", "gunicorn", "discord"]
