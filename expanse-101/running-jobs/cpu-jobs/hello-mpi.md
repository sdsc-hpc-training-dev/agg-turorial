---
description: >-
  Simple tutorial to compile and run a MPI hello world program on Expanse CPU
  node
---

# Hello MPI

## Code

`hello\_mpi.f90`
```text
!  Fortran example  
   program hello
   include 'mpif.h'
   integer rank, size, ierror, tag, status(MPI_STATUS_SIZE)
   
   call MPI_INIT(ierror)
   call MPI_COMM_SIZE(MPI_COMM_WORLD, size, ierror)
   call MPI_COMM_RANK(MPI_COMM_WORLD, rank, ierror)
   print*, 'node', rank, ': Hello world!'
   call MPI_FINALIZE(ierror)
   end
```

`mpi-slurm.sb`
```bash
#!/bin/bash
#SBATCH --job-name="hellompi"
#SBATCH --output="hellompi.%j.%N.out"
#SBATCH --partition=compute
####SBATCH --partition=shared
#SBATCH --nodes=3
#SBATCH --ntasks-per-node=12
#SBATCH --export=ALL
#SBATCH -t 00:04:00
#SBATCH -A abc123

# This job runs with 3 nodes, and a total of 12 cores.
## Environment
### MODULE ENV: updated 01/28/2020 (MPT)
module purge
module load slurm
module load cpu
module load gcc/10.2.0
module load openmpi/4.0.4

## Use srun to run the job
srun --mpi=pmi2 -n 12 --cpu-bind=rank ./hello_mpi
```

In the batch script we are using the GNU compiler, and asking for 2 CPU compute nodes, with 128 tasks per node for a total of 256 tasks. The name of job is set in line 2, while the name of the output file is set in line 3, where "**%j**" is the Slurm JOB\_ID, and and "**%N**" is the compute node name. You can name your outupt file however you wish, but it helpful to keep track of the JOB\_ID and node info in case something goes wrong.

## Compiling

1. Load modules:

   ```text
   [user@login01 MPI]$ module purge
   [user@login01 MPI]$ module load slurm
   [user@login01 MPI]$ module load cpu
   [user@login01 MPI]$ module load gcc/10.2.0
   [user@login01 MPI]$ module load openmpi/4.0.4
   [user@login01 MPI]$ module load openmpi/4.0.4
   [user@login01 MPI]$ module list

   Currently Loaded Modules:
     1) slurm/expanse/20.02.3   2) cpu/1.0   3) gcc/10.2.0   4) openmpi/4.0.4
   ```

2. Compile the code:

   ```text
   [user@login01 MPI]$ mpif90 -o hello_mpi hello_mpi.f90
   ```

## Submission

```text
[user@login02 OPENMP]$ sbatch mpi-slurm.sb
Submitted batch job 667424

[user@login01 MPI]$ squeue -u user -u user
 JOBID PARTITION     NAME  USER ST   TIME  NODES NODELIST(REASON)
667424   compute hellompi  user PD   0:00      2 (Priority)


[user@login01 MPI]$ squeue -u user -u user
 JOBID PARTITION     NAME  USER ST   TIME  NODES NODELIST(REASON)
667424   compute hellompi  user CF   0:01      2 exp-2-[28-29]

[user@login01 MPI]$ squeue -u user -u user
 JOBID PARTITION     NAME  USER ST TIME    NODES NODELIST(REASON)
667424   compute hellompi  user  R   0:02      2 exp-2-[28-29]

[user@login01 MPI]$ squeue -u user -u user
 JOBID PARTITION     NAME  USER ST TIME    NODES NODELIST(REASON)
 
[user@login01 MPI]$ ll
total 151
drwxr-xr-x 2 user abc123    13 Dec 10 01:06 .
drwxr-xr-x 8 user abc123     8 Oct  8 04:16 ..
-rwxr-xr-x 1 user abc123 21576 Oct  8 03:12 hello_mpi
-rw-r--r-- 1 user abc123  8448 Oct  8 03:32 hellompi.667424.exp-2-28.out
```

## Output

`hellompi.667424,exp-2-28.out`
```text
node           1 : Hello world!
node           0 : Hello world!
[SNIP]
node         247 : Hello world!
node         254 : Hello world!
node         188 : Hello world!
node         246 : Hello world!
```

