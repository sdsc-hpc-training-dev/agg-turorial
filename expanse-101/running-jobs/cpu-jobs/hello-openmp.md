---
description: >-
  Simple tutorial to compile and run a OpenMP hello world program on Expanse CPU
  node
---

# Hello OpenMP

## Code

`hello\_openmp.f90`
```text
PROGRAM OMPHELLO
      INTEGER TNUMBER
      INTEGER OMP_GET_THREAD_NUM

!$OMP PARALLEL DEFAULT(PRIVATE)
      TNUMBER = OMP_GET_THREAD_NUM()
      PRINT *, 'HELLO FROM THREAD NUMBER = ', TNUMBER
!$OMP END PARALLEL

      END
```

`openmp-slurm.sb`
```bash
#!/bin/bash
## Example of OpenMP code running on a shared node
#SBATCH --job-name="hell_openmp_shared"
#SBATCH --output="hello_openmp_shared.%j.%N.out"
#SBATCH --partition=shared
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=16
#SBATCH --mem=32G
#SBATCH --export=ALL
#SBATCH --account=sds173
#SBATCH -t 00:10:00

# AOCC environment
module purge
module load slurm
module load cpu
module load aocc

#SET the number of openmp threads
export OMP_NUM_THREADS=16

#Run the openmp job
./hello_openmp
```

The script is loading the module stack, and setting the number of OMP threads

## Compiling

1. Load modules:

   ```text
   module purge
   module load slurm
   module load cpu
   module load aocc
   module list

   Currently Loaded Modules:
     1) slurm/expanse/20.02.3   2) cpu/0.15.4   3) aocc/2.2.0
   ```

2. Compile the code:

   ```text
   flang -fopenmp -o hello_openmp hello_openmp.f90
   ```

## Submission

```text
[user@login02 OPENMP]$ sbatch openmp-slurm.sb
Submitted batch job 1088802

[user@login02 OPENMP]$ squeue -u user
   JOBID PARTITION     NAME  USER ST  TIME  NODES NODELIST(REASON)
 1088802    shared hell_ope  user PD  0:00      1 (None)
[...]
```

## Output

`hello\_openmp\_shared.1088802.exp-3-08.out`
```text
HELLO FROM THREAD NUMBER =            14
HELLO FROM THREAD NUMBER =            15
HELLO FROM THREAD NUMBER =            10
HELLO FROM THREAD NUMBER =             8
HELLO FROM THREAD NUMBER =            12
HELLO FROM THREAD NUMBER =             4
HELLO FROM THREAD NUMBER =             1
HELLO FROM THREAD NUMBER =             0
HELLO FROM THREAD NUMBER =             9
HELLO FROM THREAD NUMBER =             7
HELLO FROM THREAD NUMBER =            11
HELLO FROM THREAD NUMBER =             2
HELLO FROM THREAD NUMBER =             5
HELLO FROM THREAD NUMBER =            13
HELLO FROM THREAD NUMBER =             3
HELLO FROM THREAD NUMBER =             6
```

The non-deterministic order of the thread numbers is normal for HPC systems

