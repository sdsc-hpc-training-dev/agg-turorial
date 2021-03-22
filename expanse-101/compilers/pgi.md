---
description: PGI Compilers
---

# PGI

The PGI compilers can be loaded by executing the following commands at the Linux prompt or placing in your startup file \(~/.cshrc or ~/.bashrc\)

```text
module purge
module load pgi mvapich2_ib
```

For more information on the PGI compilers: man \[pgf90 \| pgcc \| pgCC\]

## Suggested Compilers

| Language | Serial | MPI | OpenMP | MPI+OpenMP |
| :--- | :--- | :--- | :--- | :--- |
| Fortran | pgf90 | mpif90 | mpif90 -mp | mpif90 -mp |
| C | pgcc | mpicc | pgcc -mp | mpicc -mp |
| C++ | pgCC | mpicxx | pgCC -mp | mpicxx -mp |

 For AVX support, compile with `-fast`

