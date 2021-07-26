---
sort: 1
---
# Expanse 101 (Refactored)
## Introduction to Running Jobs on the Expanse Supercomputer

[SDSC HPC Training Group](https://www.sdsc.edu/education_and_training/training_hpc.html)

<hr>
In this tutorial, you will learn how to compile and run jobs on Expanse,
where to run them, and how to run batch jobs. The commands below can be
cut & pasted into the terminal window, when it is connected to
expanse.sdsc.edu.

# Misc Notes/Updates:
*  You must have a expanse account in order to access the system.
  * To obtain a trial account:
      [Expanse trial account](http://www.sdsc.edu/support/user_guides/expanse.html#trial_accounts)
*  You must be familiar with running basic Unix commands: see the
   following tutorials at:
   *  [https://github.com/sdsc-hpc-training/basic_skills](https://github.com/sdsc-hpc-training/basic_skills)
*  The ``hostname`` for Expanse is ``expanse.sdsc.edu``
*  The operating system for Expanse is CentOS
*  For information on moving files from Comet to Expanse, see the [Comet to Expanse
Transition Workshop](https://education.sdsc.edu/training/interactive/202010_comet_to_expanse/index.html)

If you have any difficulties completing these tasks, please contact SDSC
Consulting group at help@xsede.org.

Contents:
* [Expanse Overview & Innovative Features](#overview)
* [Getting Started](#get-start)
  * [Obtaining Expanse Accounts](#get-start-expanse-accounts)
  * [Logging Onto Expanse](#get-start-expanse-logon)
  * [Obtaining Example Code](#get-start-example-code)
  * [Expanse User Portal](#get-start-user-portal)
* [Modules](#modules)
   * [Loading Modules During Login](#module-login-load)
   * [Modules: Popular Lmod Commands](#module-commands)
   * [Loading Modules During Login](#module-login-load)
   * [Lmod warning “rebuild your saved collection”](#lmod-warn-rebuild)

   * [Troubleshooting:Module Error](#module-error)
* [Managing Accounts](#managing-accounts)
   * [Expanse Client Script](#manage-accts-client-script)
   * [Using Accounts in Batch Jobs](#manage-accts-batch-script)
   * [Managing Users on an Account](#manage-accts-users)  
* [Job Charging](#job-charging)
* [Compiling & Linking](#compilers)
   * [Supported Compilers](#compilers-supported")
   * [AMD Optimizing C/C++ Compiler (AOCC)](#compilers-amd)
   * [Intel Compilers](#compilers-intel)
   * [GNU Compilers](#compilers-gnu)
   * [PGI Compilers](#compilers-pgi)
* [Running Jobs](#run-jobs)
   * [Parallel Models](#run-jobs-par-models)
   * [Methods for  Running Jobs on Expanse](#run-jobs-methods)
      * [Batch Jobs](#run-jobs-methods-batch)
      * [Interactive Jobs](#run-jobs-methods-ineractive)
   * [Slurm Resource Manager](#run-jobs-slurm)
      * [Slurm Job Status States](#run-jobs-slurm-status)
      * [Slurm Partitions](#run-jobs-slurm-partition)
      * [Slurm Commands](#run-jobs-slurm-commands)
      * [Slurm Batch Script Example](#run-jobs-slurm-batch)
* [Compiling and Running CPU Jobs](#comp-and-run-cpu-jobs)
   * [Checking Your Environment](#check-env)
   * [Hello World (MPI)](#hello-world-mpi)
        * [Hello World (MPI): Source Code](#hello-world-mpi-source)
        * [Hello World (MPI): Compiling](#hello-world-mpi-compile)
        * [Hello World (MPI): Batch Script Submission](#hello-world-mpi-batch-submit)
        * [Hello World (MPI): Batch Script Output](#hello-world-mpi-batch-output)
        * [Hello World (MPI): Interactive Jobs](#hello-world-mpi-interactive)
   * [Hello World (OpenMP)](#hello-world-omp)
        * [Hello World (OpenMP): Source Code](#hello-world-omp-source)
        * [Hello World (OpenMP): Compiling](#hello-world-omp-compile)
        * [Hello World (OpenMP): Batch Script Submission](#hello-world-omp-batch-submit)
        * [Hello World (OpenMP): Batch Script Output](#hello-world-omp-batch-output)
   * [Compiling and Running Hybrid (MPI + OpenMP) Jobs](#hybrid-mpi-omp)
        * [Hybrid (MPI + OpenMP): Source Code](#hybrid-mpi-omp-source)
        * [Hybrid (MPI + OpenMP): Compiling](#hybrid-mpi-omp-compile)
        * [Hybrid (MPI + OpenMP): Batch Script Submission](#hybrid-mpi-omp-batch-submit)
        * [Hybrid (MPI + OpenMP): Batch Script Output](#hybrid-mpi-omp-batch-output)
* [Compiling and Running GPU Jobs](#comp-run-gpu)
   * [Using Expanse GPU Nodes](#comp-run-gpu-nodes)
   * [Using Interactive GPU Nodes](#comp-run-gpu-interactive)
   * [Vector Addition (GPU/CUDA)](#vec-add-cuda-gpu)
       * [Vector Addition (GPU/CUDA): Source Code](#vec-add-cuda-source)
       * [Vector Addition (GPU/CUDA): Compiling](#vec-add-cuda-compile)
       * [Vector Addition (GPU/CUDA): Batch Script Submission](#vec-add-cuda-batch-submit)
       * [Vector Addition (GPU/CUDA): Batch Script Output](#vec-add-cuda-batch-output)
   * [Laplace2D (GPU/OpenACC)](#laplace2d-gpu)
       * [Laplace2D (GPU/OpenACC): Source Code](#laplace2d-gpu-source)
       * [Laplace2D (GPU/OpenACC): Compiling](#laplace2d-gpu-compile)
       * [Laplace2D (GPU/OpenACC): Batch Script Submission](#laplace2d-gpu-batch-submit)
       * [Laplace2D (GPU/OpenACC): Batch Script Output](#laplace2d-gpu-batch-output)
* Data and Storage, Globus Endpoints, Data Movers, Mount Points
* Final Comments
