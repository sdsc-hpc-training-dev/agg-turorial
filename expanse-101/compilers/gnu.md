---
description: GNU Compilers
---

# GNU

The GNU compilers can be loaded by executing the following commands at the Linux prompt or placing in your startup files \(~/.cshrc or ~/.bashrc\)

```text
module purge
module load gnu openmpi_ib
```

For more information on the GNU compilers: man \[gfortran \| gcc \| g++\]

## Suggested Compilers

| Language | Serial | MPI | OpenMP | MPI+OpenMP |
| :--- | :--- | :--- | :--- | :--- |
| Fortran | gfortran | mpif90 | gfortran -fopenmp | mpif90 -fopenmp |
| C | gcc | mpicc | gcc -fopenmp | mpicc -fopenmp |
| C++ | g++ | mpicxx | g++ -fopenmp | mpicxx -fopenmp |

For AVX support, compile with -mavx. Note that AVX support is only available in version 4.7 or later, so it is necessary to explicitly load the gnu/4.9.2 module until such time that it becomes the default



