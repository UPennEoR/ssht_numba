import os
import glob

from cffi import FFI

ffi = FFI()

cdef_str = """
typedef int ssht_dl_size_t;
typedef int ssht_dl_method_t;

int ssht_sampling_mw_n(int L);
int ssht_sampling_mw_ntheta(int L);
int ssht_sampling_mw_nphi(int L);

double ssht_sampling_mw_t2theta(int t, int L);
double ssht_sampling_mw_p2phi(int p, int L);
double ssht_sampling_mw_ss_t2theta(int t, int L);
double ssht_sampling_mw_ss_p2phi(int p, int L);

void ssht_sampling_gl_thetas_weights(double *thetas, double *weights, int L);
double ssht_sampling_gl_p2phi(int p, int L);

void ssht_core_mw_forward_sov_conv_sym(double _Complex *flm,
                                       const double _Complex *f,
                        		       int L, int spin,
                        		       ssht_dl_method_t dl_method,
                        		       int verbosity);

void ssht_core_mw_inverse_sov_sym(double _Complex *f,
                                  const double _Complex *flm,
                                  int L, int spin,
                                  ssht_dl_method_t dl_method,
                                  int verbosity);

void ssht_core_mw_forward_sov_conv_sym_real(double _Complex *flm,
                                            const double *f,
                                            int L,
                                            ssht_dl_method_t dl_method,
                                            int verbosity);

void ssht_core_mw_inverse_sov_sym_real(double *f,
                                       const double _Complex *flm,
                                       int L,
                                       ssht_dl_method_t dl_method,
                                       int verbosity);

void ssht_core_mw_forward_sov_conv_sym_ss(double _Complex *flm,
                                          const double _Complex *f,
                                          int L, int spin,
                                          ssht_dl_method_t dl_method,
                                          int verbosity);

void ssht_core_mw_inverse_sov_sym_ss(double _Complex *f,
                                     const double _Complex *flm,
                                     int L, int spin,
                                     ssht_dl_method_t dl_method,
                                     int verbosity);

void ssht_core_mw_forward_sov_conv_sym_ss_real(double _Complex *flm,
                                               const double *f,
                                               int L,
                                               ssht_dl_method_t dl_method,
                                               int verbosity);

void ssht_core_mw_inverse_sov_sym_ss_real(double *f,
                                          const double _Complex *flm,
                                          int L,
                                          ssht_dl_method_t dl_method,
                                          int verbosity);

void ssht_core_gl_forward_sov(double _Complex *flm, const double _Complex *f,
                          int L, int spin, int verbosity);

void ssht_core_gl_inverse_sov(double _Complex *f, const double _Complex *flm,
                          int L, int spin, int verbosity);
"""

ffi.cdef(cdef_str)

ssht_root = '/users/zmartino/zmartino/projects/ssht_numba/ssht'

# include_dirs = [ssht_root + '/include', ssht_root + '/include/c']
include_dirs = [
    ssht_root + '/fftw/include',
    ssht_root + '/src/c',
]

library_dirs = [
    ssht_root + '/fftw/lib'
]

extra_link_args=[
    "-L/users/zmartino/zmartino/projects/ssht_numba/ssht/fftw"
]

# the compiler options from the ssht makefile
extra_compile_args = [
    '-std=c99',
#     '-pedantic',
    '-Wall',
    '-O3',
    '-fopenmp',
    '-DSSHT_VERSION=\"1.2b1\"',
    '-DSSHT_BUILD=\"`git rev-parse HEAD`\"',
    '-fPIC'
]

# avoid including the ssht_about.c source file, it is not needed here
# for cffi and produces an error

# the ssht_about.c path is the first element of the sorted list
ssht_src = sorted(glob.glob(os.path.join(ssht_root, 'src', 'c', '*.c')))[1:]

ffi.set_source("_ssht_cffi",
"""
#include "ssht_types.h"
#include "ssht_error.h"
#include "ssht_sampling.h"
#include "ssht_dl.h"
#include "ssht_core.h"
#include "ssht_adjoint.h"
""",
    sources=ssht_src,
    libraries=["fftw3"],
    include_dirs=include_dirs,
    extra_link_args=extra_link_args,
    extra_compile_args=extra_compile_args)

if __name__ == '__main__':
    ffi.compile(verbose=True)