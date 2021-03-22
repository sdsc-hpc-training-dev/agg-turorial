---
description: >-
  Simple tutorial to compile and run a CUDA hello world program on Expanse GPU
  node
---

# Hello CUDA

## Code

`hello\_world\_gpu.cu`
```c
// Cuda By Example - By Sanders and Kudrot
//
// Hello World Program in CUDA C
//
// Contains a function that is executed on the device (GPU)
//

#include<stdio.h>

__global__ void my_kernel(void){
 // nothing done here 
}

int main(void) {

  my_kernel<<<1,1>>>();
  printf("Hello World!\n");
  return 0;

}
```

`hello-world-gpu.sb`
```bash
#!/bin/bash
#SBATCH --job-name="hello_world"
#SBATCH --output="hello_world.%j.%N.out"
#SBATCH --partition=gpu-shared
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --gpus=1
#SBATCH --account=sds173
#SBATCH -t 01:00:00

#Environment
module purge
module load slurm
module load gpu
module load cuda10.2/toolkit/10.2.89

#Run the job
./hello_world
```

## Compiling

1. Get an [interactive node](../#interactive-jobs)
2. Load modules:

   ```text
   [user@exp-7-59 ~]$ module purge
   [user@exp-7-59 ~]$ module load slurm
   [user@exp-7-59 ~]$ module load gpu
   [user@exp-7-59 ~]$ module load cuda
   cuda10.2/blas              cuda10.2/profiler
   cuda10.2/blas/10.2.89      cuda10.2/profiler/10.2.89
   cuda10.2/fft               cuda10.2/toolkit
   cuda10.2/fft/10.2.89       cuda10.2/toolkit/10.2.89
   cuda10.2/nsight            cuda-dcgm
   cuda10.2/nsight/10.2.89    cuda-dcgm/1.7.1.1
   [user@exp-7-59 ~]$ module load cuda10.2/toolkit/10.2.89
   [user@exp-7-59 ~]$ module list

   Currently Loaded Modules:
     1) slurm/expanse/20.02.3   2) gpu/1.0   3) pgi/20.4
     nvcc -o hello_world_device hello_world_gpu.cu
   ```

3. Compile the code:

   ```text
   [user@exp-7-59 hello_world]$ nvcc -o hello_world hello_world_gpu.cu
   [user@exp-7-59 hello_world]$ exit
   ```

## Submission

```text
[user@login01 hello_world]$ sbatch hello-world-gpu.sb
Submitted batch job 1221237
[user@login01 hello_world]$ squeue -u $USER
JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
[user@login01 hello_world]$ ls
hello_world.1221216.exp-4-58.out  hello_world_device  README.txt
hello_world_cpu.c                 hello_world_gpu.cu
hello_world_cpu.cu                hello-world-gpu.sb
```

## Output

`hello\_world.1221237.exp-4-58.out`
```text
Hello World!
```

