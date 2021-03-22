---
description: AMD Optimizing C/C++ Compiler (AOCC)
---

# AMD

The AMD Optimizing C/C++ Compiler \(AOCC\) is only available on CPU nodes. AMD compilers can be loaded by executing the following commands at the Linux prompt:

```text
module load aocc
```

For more information on the AMD compilers run \[flang \| clang \] -help

## Suggested Compilers

| Language | Serial | MPI | OpenMP | MPI + OpenMP |
| :--- | :--- | :--- | :--- | :--- |
| Fortran | flang | mpif90 | ifort -fopenmp | mpif90 -fopenmp |
| C | clang | mpiclang | icc -fopenmp | mpicc -fopenmp |
| C++ | clang++ | mpiclang | icpc -fopenmp | mpicxx -fopenmp |

