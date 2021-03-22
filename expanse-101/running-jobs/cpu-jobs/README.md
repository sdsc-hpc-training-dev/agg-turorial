# CPU Jobs

## General Steps

Change to a working directory \(for example the expanse101 directory\):

```text
cd /home/$USER/expanse101/MPI
```

Verify that the correct modules loaded:

```text
module list
Currently Loaded Modulefiles:
  1) slurm/expanse/20.02.3   2) cpu/1.0   3) gcc/10.2.0   4) openmpi/4.0.4
```

Compile the MPI hello world code:

```text
mpif90 -o hello_mpi hello_mpi.f90
```

Verify executable has been created \(check that date\):

```text
ls -lt hello_mpi
-rwxr-xr-x 1 user sdsc 721912 Mar 25 14:53 hello_mpi
```

Submit job:

```text
sbatch hello_mpi_Slurm.sb
```

## Checking Environment

This simple batch script will show you how to check your user environment and to also verify that your Slurm environment is working.

`env-Slurm.sb`
```bash
#!/bin/bash
#SBATCH --job-name="envinfo"
#SBATCH --output="envinfo.%j.%N.out"
#SBATCH --partition=compute
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --export=ALL
#SBATCH -A sds173
#SBATCH -t 00:1:00

## Load module environment
module purge
module load slurm
module load cpu
module load sdsc

##  perform some basic unix commands

echo "----------------------------------"
echo "hostname= " `hostname`
echo "date= " `date`
echo "whoami= " `whoami`
echo "pwd= " `pwd`
echo "module list= " `module list`
echo "----------------------------------"
echo "env= " `env`
echo "----------------------------------"
echo "expanse-client user -p: " `expanse-client user -p`
echo "----------------------------------"
```

Submit the batch script and monitor until the job is allocated a node, and completes execution:

```text
[user@login01 ENV_INFO]$ sbatch env-Slurm.sb
Submitted batch job 1088090
[user@login01 ENV_INFO]$ squeue -u user
           1088090   compute  envinfo  user PD   0:00   1 (ReqNodeNotAvail,[SNIP]
[...]
[user@login01 ENV_INFO]$ squeue -u user
   JOBID PARTITION     NAME     USER ST   TIME  NODES NODELIST(REASON)
 1088090   compute  envinfo  user PD      0:00      1 (ReqNodeNotAvail,[SNIP]
```

You can get an [Interactive CPU Node](../#interactive-jobs)

