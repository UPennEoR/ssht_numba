==========
ssht_numba
==========

**Spin-Spherical Harmonic Transforms jit-compiled with numba**


Features
========

Installation
============
There is a single external requirement that will not be installed automatically, and
that is `FFTW`. This can usually be installed via your package manager, but take care
to install the *shared library*. If compiling yourself, that means using the option
`--enable-shared`.

Then, installation should be as simple as `pip install .` from the top-level directory,
or `pip install git+git://github.com/UPennEoR/ssht_numba`. If you installed `FFTW` to a
non-default location, then you can point to its location using the environment variable
`FFTW_PATH`, which should be the path to the `lib` folder, eg.:
`FFTW_PATH=/usr/lib pip install .`.

Other dependencies of ssht_numba are installed automatically. However, if you are using
`conda` and would like these packages to be installed with `conda` rather than `pip`,
you may want to do `conda install numpy numba cffi` prior to installing the package.

Quick Usage
===========


Development
===========

pre-commit
----------
This package has `pre-commit` hooks set up. If developing this package, please
`pip install pre-commit` and `pre-commit install`.

Versioning
----------
This package uses `pyscaffold`, which in turn uses `setuptools_scm`, and manages
versioning via Git tags. Versioning should use https://semver.org semantic versioning
rules.
>>>>>>> Stashed changes

Note
====

This project has been set up using PyScaffold 3.2.1. For details and usage
information on PyScaffold see https://pyscaffold.org/.
