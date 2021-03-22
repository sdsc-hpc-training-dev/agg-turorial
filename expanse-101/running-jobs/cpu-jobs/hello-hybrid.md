---
description: >-
  Simple tutorial to compile and run a hybrid (MPI + OpenMP) hello world program
  on Expanse CPU node
---

# Hello Hybrid

## Code

`hybrid.c`
```c
#include <stdio.h>
#include "mpi.h"
#include <omp.h>

int main(int argc, char *argv[]) {
  int numprocs, rank, namelen;
  char processor_name[MPI_MAX_PROCESSOR_NAME];
  int iam = 0, np = 1;

  MPI_Init(&argc, &argv);
  MPI_Comm_size(MPI_COMM_WORLD, &numprocs);
  MPI_Comm_rank(MPI_COMM_WORLD, &rank);
  MPI_Get_processor_name(processor_name, &namelen);

  #pragma omp parallel default(shared) private(iam, np)
  {
    np = omp_get_num_threads();
    iam = omp_get_thread_num();
    printf("Hello from thread %d out of %d from process %d out of %d on %s\n",
           iam, np, rank, numprocs, processor_name);
  }

  MPI_Finalize();
}
```

`hybrid-slurm.sb`
```bash
#!/bin/bash
#SBATCH --job-name="hellohybrid"
#SBATCH --output="hellohybrid.%j.%N.out"
#SBATCH --partition=shared
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=2
#SBATCH --cpus-per-task=16
#SBATCH -B 2:16:1
#SBATCH --export=ALL
#SBATCH -t 01:30:00

#Load Module Environment
module purge
module load slurm
module load cpu
module load intel
module load intel-mpi

#Run
export OMP_NUM_THREADS=16
mpirun -genv I_MPI_PIN_DOMAIN=omp:compact ./hello_hybrid
```

## Compiling

1. Load modules:

   ```text
   [user@login01 HYBRID]$ module purge
   [user@login01 HYBRID]$ module load slurm
   [user@login01 HYBRID]$ module load cpu
   [user@login01 HYBRID]$ module load intel
   [user@login01 HYBRID]$ module load intel-mpi
   [user@login01 HYBRID]$ export I_MPI_CC=icc 
   ```

2. Compile the code:

   ```text
   [user@login01 HYBRID]$ mpicc -qopenmp -o hello_hybrid hybrid.c
   ```

## Submission

```text
[user@login01 HYBRID]$ sbatch hybrid-slurm.sb
Submitted batch job 1089019
[...]
```

## Output

`hellohybrid.1089019.exp-10-07.out`
```text
Hello from thread 0 out of 16 from process 1 out of 2 on exp-10-07
Hello from thread 14 out of 16 from process 1 out of 2 on exp-10-07
Hello from thread 1 out of 16 from process 1 out of 2 on exp-10-07
Hello from thread 4 out of 16 from process 1 out of 2 on exp-10-07
Hello from thread 12 out of 16 from process 1 out of 2 on exp-10-07
Hello from thread 2 out of 16 from process 1 out of 2 on exp-10-07
Hello from thread 13 out of 16 from process 1 out of 2 on exp-10-07
Hello from thread 7 out of 16 from process 1 out of 2 on exp-10-07
Hello from thread 3 out of 16 from process 1 out of 2 on exp-10-07
Hello from thread 8 out of 16 from process 1 out of 2 on exp-10-07
Hello from thread 0 out of 16 from process 0 out of 2 on exp-10-07
Hello from thread 3 out of 16 from process 0 out of 2 on exp-10-07
Hello from thread 13 out of 16 from process 0 out of 2 on exp-10-07
Hello from thread 14 out of 16 from process 0 out of 2 on exp-10-07
Hello from thread 6 out of 16 from process 0 out of 2 on exp-10-07
Hello from thread 7 out of 16 from process 0 out of 2 on exp-10-07
Hello from thread 11 out of 16 from process 0 out of 2 on exp-10-07
Hello from thread 12 out of 16 from process 0 out of 2 on exp-10-07
Hello from thread 4 out of 16 from process 0 out of 2 on exp-10-07
Hello from thread 1 out of 16 from process 0 out of 2 on exp-10-07
Hello from thread 5 out of 16 from process 0 out of 2 on exp-10-07
Hello from thread 15 out of 16 from process 1 out of 2 on exp-10-07
Hello from thread 11 out of 16 from process 1 out of 2 on exp-10-07
Hello from thread 9 out of 16 from process 1 out of 2 on exp-10-07
Hello from thread 5 out of 16 from process 1 out of 2 on exp-10-07
Hello from thread 2 out of 16 from process 0 out of 2 on exp-10-07
Hello from thread 6 out of 16 from process 1 out of 2 on exp-10-07
Hello from thread 9 out of 16 from process 0 out of 2 on exp-10-07
Hello from thread 8 out of 16 from process 0 out of 2 on exp-10-07
Hello from thread 10 out of 16 from process 1 out of 2 on exp-10-07
Hello from thread 10 out of 16 from process 0 out of 2 on exp-10-07
Hello from thread 15 out of 16 from process 0 out of 2 on exp-10-07
```

