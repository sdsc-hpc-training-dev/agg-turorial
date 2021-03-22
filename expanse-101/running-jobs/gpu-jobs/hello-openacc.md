---
description: >-
  Simple tutorial to compile and run an OpenACC laplace2d program on Expanse GPU
  node
---

# Hello OpenACC

## Code

`laplace2d.c`
```c
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

#include <math.h>
#include <string.h>
#include <stdio.h>
#include "timer.h"

#define NN 4096
#define NM 4096

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

#pragma acc data copy(A), create(Anew)
    while ( error > tol && iter < iter_max )
    {
        error = 0.0;

#pragma acc kernels
        for( int j = 1; j < n-1; j++)
        {
            for( int i = 1; i < m-1; i++ )
            {
                Anew[j][i] = 0.25 * ( A[j][i+1] + A[j][i-1]
                                    + A[j-1][i] + A[j+1][i]);
                error = fmax( error, fabs(Anew[j][i] - A[j][i]));
            }
        }

#pragma acc kernels
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

`timer.h`
```c
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

#ifndef TIMER_H
#define TIMER_H

#include <stdlib.h>

#ifdef WIN32
#define WIN32_LEAN_AND_MEAN
#include <windows.h>
#else
#include <sys/time.h>
#endif

#ifdef WIN32
double PCFreq = 0.0;
__int64 timerStart = 0;
#else
struct timeval timerStart;
#endif

void StartTimer()
{
#ifdef WIN32
    LARGE_INTEGER li;
    if(!QueryPerformanceFrequency(&li))
        printf("QueryPerformanceFrequency failed!\n");

    PCFreq = (double)li.QuadPart/1000.0;

    QueryPerformanceCounter(&li);
    timerStart = li.QuadPart;
#else
    gettimeofday(&timerStart, NULL);
#endif
}

// time elapsed in ms
double GetTimer()
{
#ifdef WIN32
    LARGE_INTEGER li;
    QueryPerformanceCounter(&li);
    return (double)(li.QuadPart-timerStart)/PCFreq;
#else
    struct timeval timerStop, timerElapsed;
    gettimeofday(&timerStop, NULL);
    timersub(&timerStop, &timerStart, &timerElapsed);
    return timerElapsed.tv_sec*1000.0+timerElapsed.tv_usec/1000.0;
#endif
}

#endif // TIMER_H
```

`openacc-gpu-shared.sb`
```bash
#!/bin/bash
#SBATCH --job-name="OpenACC"
#SBATCH --output="OpenACC.%j.%N.out"
#SBATCH --partition=gpu-shared
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --gpus=1
#SBATCH --acount=abc123
#SBATCH -t 01:00:00

#Environment
module purge
module load slurm
module load gpu
module load pgi

#Run the job
./laplace2d.openacc.exe
```

## Compiling

1. Get an [interactive node](../#interactive-jobs)
2. Load modules:

   ```text
   [user@exp-7-59 ~]$ module purge
   [user@exp-7-59 ~]$ module load slurm
   [user@exp-7-59 ~]$ module load gpu
   [user@exp-7-59 ~]$ module load pgi
   [user@exp-7-59 ~]$ module list

   Currently Loaded Modules:
     1) slurm/expanse/20.02.3   2) gpu/1.0   3) pgi/20.4
   ```

3. Compile the code: 

   ```text
   [user@exp-7-59 OpenACC]$ pgcc -o laplace2d.openacc.exe -fast \
      -Minfo -acc -ta=tesla:cc70 laplace2d.c
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
   [user@exp-7-59 OpenACC]$ exit
   ```

## Submission

```text
[user@login01 OpenACC]$ sbatch openacc-gpu-shared.sb
Submitted batch job 1093002
[user@login01 OpenACC]$ squeue -u user
     JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
[mthomas@login01 OpenACC]$ ll
total 106
drwxr-xr-x  2 user use300     8 Jan 29 16:25 .
drwxr-xr-x 10 user use300    10 Jan 29 03:28 ..
-rw-r--r--  1 user use300  2136 Jan 29 03:27 laplace2d.c
-rwxr-xr-x  1 user use300 52080 Jan 29 16:20 laplace2d.openacc.exe
-rw-r--r--  1 user use300   234 Jan 29 16:25 OpenACC.1093002.exp-7-57.out
-rw-r--r--  1 user use300   332 Jan 29 16:11 openacc-gpu-shared.sb
-rw-r--r--  1 user use300  1634 Jan 29 03:27 README.txt
-rw-r--r--  1 user use300  1572 Jan 29 03:27 timer.h
```

## Output

`OpenACC.1093002.exp-7-57.out`
```text
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
```

