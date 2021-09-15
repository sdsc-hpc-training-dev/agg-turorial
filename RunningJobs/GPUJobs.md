---
sort: 2
---

#  Compiling and Running GPU Jobs <a name="comp-run-gpu"></a>
**Sections**
* [Using Expanse GPU Nodes](#comp-run-gpu-nodes)
* [Using Interactive GPU Nodes](#comp-run-gpu-interactive)
* [Laplace2D (GPU/OpenACC): Source Code](#laplace2d-gpu)

##  Using Expanse GPU Nodes <a name="comp-run-gpu-nodes"></a>

###  Expanse GPU Hardware

|	GPU Type	|	NVIDIA V100 SMX2	|
|	  :----	|	  :----
|	Nodes	|	52	|
|	GPUs/node	|	4	|
|	CPU Type	|	Xeon Gold 6248	|
|	Cores/socket	|	20	|
|	Sockets	|	2	|
|	Clock speed	|	2.5 GHz	|
|	Flop speed	|	34.4 TFlop/s	|
|	Memory capacity	|	*384 GB DDR4 DRAM	|
|	Local Storage	|	1.6TB Samsung PM1745b NVMe PCIe SSD	|
|	Max CPU Memory bandwidth	|	281.6 GB/s	|

###  Using GPU Nodes

* GPU nodes are allocated as a separate resource. The conversion rate is (TBD) Expanse Service Units (SUs) to 1 V100 GPU-hour. 
* Login nodes are not the same as the GPU nodes:
   *  _GPU codes must be compiled by requesting an interactive session on a GPU nodes_
* Batch: GPU nodes can be accessed via either the "gpu" or the "gpu-shared" partitions.
   *  #SBATCH -p gpu
   * or #SBATCH -p gpu-shared
* Be sure to setup  your CUDA environment for the compiler that you want to use:   
   * For CUDA codes, you will need the cuda Compiler. Expanse has several CUDA compiler libraries

```
 Environment for the CUDA Compiler
module purge
module load slurm
module load gpu
module load cuda
```
   * Note that Expanse has several CUDA compiler libraries, and you can see them by
   running *module avail* (once you have loaded the gpu module)

   ```
   ------------------------------------ /cm/shared/modulefiles ------------------------------------
      cuda10.2/blas/10.2.89      cuda10.2/profiler/10.2.89    sdsc/1.0
      cuda10.2/fft/10.2.89       cuda10.2/toolkit/10.2.89     xsede/xdusage/2.1-1
      cuda10.2/nsight/10.2.89    default-environment

   ```

   * For OpenACC codes, you will need the PGI Compiler:

```
 Environment for the PGI Compiler
module purge
module load slurm
module load gpu
module load pgi
```

###  Using Interactive GPU Nodes  <a name="comp-run-gpu-interactive"></a>
* Interactive GPU node:

```
[user@login01 OpenACC]$ srun --pty --nodes=1 --ntasks-per-node=1 --cpus-per-task=10 -p gpu-debug --gpus=1 -t 00:10:00 -A abc123 /bin/bash
srun: job 1089081 queued and waiting for resources
srun: job 1089081 has been allocated resources
[user@exp-7-59 OpenACC]$

```

* Change to the tutorial *OpenAC*  directory:

```
[user@exp-7-59 OpenACC]$ ll
total 71
-rw-r--r-- 1 user abc123  2136 Oct  7 11:28 laplace2d.c
-rwxr-xr-x 1 user abc123 52056 Oct  7 11:28 laplace2d.openacc.exe
-rw-r--r-- 1 user abc123   234 Oct  7 11:28 OpenACC.108739.exp-7-57.out
-rw-r--r-- 1 user abc123   307 Oct  8 00:21 openacc-gpu-shared.sb
-rw-r--r-- 1 user abc123  1634 Oct  7 11:28 README.txt
-rw-r--r-- 1 user abc123  1572 Oct  7 11:28 timer.h
```

###  Obtaining GPU/CUDA: Node Information

* Once you are on an interactive node, reload the module environment:

```
[user@exp-7-59 OpenACC]$
[user@exp-7-59 OpenACC]$ module purge
[user@exp-7-59 OpenACC]$ module load slurm
[user@exp-7-59 OpenACC]$ module load gpu
[user@exp-7-59 OpenACC]$ module load pgi
[user@exp-7-59 OpenACC]$ module list

Currently Loaded Modules:
  1) slurm/expanse/20.02.3   2) gpu/0.15.4   3) pgi/20.4

```

* You can also check node configuration using the nvidia-smi command:

```

[user@exp-7-59 OpenACC]$ nvidia-smi
Fri Jan 29 12:33:25 2021       
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 450.51.05    Driver Version: 450.51.05    CUDA Version: 11.0     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  Tesla V100-SXM2...  On   | 00000000:18:00.0 Off |                    0 |
| N/A   32C    P0    41W / 300W |      0MiB / 32510MiB |      0%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+

+-----------------------------------------------------------------------------+
| Processes:                                                                  |
|  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
|        ID   ID                                                   Usage      |
|=============================================================================|
|  No running processes found                                                 |
+-----------------------------------------------------------------------------+

```

###  GPU Compiling:
All compilng for GPU codes must be done on an interactive node:
Steps to compile the code:

1. Otain an interactive node
2. Load the right Modules
3. Compile the Source code
4. Run code locally, or exit interactive node and submit the batch script

##  [Vector Addition (GPU/CUDA)](#vec-add-cuda-gpu)
**Subsections:**
* [Vector Addition (GPU/CUDA): Source Code](#vec-add-cuda-source)
* [Vector Addition (GPU/CUDA): Compiling](#vec-add-cuda-compile)
* [Vector Addition (GPU/CUDA): Batch Script Submission](#vec-add-cuda-batch-submit)
* [Vector Addition (GPU/CUDA): Batch Script Output](#vec-add-cuda-batch-output)


##  [Laplace2D (GPU/OpenACC)](#laplace2d-gpu)
**Subsections:**
* [Laplace2D (GPU/OpenACC): Source Code](#laplace2d-gpu-source)
* [Laplace2D (GPU/OpenACC): Compiling](#laplace2d-gpu-compile)
* [Laplace2D (GPU/OpenACC): Batch Script Submission](#laplace2d-gpu-batch-submit)
* [Laplace2D (GPU/OpenACC): Batch Script Output](#laplace2d-gpu-batch-output)

###  Laplace2D (GPU/OpenACC): Source Code  <a name="laplace2d-gpu-source"></a>
Source Code

```
[user@login01 OpenACC]$ !cat
cat laplace2d.c
/*
 *  Copyright 2012 NVIDIA Corporation
 *
 *  Licensed under the Apache License, Version 2.0 (the "License");
 *  you may not use this file except in compliance with the License.
 *  You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 *  Unless required by applicable law or agreed to in writing, software
 *  distributed under the License is distributed on an "AS IS" BASIS,
 *  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 *  See the License for the specific language governing permissions and
 *  limitations under the License.
 */

 include <math.h>
 include <string.h>
 include <stdio.h>
 include "timer.h"

 define NN 4096
 define NM 4096

double A[NN][NM];
double Anew[NN][NM];

int main(void)
{
	int laplace(void);
	printf("main()\n");
	laplace();
}

int laplace()
{
    const int n = NN;
    const int m = NM;
    const int iter_max = 1000;

    const double tol = 1.0e-6;
    double error     = 1.0;

    memset(A, 0, n * m * sizeof(double));
    memset(Anew, 0, n * m * sizeof(double));

    for (int j = 0; j < n; j++)
    {
        A[j][0]    = 1.0;
        Anew[j][0] = 1.0;
    }
    printf("Jacobi relaxation Calculation: %d x %d mesh\n", n, m);
    StartTimer();
    int iter = 0;

 pragma acc data copy(A), create(Anew)
    while ( error > tol && iter < iter_max )
    {
        error = 0.0;

 pragma acc kernels
        for( int j = 1; j < n-1; j++)
        {
            for( int i = 1; i < m-1; i++ )
            {
                Anew[j][i] = 0.25 * ( A[j][i+1] + A[j][i-1]
                                    + A[j-1][i] + A[j+1][i]);
                error = fmax( error, fabs(Anew[j][i] - A[j][i]));
            }
        }

 pragma acc kernels
        for( int j = 1; j < n-1; j++)
        {
            for( int i = 1; i < m-1; i++ )
            {
                A[j][i] = Anew[j][i];    
            }
        }

        if(iter % 100 == 0) printf("%5d, %0.6f\n", iter, error);

        iter++;
    }
    double runtime = GetTimer();
    printf(" total: %f s\n", runtime / 1000);
}
```

###  Laplace2D (GPU/OpenACC): Compiling  <a name="laplace2d-gpu-compile"></a>
Compile the code:
1. obtain an interactive node
2. load the right Modules
3. compile the Source code
4. exit interactive node


```
[user@login01 ~]$ module load slurm
[user@login01 ~]$ srun --pty --nodes=1 --ntasks-per-node=1 --cpus-per-task=10 -p gpu-debug -A abc123 --gpus=1 -t 00:10:00 /bin/bash
srun: job 667263 queued and waiting for resources
srun: job 667263 has been allocated resources
[user@exp-7-59 ~]$ module purge
[user@exp-7-59 ~]$ module load slurm
[user@exp-7-59 ~]$ module load gpu
[user@exp-7-59 ~]$ module load pgi
[user@exp-7-59 ~]$ module list

Currently Loaded Modules:
  1) slurm/expanse/20.02.3   2) gpu/1.0   3) pgi/20.4

```

* Now you are set up to compile the code:

```
[user@exp-7-59 OpenACC]$ pgcc -o laplace2d.openacc.exe -fast -Minfo -acc -ta=tesla:cc70 laplace2d.c
"laplace2d.c", line 91: warning: missing return statement at end of non-void
          function "laplace"
  }
  ^

GetTimer:
     20, include "timer.h"
          61, FMA (fused multiply-add) instruction(s) generated
laplace:
     47, Loop not fused: function call before adjacent loop
         Loop unrolled 8 times
         FMA (fused multiply-add) instruction(s) generated
     55, StartTimer inlined, size=2 (inline) file laplace2d.c (37)
     59, Generating create(Anew[:][:]) [if not already present]
         Generating copy(A[:][:]) [if not already present]
         Loop not vectorized/parallelized: potential early exits
     61, Generating implicit copy(error) [if not already present]
     64, Loop is parallelizable
     66, Loop is parallelizable
         Generating Tesla code
         64, #pragma acc loop gang, vector(4) /* blockIdx.y threadIdx.y */
             Generating implicit reduction(max:error)
         66, #pragma acc loop gang, vector(32) /* blockIdx.x threadIdx.x */
     75, Loop is parallelizable
     77, Loop is parallelizable
         Generating Tesla code
         75, #pragma acc loop gang, vector(4) /* blockIdx.y threadIdx.y */
         77, #pragma acc loop gang, vector(32) /* blockIdx.x threadIdx.x */
     88, GetTimer inlined, size=9 (inline) file laplace2d.c (54)
[user@exp-7-59 OpenACC]$
[user@exp-7-59 OpenACC]$ exit
```

###  Laplace2D (GPU/OpenACC): Batch Script Submission  <a name="laplace2d-gpu-batch-submit"></a>
* Batch Script Contents

```

[user@exp-7-59 OpenACC]$ cat openacc-gpu-shared.sb
 !/bin/bash
 SBATCH --job-name="OpenACC"
 SBATCH --output="OpenACC.%j.%N.out"
 SBATCH --partition=gpu-shared
 SBATCH --nodes=1
 SBATCH --ntasks-per-node=1
 SBATCH --gpus=1
 SBATCH --acount=abc123
 SBATCH -t 01:00:00

 Environment
module purge
module load slurm
module load gpu
module load pgi

 Run the job
./laplace2d.openacc.exe

```
* Submit the batch script, and monitor queue status:

```
[mthomas@login01 OpenACC]$ sbatch openacc-gpu-shared.sb
Submitted batch job 1093002
[mthomas@login01 OpenACC]$ squeue -u mthomas
             JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
[mthomas@login01 OpenACC]$ ll
total 106
drwxr-xr-x  2 mthomas use300     8 Jan 29 16:25 .
drwxr-xr-x 10 mthomas use300    10 Jan 29 03:28 ..
-rw-r--r--  1 mthomas use300  2136 Jan 29 03:27 laplace2d.c
-rwxr-xr-x  1 mthomas use300 52080 Jan 29 16:20 laplace2d.openacc.exe
-rw-r--r--  1 mthomas use300   234 Jan 29 16:25 OpenACC.1093002.exp-7-57.out
-rw-r--r--  1 mthomas use300   332 Jan 29 16:11 openacc-gpu-shared.sb
-rw-r--r--  1 mthomas use300  1634 Jan 29 03:27 README.txt
-rw-r--r--  1 mthomas use300  1572 Jan 29 03:27 timer.h

```

###  Laplace2D (GPU/OpenACC): Batch Script Output  <a name="laplace2d-gpu-batch-output"></a>

* Batch Script Output:

```
[mthomas@login01 OpenACC]$ cat OpenACC.1093002.exp-7-57.out
main()
Jacobi relaxation Calculation: 4096 x 4096 mesh
    0, 0.250000
  100, 0.002397
  200, 0.001204
  300, 0.000804
  400, 0.000603
  500, 0.000483
  600, 0.000403
  700, 0.000345
  800, 0.000302
  900, 0.000269
 total: 1.029057 s
[mthomas@login01 OpenACC]$

```
