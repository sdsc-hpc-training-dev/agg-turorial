# Compilers

Expanse provides the Intel, Portland Group \(PGI\), and GNU compilers along with multiple MPI implementations \(MVAPICH2, MPICH2, OpenMPI\). Most applications will achieve the best performance on Expanse using the Intel compilers and MVAPICH2 and the majority of libraries installed on Expanse have been built using this combination. Having such a diverse set of compilers avaiable allows for our users to customize the software stack need for their application. However, there can be some complexity involved in sorting out the module dependencies needed for your applications. Often the set of modules being loaded depends on the application you are using and the compiler and libraries you may need. In many cases you will need to use the `module spider` command to sort out what modules your application will need. Additionally, it is possible the list will change if some of the dependent software changes.

Other compilers and versions can be installed by Expanse staff on request. More information at [Expanse User Guide](https://www.sdsc.edu/support/user_guides/expanse.html#compiling)

## Supported Compilers

### CPU Nodes

* GNU, Intel, AOCC \(AMD\) compilers
* Multiple MPI implementations \(OpenMPI, MVAPICH2, and IntelMPI\).
* A majority of applications have been built using gcc/10.2.0 which features AMD Rome specific optimization flags \(-march=znver2\).
* Intel, and AOCC compilers all have flags to support Advanced Vector Extensions 2 \(AVX2\).

Users should evaluate their application for best compiler and library selection. GNU, Intel, and AOCC compilers all have flags to support Advanced Vector Extensions 2 \(AVX2\). Using AVX2, up to eight floating point operations can be executed per cycle per core, potentially **doubling the performance** relative to non-AVX2 processors running at the same clock speed. Note that AVX2 support is not enabled by default and compiler flags must be set as described below.

### GPU Nodes

Expanse GPU nodes have GNU, Intel, and PGI compilers available along with multiple MPI implementations \(OpenMPI, IntelMPI, and MVAPICH2\). The gcc/10.2.0, Intel, and PGI compilers have specific flags for the Cascade Lake architecture. Users should evaluate their application for best compiler and library selections.

login nodes are not the same as the GPU nodes, therefore all GPU codes must be compiled by requesting an interactive session on the GPU nodes.

## Examples

We include several hands-on examples that cover many of the cases in the table:






