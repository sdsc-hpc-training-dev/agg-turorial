# GPU Jobs

## GPU Hardware

| GPU Type | NVIDIA V100 SMX2 |
| :--- | :--- |
| Nodes | 52 |
| GPUs/node | 4 |
| CPU Type | Xeon Gold 6248 |
| Cores/socket | 20 |
| Sockets | 2 |
| Clock speed | 2.5 GHz |
| Flop speed | 34.4 TFlop/s |
| Memory capacity | 384 GB DDR4 DRAM |
| Local Storage | 1.6TB Samsung PM1745b NVMe PCIe SSD |
| Max CPU Memory bandwidth | 281.6 GB/s |

## Using GPU Nodes

* GPU nodes are allocated as a separate resource. The conversion rate is \(TBD\) Expanse Service Units \(SUs\) to 1 V100 GPU-hour.
* GPU nodes are not the same as the login nodes

**GPU codes must be compiled by requesting an interactive session on a GPU nodes**

* Batch: GPU nodes can be accessed via either the "gpu" or the "gpu-shared" partitions: `#SBATCH -p gpu` or `#SBATCH -p gpu-shared`
* Be sure to setup your CUDA environment for the compiler that you want to use   

#### For CUDA codes, you will need the cuda Compiler. Expanse has several CUDA compiler libraries

```text
# Environment for the CUDA Compiler
module purge
module load slurm
module load gpu
module load cuda
```

Expanse has several CUDA compiler libraries, and you can see them by running `module avail` \(once you have loaded the gpu module\)

```text
------------------------- /cm/shared/modulefiles -----------------------
cuda10.2/blas/10.2.89     cuda10.2/profiler/10.2.89   sdsc/1.0
cuda10.2/fft/10.2.89      cuda10.2/toolkit/10.2.89    xsede/xdusage/2.1-1
cuda10.2/nsight/10.2.89   default-environment
```

#### For OpenACC codes, you will need the PGI Compiler:

```text
# Environment for the PGI Compiler
module purge
module load slurm
module load gpu
module load pgi
```

## Obtaining CUDA Information

Once you are on an [**interactive node**](../#interactive-jobs), reload the module environment:

```text
[user@exp-7-59 OpenACC]$
[user@exp-7-59 OpenACC]$ module purge
[user@exp-7-59 OpenACC]$ module load slurm
[user@exp-7-59 OpenACC]$ module load gpu
[user@exp-7-59 OpenACC]$ module load pgi
[user@exp-7-59 OpenACC]$ module list

Currently Loaded Modules:
  1) slurm/expanse/20.02.3   2) gpu/0.15.4   3) pgi/20.4
```

You can also check node configuration using the `nvidia-smi` command:

```text
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

## Compiling:

All compilng for GPU codes **must be done on an** [**interactive node**](../#interactive-jobs) to compile the code:

1. Load the right Modules
2. Compile the Source code
3. Run code locally or exit interactive node and submit the batch script

