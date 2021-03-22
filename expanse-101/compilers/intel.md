---
description: Intel Compilers
---

# Intel

The Intel compilers and the MVAPICH2 MPI implementation will be loaded by default. The MKL and related libraries may need several modules. If you have modified your environment, you can reload by executing the following commands such as those shown below at the Linux prompt or placing in your startup file \(~/.cshrc or ~/.bashrc\). Below is the list of modules created for the DGEMM MKL example described below \(on 01/25/21\):

```text
module purge
module load slurm
module load cpu
module load gpu/0.15.4  
module load intel/19.0.5.281
module load intel-mkl/2020.3.279
```

For more information on the Intel compilers run: \[ifort \| icc \| icpc\] -help

## Suggested Compilers

| Language | Serial | MPI | OpenMP | MPI + OpenMP |
| :--- | :--- | :--- | :--- | :--- |
| Fortran | ifort | mpif90 | mpif90 -fopenmp | mpif90 -qopenmp |
| C | icc | mpicc | icc -qopenmp | mpicc -qopenmp |
| C++ | icpc | mpicxx | icpc -qopenmp | mpicxx -qopenmp |

For AVX2 support, compile with the -xHOST option. Note that -xHOST alone does not enable aggressive optimization, so compilation with -O3 is also suggested. The -fast flag invokes -xHOST, but should be avoided since it also turns on interprocedural optimization \(-ipo\), which may cause problems in some instances.

