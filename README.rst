SpiceyPy
========

+------------------------------------------------+---------------------+--------------------------+-------------------+------------+
| Continuous Integration                         | Code Coverage       | Docs                     | Chat              | Citation   |
+================================================+=====================+==========================+===================+============+
| |Travis Build Status| |Windows Build Status|   | |Coverage Status|   | |Documentation Status|   | |Join the chat|   | |Citation| |
+------------------------------------------------+---------------------+--------------------------+-------------------+------------+

.. |Travis Build Status| image:: https://travis-ci.org/AndrewAnnex/SpiceyPy.svg?style=flat?branch=master
   :target: https://travis-ci.org/AndrewAnnex/SpiceyPy
.. |Windows Build Status| image:: https://ci.appveyor.com/api/projects/status/wly0q2cwy33ffura/branch/master?svg=true
   :target: https://ci.appveyor.com/project/AndrewAnnex/spiceypy/
.. |Coverage Status| image:: https://coveralls.io/repos/github/AndrewAnnex/SpiceyPy/badge.svg?branch=master
   :target: https://coveralls.io/github/AndrewAnnex/SpiceyPy?branch=master
.. |Documentation Status| image:: https://readthedocs.org/projects/spiceypy/badge/?version=master
   :target: http://spiceypy.readthedocs.org/en/master/
.. |Join the chat| image:: https://badges.gitter.im/Join%20Chat.svg
   :target: https://gitter.im/AndrewAnnex/SpiceyPy?utm_source=badge
.. |Citation| image:: https://zenodo.org/badge/16987/AndrewAnnex/SpiceyPy.svg
   :target: https://zenodo.org/badge/latestdoi/16987/AndrewAnnex/SpiceyPy


SpiceyPy is a Python wrapper for the NAIF C SPICE Toolkit (N65),
compatible with Python 2 and 3, written using ctypes.

Introduction
------------

| SpiceyPy is a python wrapper for the `SPICE Toolkit <http://naif.jpl.nasa.gov/naif/>`__.
  SPICE is an essential tool for scientists and engineers alike in the planetary
  science field for Solar System Geometry.
| Please visit the NAIF website for more details.

*IMPORTANT*: I have no current affiliation with NASA, NAIF, or JPL. The
code is provided "as is", use at your own risk.

Installation
------------
First install the dependencies (numpy, six, pytest) for the project. Then
run ``pip install spiceypy`` to install from pypi. SpiceyPy is also available
through conda by either first installing pip via conda or by running
``conda install -c https://conda.anaconda.org/andrewannex spiceypy``.

If you wish to install spiceypy from source first download the project. Then
extract it, and inside just run ``python setup.py install``. If
you are updating to the newest commit/version, be sure to completely
delete the SpiceyPy folder in your site-packages. This is normally by running ``pip uninstall spiceypy``

Documentation
-------------

**The SpiceyPy docs are available at:**
`spiceypy.readthedocs.org <http://spiceypy.readthedocs.org>`__.

| The documentation for SpiceyPy is intentionally abridged so as to
  utilize the excellent `documentation provided by the
  NAIF. <http://naif.jpl.nasa.gov/pub/naif/toolkit_docs/C/index.html>`__
| Please refer to C and IDL documentation available on the NAIF website
  for in-depth explanations. Each function has a link to the
  corresponding C function in the NAIF docs at a minimum.

Citing SpiceyPy
---------------

| If the use of SpiceyPy is used in a publication, please consider
  citing SpiceyPy and the SPICE toolkit. The citation information
  for SPICE can be found on the NAIF website. To cite SpiceyPy please
  utilize the zenodo DOI badge at the top of this readme.


Travis and Coveralls Status
---------------------------

| A secondary list (non-maintained) of what functions have been wrapped
  can be found
  `here <https://github.com/AndrewAnnex/SpiceyPy/wiki/Wrapper-Completion>`__.
| A majority of SPICE functions have written wrappers along with tests
  mainly derived from the CSPICE documentation.
| A small number of functions have no wrapper functions of any kind due
  to lack of necessity, they are labeled as "Skipped".
| The rest of the functions generally have written wrapper functions but
  remain untested, mostly due to lack of SPICE documentation (the EK
  kernel functions are one example of this).
| Functions that utilize call-backs have not been wrapped or tested yet,
  although ctypes does support call-backs so they will be revisited.
| If you encounter an error with a function please report it or push
  a PR with a fix, with ctypes it is easy!

How to Help
-----------

| Feedback is always welcomed, if you discover that a function is not
  working as expected, submit an issue detailing how
| to reproduce the problem. If you utilize SpiceyPy frequently please
  consider contributing to the project by:
| writing a test, writing a wrapper, doing some code review, adding
  documentation, improving infrastructure code (like setup.py), or by
  spreading the word.

Design Goals
------------

-  [x] Majorly complete coverage of all existing CSPICE commands, within
   reason.
-  [x] Useful, but abbreviated commenting on functions.
-  [x] Python 2 and 3 support.
-  [x] Numpy Support.
-  [x] Enable vectorization of certain functions to be more like ICY.

Known Working Environments:
---------------------------

SpicyPy is now compatible with modern Linux, Mac, and Windows
environments. Since the package is a wrapper, any environment not
supported by the NAIF is similarly not supported by SpiceyPy.
If you run into issues with your system please submit an issue with details.

- OS: OS X, Linux, Windows
- CPU: 64bit & 32bit
- Python 2.7, 3.3, 3.4, 3.5

Acknowledgements
----------------

`DaRasch <https://github.com/DaRasch>`__ wrote spiceminer, which I
looked at to get SpiceCells working, thanks!

