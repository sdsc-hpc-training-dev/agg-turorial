Contents:
* [Introduction](#main)
* [Expanse 101](#expanse-101)
  * [Getting Started](#getting-started)
    * [Account Access](#account-access)
    * [Environment Modules](#environment-modules)
  * [Compilers](#compilers)
    * [AMD](#amd)
    * [Intel](#intel)
    * [PGI](#pgi)
    * [GNU](#gnu)
  * [Running Jobs](#running-jobs)
    * [Slurm Resource Manager](#slurm-resource-manager)
    * [CPU Jobs](#cpu-jobs)
      * [Hello MPI](#hello-mpi)
      * [Hello OpenMP](#hello-openmp)
      * [Hello Hybrid](#hello-hybrid)
    * [GPU Jobs](#gpu-jobs)
      * [Hello CUDA](#hello-cuda)
      * [Hello OpenACC](#hello-openacc)
# Introduction
<a name="main"></a>
[SDSC HPC Training Group](https://www.sdsc.edu/education_and_training/training_hpc.html)

---
<a name="expanse-101"></a>description: Introduction to Running Jobs on the Expanse Supercomputer
---

# Expanse 101

## Prerequisite

* You must have a expanse account in order to access the system.
* You must be familiar with running [basic Unix commands](https://github.com/sdsc-hpc-training/basic_skills)

## Notes

* The `hostname` for Expanse is `expanse.sdsc.edu`
* The operating system for Expanse is CentOS
* For information on moving files from Comet to Expanse, see the [Comet to Expanse](https://education.sdsc.edu/training/interactive/202010_comet_to_expanse/index.html)

  [Transition Workshop](https://education.sdsc.edu/training/interactive/202010_comet_to_expanse/index.html)

#### In this tutorial, you will learn how to compile and run jobs on Expanse, where to run them, and how to run batch jobs. The commands below can be cut & pasted into the terminal window, when it is connected to expanse.sdsc.edu.


---
<a name="getting-started"></a>description: Hello world
---

## Getting Started

![Expanse Overview](../../.gitbook/assets/expanse_overview.png)



### HPC for the _long tail_ of science

* Designed by Dell and SDSC delivering 5.16 peak petaflops
* Designed and operated on the principle that the majority of computational research is performed at modest scale: large number jobs that run for less than 48 hours, but can be computationally intensvie and generate large amounts of data.
* An NSF-funded system available through the eXtreme Science and Engineering Discovery Environment \([XSEDE](https://www.xsede.org)\) program.
* Supports interactive computing and science gateways.
* Will offer Composible Systems and Cloud Bursting.

![Expanse Heterogeneous Architecture](../../.gitbook/assets/expanse_heterogeneous_arch.png)



### System Summary

* 13 SDSC Scalable Compute Units \(SSCU\)
* 728 x 2s Standard Compute Nodes
* 93,184 Compute Cores
* 200 TB DDR4 Memory
* 52x 4-way GPU Nodes w/NVLINK
* 208 V100s \| \* 4x 2TB Large Memory Nodes
* HDR 100 non-blocking Fabric
* Storage
  * 12 PB Lustre High Performance
  * 7 PB Ceph Object Storage
  * 1.2 PB on-node NVMe
* Dell EMC PowerEdge
* Direct Liquid Cooled

#### Expanse Scaleable Compute Unit

![](../../.gitbook/assets/expanse_sccu.png)

#### Expanse Connectivity Fabric

![](../../.gitbook/assets/expanse_connectivity_fabric.png)

#### AMD EPYC 7742 Processor Architecture

![](../../.gitbook/assets/amd-epyc-7742-processor-arch.png)

* 8 Core Complex Dies \(CCDs\).
* CCDs connect to memory, I/O, and each other through the I/O Die.
* 8 memory channels per socket.
* DDR4 memory at 3200MHz.
* PCI Gen4, up to 128 lanes of high speed I/O.
* Memory and I/O can be abstracted into separate quadrants each with 2 DIMM channels and 32 I/O lanes.
* 2 Core Complexes \(CCXs\) per CCD
* 4 Zen2 cores in each CCX share a16ML3 cache. Total of 16x16=256MB L3 cache.
* Each core includes a private 512KB L2 cache.  

### New Features

#### Composable Systems

![](../../.gitbook/assets/expanse_composable_systems.png)

##### Composable Systems will support complex, distributed, workflows � making Expanse part of a larger CI ecosystem

* Bright Cluster Manager + Kubernetes
* Core components developed via NSF- funded CHASE-CI \(NSF Award \# 1730158\), and the Pacific Research Platform \(NSF Award \# 1541349\)
* Requests for a composable system will be part of an XRAC request
* Advanced User Support resources available to assist with projects - this is part of our operations funding.

[Webinar scheduled for April 2021](https://www.sdsc.edu/education_and_training/training_hpc.html)

#### Cloud Bursting

![](../../.gitbook/assets/expanse_cloud_burst_aws.png)

##### Expanse will support integration with public clouds

* Supports projects that share data, need access to novel technologies, and integrate cloud resources into workflows
* Slurm + in-house developed software + Terraform \(Hashicorp\)
* Early work funded internally and via NSF E-CAS/Internet2 project for CIPRES \(Exploring Cloud for the Acceleration of Science, Award \#1904444\)
* Approach is cloud-agnostic and will support the major cloud providers
* Users submit directly via Slurm, or as part of a composed system
* Options for data movement: data in the cloud; remote mounting of file systems; cached filesystems \(e.g., StashCache\), and data transfer during the job
* Funding for users cloud resources is not part of an Expanse award: the researcher must have access to cloud computing credits via other NSF awards and funding


### Account Access
<a name="account-access"></a>
#### Logging Onto Expanse

Expanse supports Single Sign-On through the [XSEDE User Portal](https://portal.xsede.org), from the command line using an XSEDE-wide password \(coming soon, the Expanse User Portal\). While CPU and GPU resources are allocated separately, the login nodes are the same. To log in to Expanse from the command line, use the hostname `login.expanse.sdsc.edu`

The following Secure Shell \(ssh\) command may be used to log in to Expanse

```text
ssh <your_user>@login.expanse.sdsc.edu
```

Details about how to access Expanse under different circumstances are described in the [Expanse User Guide](https://www.sdsc.edu/support/user_guides/expanse.html#access)

For instructions on how to use SSH, see [Connecting to SDSC HPC Systems Guide](https://github.com/sdsc-hpc-training-org/hpc-security). Below is the logon message � often called the _MOTD_ \(message of the day, located in /etc/motd\). This has not been implemented at this point on Expanse.

```text
[user@localhost:~] ssh -Y expanse.sdsc.edu
Welcome to Bright release         9.0

                                                        Based on CentOS Linux 8
                                                                    ID: #000002

--------------------------------------------------------------------------------

                                 WELCOME TO
                  _______  __ ____  ___    _   _______ ______
                 / ____/ |/ // __ \/   |  / | / / ___// ____/
                / __/  |   // /_/ / /| | /  |/ /\__ \/ __/
               / /___ /   |/ ____/ ___ |/ /|  /___/ / /___
              /_____//_/|_/_/   /_/  |_/_/ |_//____/_____/

--------------------------------------------------------------------------------

Use the following commands to adjust your environment:

'module avail'            - show available modules
'module add <module>'     - adds a module to your environment for this session
'module initadd <module>' - configure module to be loaded at every login

-------------------------------------------------------------------------------
Last login: Fri Nov 1 11:16:02 2020 from x.x.x.x
```

###### Example of a terminal connection/Unix login session

```text
localhost:~ user$ ssh -l user login.expanse.sdsc.edu
Last login: Wed Oct  7 11:04:17 2020 from 76.176.117.51
[user@login02 ~]$
[user@login02 ~]$ whoami
user
[user@login02 ~]$ hostname
login01
[user@login02 ~]$ pwd
/home/user
[user@login02 ~]$
```

#### Obtaining Tutorial Example Code

We will clone the example code from [this repository](https://github.com/sdsc-hpc-training-org/expanse-101)

You can create a test directory to hold the expanse example files \(optional\)

The example below will be for anonymous HTTPS downloads

```text
[user@login01 TEMP]$ git clone https://github.com/sdsc-hpc-training-org/expanse-101.git
Cloning into 'expanse-101'...
remote: Enumerating objects: 275, done.
remote: Counting objects: 100% (275/275), done.
remote: Compressing objects: 100% (217/217), done.
remote: Total 784 (delta 163), reused 122 (delta 55), pack-reused 509
Receiving objects: 100% (784/784), 12.98 MiB | 20.92 MiB/s, done.
Resolving deltas: 100% (434/434), done.
Checking out files: 100% (56/56), done.
[user@login01 TEMP]$ cd expanse-101/
[user@login01 expanse-101]$ ll
total 8784
drwxr-xr-x 6 user abc123       11 Jan 28 22:39 .
drwxr-xr-x 3 user abc123        3 Jan 28 22:39 ..
-rw-r--r-- 1 user abc123     6148 Jan 28 22:39 .DS_Store
drwxr-xr-x 8 user abc123       8 Jan 28 22:39 examples
-rw-r--r-- 1 user abc123    76883 Jan 28 22:39 Expanse_Aggregate.md
drwxr-xr-x 8 user abc123       13 Jan 28 22:39 .git
-rw-r--r-- 1 user abc123      457 Jan 28 22:39 .gitignore
drwxr-xr-x 2 user abc123       16 Jan 28 22:39 images
-rw-r--r-- 1 user abc123     3053 Jan 28 22:39 README.md
```

#### [Expanse User Portal](https://portal.expanse.sdsc.edu)

* Quick and easy way for Expanse users to login, transfer and edit files and submit and monitor jobs.
* Gateway for launching interactive applications such as MATLAB, Rstudio
* Integrated web-based environment for file management and job submission
* All Users with valid Expanse Allocation and XSEDE Based credentials have access via their XSEDE credentials

#### Expanse-Client Script

* The expanse-client script provides additional details regarding User and Project availability and usage located at

```text
/cm/shared/apps/sdsc/current/bin/expanse-client
```

Use command `module load sdsc`to load`expanse-client`into environment

* **Example of Script Usage**

```text
[user@login01 ~]$ expanse-client -h
Allows querying the user statistics.

Usage:
  expanse-client [command]

Available Commands:
  help        Help about any command
  project     Get project information
  user        Get user information

Flags:
  -a, --auth      authenticate the request
  -h, --help      help for expanse-client
  -p, --plain     plain no graphics output
  -v, --verbose   verbose output

Use "expanse-client [command] --help" for more information about a command.
```

* Example of using the script shows that the user has allocations on 3 accounts, and SU's remaining:

```text
[user@login01 ~]$ expanse-client user -p

 Resource  sdsc_expanse

 NAME     PROJECT  USED  AVAILABLE  USED BY PROJECT
----------------------------------------------------
 user  abc123     33      80000              180
 user  srt456      0       5000               79
 user  xyz789    318     500000          2905439
```

* To see who is on an account:

```text
[user@login01]$  expanse-client project abc123 -p

 Resource          sdsc_expanse    
 Project           xyz789         
 Total allocation  500000         
 Total recorded    289243         
 Total queued      13004           
 Expiration        January 1, 2024

 NAME          USED  AVAILABLE  USED BY PROJECT
------------------------------------------------
 user1            0     500000           289243
 user2         6624     500000           289243
 user3           33     500000           289243
 user4           14     500000           289243
```

#### Using Accounts in Batch Jobs

As with the case above, some users will have access to multiple accounts \(e.g. an allocation for a research project and a separate allocation for classroom or educational use\). Users should verify that the correct project is designated for all batch jobs. Awards are granted for a specific purposes and should not be used for other projects. Designate a project by replacing &lt;&lt; project &gt;&gt; with a project listed as above in the SBATCH directive in your job script:

```text
  #SBATCH -A <project>
```

#### Managing Users on an Account

Only project PIs and co-PIs can add or remove users from an account. This can only be done via the [XSEDE portal](https://portal.xsede.org) account \(there is no command line interface for this\). After logging in, go to the Add User page for the account.

#### Job Charging

The basic charge unit for all SDSC machines, including Expanse, is the Service Unit \(SU\). This corresponds to:

* Use of one compute core utilizing less than or equal to 2G of data for one hour
* 1 GPU using less than 96G of data for 1 hour.

  Note: your charges are based on the resources that are tied up by your job and don't necessarily reflect how the resources are used. Charges are based on either the number of cores or the fraction of the memory requested, whichever is larger. The minimum charge for any job is 1 SU.

See the [Expanse User Guide](https://www.sdsc.edu/support/user_guides/expanse.html#charging) for more details and factors that affect job charging.


---
<a name="environment-modules"></a>description: Customizing Your User Environment
---

### Environment Modules

The Environment Modules package provides for dynamic modification of your shell environment. Module commands set, change, or delete environment variables, typically in support of a particular application. They also let the user choose between different versions of the same software or different combinations of related codes. See the [Expanse User Guide](https://www.sdsc.edu/support/user_guides/expanse.html#modules).

#### Introduction to Lmod

Expanse uses [Lmod](https://lmod.readthedocs.io/en/latest/010_user.html), a Lua based module system. Users setup custom environments by loading available modules into the shell environment, including needed compilers and libraries and the batch scheduler.

##### What's the same as Comet:

* Dynamic modification of your shell environment
* User can set, change, or delete environment variables
* User chooses between different versions of the same software or different combinations of related codes.

##### What's Different?

* Users will need to load the scheduler \(e.g. Slurm\)
* Depending on which hardware users are working on, users will need to load either the `gpu` or `cpu` modules.
* Users will not see all available modules when they run command "module available" without loading a compiler.
* Use the command "module spider" option to see if a particular package exists and can be loaded, run command
  * `module spider`
  * `module keywords`
* For additional details, and to identify module dependencies modules, use the command
  * `module spider`
* The module paths are different for the CPU and GPU nodes. Users can enable the paths by loading the following modules:            
  * `module load cpu`  \(for cpu nodes\)
  * `module load gpu`  \(for gpu nodes\)     

###### Avoid loading both modules

#### Popular Lmod Commands

Here are some common module commands and their descriptions

| Lmod Command | Description |
| :--- | :--- |
| `module purge` | Remove all modules that are currently loaded |
| `module list` | List the modules that are currently loaded |
| `module avail` | List the modules that are available in environment |
| `module spider` | List of the modules and extensions currently available |
| `module display` | Show the environment variables used by  and how they are affected |
| `module unload` | Remove  from the environment |
| `module load` | Load  into the environment |
| `module swap` | Replace  with  in the environment |
| `module save` | Save the current list of modules to "name" collection. |
| `module savelist` | List of saved module collections. |
| `module describe` | Describe the contents of a module collection. |
| `module help` | Get a list of all the commands that module knows about do: |

Lmod commands support _short-hand_ notation, for example:

`ml foo` == `module load foo`

`foo ml -bar` == `module unload bar`

SDSC Guidance: add module calls to your environment and batch scripts

###### Examples

* Default environment for a new user/new login: `list`, `li`

```text
(base) [user@login01 expanse-101]$ module list
Currently Loaded Modules:
1) shared   2) slurm/expanse/20.02.3   3) cpu/0.15.4   4) DefaultModules
```

* List available modules:  `available`, `avail`, `av`

```text
$ module av
[user@expanse-ln3:~] module av
(base) [user@login01 expanse-101]$ module available

--------------- /cm/shared/apps/spack/cpu/lmod/linux-centos8-x86_64/Core ----------------
   abaqus/2018     gaussian/16.C.01        gmp/6.1.2           mpfr/4.0.2
   aocc/2.2.0      gcc/7.5.0               intel/19.1.1.217    openjdk/11.0.2
   cmake/3.18.2    gcc/9.2.0               libtirpc/1.2.6      parallel/20200822
   emboss/6.6.0    gcc/10.2.0       (D)    matlab/2020b        subversion/1.14.0

--------------------------------- /cm/local/modulefiles ---------------------------------
   cluster-tools-dell/9.0        gcc/9.2.0                    null
   cluster-tools/9.0             gpu/1.0                      openldap
   cmd                           ipmitool/1.8.18              python3
   cmjob                         kubernetes/expanse/1.18.8    python37
   cpu/1.0                (L)    lua/5.3.5                    shared                (L)
   docker/19.03.5                luajit                       singularitypro/3.5
   dot                           module-git                   slurm/expanse/20.02.3
   freeipmi/1.6.4                module-info

-------------------------------- /usr/share/modulefiles ---------------------------------
   DefaultModules (L)    gct/6.2    globus/6.0

-------------------------------- /cm/shared/modulefiles ---------------------------------
   bonnie++/1.98                default-environment           netperf/2.7.0
   cm-pmix3/3.1.4               gdb/8.3.1                     openblas/dynamic/0.3.7
   cuda10.2/blas/10.2.89        hdf5/1.10.1                   openmpi/gcc/64/1.10.7
   cuda10.2/fft/10.2.89         hdf5_18/1.8.21                sdsc/1.0
   cuda10.2/nsight/10.2.89      hwloc/1.11.11                 ucx/1.6.1
   cuda10.2/profiler/10.2.89    iozone/3_487
   cuda10.2/toolkit/10.2.89     netcdf/gcc/64/gcc/64/4.7.3

  Where:
   L:  Module is loaded
   D:  Default Module
```

Module defaults are chosen based on Find First Rules due to Name/Version/Version modules found in the module tree. See [https://lmod.readthedocs.io/en/latest/060\_locating.html](https://lmod.readthedocs.io/en/latest/060_locating.html) for details.

Use `module spider` to find all possible modules and extensions.

```text
(base) [user@login02 ~]$ module spider MPI
-------------------------------------------------------------------------------------
  intel-mpi: intel-mpi/2019.8.254
-------------------------------------------------------------------------------------
    You will need to load the set of module(s) on any one of the lines below before the "intel-mpi/2019.8.254" module is available to load.

      cpu/1.0  gcc/10.2.0
      cpu/1.0  intel/19.1.1.217
      gpu/1.0
      gpu/1.0  intel/19.0.5.281
      gpu/1.0  pgi/20.4

    Help:
      Intel MPI
-------------------------------------------------------------------------------------
  openmpi:
-------------------------------------------------------------------------------------
     Versions:
        openmpi/3.1.6
        openmpi/4.0.4-nocuda
        openmpi/4.0.4
-------------------------------------------------------------------------------------
  For detailed information about a specific "openmpi" package (including how to load the modules) use the module's full name. Note that names that have a trailing (E) are extensions provided by other modules.
  For example:

     $ module spider openmpi/4.0.4
-------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------
  openmpi/gcc/64: openmpi/gcc/64/1.10.7
-------------------------------------------------------------------------------------
    You will need to load all module(s) on any one of the lines below before the "openmpi/gcc/64/1.10.7" module is available to load.
      shared
    Help:
        Adds OpenMPI to your environment variables,
```

#### Environment Checking

In this example, we will add the Slurm library, and and verify that it is in your environment

* Check module environment after loggin on to the system:

```text
(base) [user@login01 ~]$ module li

Currently Loaded Modules:
  1) shared   2) slurm/expanse/20.02.3   3) cpu/0.15.4   4) DefaultModules
```

* Note that Slurm \(the cluster resource manager\) is not in the environment.

  Check environment looking for Slurm commands

```text
(base) [user@login01 ~]$ which squeue
/usr/bin/which: no squeue in (/home/user/miniconda3/bin/conda:/home/user/miniconda3/bin:/home/user/miniconda3/condabin:/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/opt/dell/srvadmin/bin:/home/user/.local/bin:/home/user/bin)
```

* Since Slurm commands do not exist,  we need to load that module:

```text
(base) [user@login01 ~]$ module load slurm
(base) [user@login01 ~]$ which squeue
/cm/shared/apps/Slurm/current/bin/squeue
```

* Display loaded module details:

```text
(base) [user@login02 ~]$ module display Slurm
-------------------------------------------------------------------------------------
   /cm/local/modulefiles/slurm/expanse/20.02.3:
-------------------------------------------------------------------------------------
whatis("Adds Slurm to your environment ")
setenv("CMD_WLM_CLUSTER_NAME","expanse")
setenv("Slurm_CONF","/cm/shared/apps/Slurm/var/etc/expanse/Slurm.conf")
prepend_path("PATH","/cm/shared/apps/Slurm/current/bin")
prepend_path("PATH","/cm/shared/apps/Slurm/current/sbin")
prepend_path("MANPATH","/cm/shared/apps/Slurm/current/man")
prepend_path("LD_LIBRARY_PATH","/cm/shared/apps/Slurm/current/lib64")
prepend_path("LD_LIBRARY_PATH","/cm/shared/apps/Slurm/current/lib64/Slurm")
prepend_path("LIBRARY_PATH","/cm/shared/apps/Slurm/current/lib64")
prepend_path("LIBRARY_PATH","/cm/shared/apps/Slurm/current/lib64/Slurm")
prepend_path("CPATH","/cm/shared/apps/Slurm/current/include")
help([[ Adds Slurm to your environment
]])
```

Once you have loaded the modules, you can check the system variables that are available for you to use.

* To see all variable, run the **`env`** command. Typically, you will see more than 60 lines containing information such as your login name, shell, your home directory:

```text
[user@expanse-ln3 IBRUN]$ env
CONDA_EXE=/home/user/miniconda3/bin/conda
__LMOD_REF_COUNT_PATH=/cm/shared/apps/Slurm/current/sbin:1;/cm/shared/apps/Slurm/current/bin:1;/home/user/miniconda3/bin/conda:1;/home/user/miniconda3/bin:1;/home/user/miniconda3/condabin:1;/usr/local/bin:1;/usr/bin:1;/usr/local/sbin:1;/usr/sbin:1;/opt/dell/srvadmin/bin:1;/home/user/.local/bin:1;/home/user/bin:1
HOSTNAME=login02
USER=user
HOME=/home/user
CONDA_PYTHON_EXE=/home/user/miniconda3/bin/python
BASH_ENV=/usr/share/lmod/lmod/init/bash
BASHRC_READ=1
LIBRARY_PATH=/cm/shared/apps/Slurm/current/lib64/Slurm:/cm/shared/apps/Slurm/current/lib64
Slurm_CONF=/cm/shared/apps/Slurm/var/etc/expanse/Slurm.conf
LOADEDMODULES=shared:cpu/1.0:DefaultModules:slurm/expanse/20.02.3
__LMOD_REF_COUNT_MANPATH=/cm/shared/apps/Slurm/current/man:1;/usr/share/lmod/lmod/share/man:1;/usr/local/. . . .
MANPATH=/cm/shared/apps/Slurm/current/man:/usr/share/lmod/lmod/share/man:/usr/local/share/man:/usr/share/man:/cm/local/apps/environment-modules/current/share/man
MODULEPATH=/cm/shared/apps/spack/cpu/lmod/linux-centos8-x86_64/Core:/cm/local/modulefiles:/etc/modulefiles:/usr/share/modulefiles:/usr/share/Modules/modulefiles:/cm/shared/modulefiles
MODULEPATH_ROOT=/usr/share/modulefiles
PATH=/cm/shared/apps/Slurm/current/sbin:/cm/shared/apps/Slurm/current/bin:/home/user/miniconda3/bin/conda:/home/user/miniconda3/bin:/home/user/miniconda3/condabin:/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/opt/dell/srvadmin/bin:/home/user/.local/bin:/home/user/bin
_LMFILES_=/cm/local/modulefiles/shared:/cm/local/modulefiles/cpu/1.0.lua:/usr/share/modulefiles/DefaultModules.lua:/cm/local/modulefiles/slurm/expanse/20.02.3
MODULESHOME=/usr/share/lmod/lmod
CONDA_DEFAULT_ENV=base
```

To see the value for any of these variables, use the `echo` command. In this example we show how to activate your miniconda environment so you can run Jupyter Notebooks:

```text
(base) [user@login02 ~]$ echo $CONDA_PYTHON_EXE
[user@login02 ~]$
[user@login02 ~]$ conda activate
-bash: conda: command not found
[user@login02 ~]$ . /home/$USER/miniconda3/etc/profile.d/conda.sh
[user@login02 ~]$ conda activate
(base) [user@login02 ~]$ which jupyter
~/miniconda3/bin/jupyter
(base) [user@login02 ~]$ echo $CONDA_PYTHON_EXE
/home/user/miniconda3/bin/python
(base) [user@login02 ~]$
```

#### Loading Modules at Login

You can override, and add to the standard set of login modules in two ways. 

1. Adding module commands to your personal startup files
2. Using `module save` command

Make sure that you always want the module loaded at login

For Bash: put the following block into your `~/.bash_profile` file:

```bash
if [ -f ~/.bashrc ]; then
       . ~/.bashrc
fi
```

Place the following in your `~/.bashrc` file:

```text
### Place module commands here
### module load hdf5
```

* First edit your `.bashrc` and `.bash_profile` files:

```text
[user@login02 ~]$ cat .bash_profile
### .bash_profile
### Get the aliases and functions
if [ -f ~/.bashrc ]; then
. ~/.bashrc
fi
[SNIP]
[user@login01 ~]$
[user@login02 ~]$ cat .bashrc
### .bashrc
### Source global definitions
if [ -f /etc/bashrc ]; then
. /etc/bashrc
fi

### Place any module commands here
module load hdf5

[SNIP]
```

* Next LOGOUT and LOG BACK IN:

```text
(base) [user@login02 ~]$ env | grep Slurm
[snip]
MANPATH=/cm/shared/apps/Slurm/current/man:/usr/share/lmod/lmod/share/man:/usr/local/share/man:/usr/share/man:/cm/local/apps/environment-modules/current/share/man
PATH=/cm/shared/apps/Slurm/current/sbin:/cm/shared/apps/Slurm/current/bin:/home/user/miniconda3/bin/conda:/home/user/miniconda3/bin:/home/user/miniconda3/condabin:/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/opt/dell/srvadmin/bin:/home/user/.local/bin:/home/user/bin
[snip]
(base) [user@login02 ~]$ which squeue
/cm/shared/apps/Slurm/current/bin/squeue
```

#### Troubleshooting

##### Lmod warning "rebuild your saved collection"

Lmod allows a user to save a bundle of modules as a collection using module save and module restore. This enables you to quickly get the same list of modules loaded if you tend to use the same modules over and over. With a new module scheme came a different system MODULEPATH. For this reason, if you have some module collections saved, you will experience the following warning: �Lmod Warning: The system MODULEPATH has changed: please rebuild your saved collection.� To solve this you need to remove your old collections and create them again.

* Too see the list of module collections that you currently have:

```text
[mthomas@login02 ~]$ module savelist
Named collection list :
  1) default  2) hdf5_env
```

* To remove or disable a saved collection:

```text
[mthomas@login02 ~]$ module disable hdf5_env
Disabling hdf5_env collection by renaming with a "~"
[mthomas@login02 ~]$ module savelist
Named collection list :
  1) default
[mthomas@login02 ~]$
```

##### Module Error

Sometimes this error is encountered when switching from one shell to another or attempting to run the module command from within a shell script or batch job. The module command may not be inherited between the shells. To keep this from happening, execute the following command:

```text
[expanse-ln3:~]source /etc/profile.d/modules.sh
```

OR add this command to your shell script \(including Slurm batch scripts\)


## Compilers
<a name="compilers"></a>
Expanse provides the Intel, Portland Group \(PGI\), and GNU compilers along with multiple MPI implementations \(MVAPICH2, MPICH2, OpenMPI\). Most applications will achieve the best performance on Expanse using the Intel compilers and MVAPICH2 and the majority of libraries installed on Expanse have been built using this combination. Having such a diverse set of compilers avaiable allows for our users to customize the software stack need for their application. However, there can be some complexity involved in sorting out the module dependencies needed for your applications. Often the set of modules being loaded depends on the application you are using and the compiler and libraries you may need. In many cases you will need to use the `module spider` command to sort out what modules your application will need. Additionally, it is possible the list will change if some of the dependent software changes.

Other compilers and versions can be installed by Expanse staff on request. More information at [Expanse User Guide](https://www.sdsc.edu/support/user_guides/expanse.html#compiling)

### Supported Compilers

#### CPU Nodes

* GNU, Intel, AOCC \(AMD\) compilers
* Multiple MPI implementations \(OpenMPI, MVAPICH2, and IntelMPI\).
* A majority of applications have been built using gcc/10.2.0 which features AMD Rome specific optimization flags \(-march=znver2\).
* Intel, and AOCC compilers all have flags to support Advanced Vector Extensions 2 \(AVX2\).

Users should evaluate their application for best compiler and library selection. GNU, Intel, and AOCC compilers all have flags to support Advanced Vector Extensions 2 \(AVX2\). Using AVX2, up to eight floating point operations can be executed per cycle per core, potentially **doubling the performance** relative to non-AVX2 processors running at the same clock speed. Note that AVX2 support is not enabled by default and compiler flags must be set as described below.

#### GPU Nodes

Expanse GPU nodes have GNU, Intel, and PGI compilers available along with multiple MPI implementations \(OpenMPI, IntelMPI, and MVAPICH2\). The gcc/10.2.0, Intel, and PGI compilers have specific flags for the Cascade Lake architecture. Users should evaluate their application for best compiler and library selections.

login nodes are not the same as the GPU nodes, therefore all GPU codes must be compiled by requesting an interactive session on the GPU nodes.

### Examples

We include several hands-on examples that cover many of the cases in the table:







---
<a name="amd"></a>description: AMD Optimizing C/C++ Compiler (AOCC)
---

### AMD

The AMD Optimizing C/C++ Compiler \(AOCC\) is only available on CPU nodes. AMD compilers can be loaded by executing the following commands at the Linux prompt:

```text
module load aocc
```

For more information on the AMD compilers run \[flang \| clang \] -help

#### Suggested Compilers

| Language | Serial | MPI | OpenMP | MPI + OpenMP |
| :--- | :--- | :--- | :--- | :--- |
| Fortran | flang | mpif90 | ifort -fopenmp | mpif90 -fopenmp |
| C | clang | mpiclang | icc -fopenmp | mpicc -fopenmp |
| C++ | clang++ | mpiclang | icpc -fopenmp | mpicxx -fopenmp |


---
<a name="intel"></a>description: Intel Compilers
---

### Intel

The Intel compilers and the MVAPICH2 MPI implementation will be loaded by default. The MKL and related libraries may need several modules. If you have modified your environment, you can reload by executing the following commands such as those shown below at the Linux prompt or placing in your startup file \(~/.cshrc or ~/.bashrc\). Below is the list of modules created for the DGEMM MKL example described below \(on 01/25/21\):

```text
module purge
module load slurm
module load cpu
module load gpu/0.15.4  
module load intel/19.0.5.281
module load intel-mkl/2020.3.279
```

For more information on the Intel compilers run: \[ifort \| icc \| icpc\] -help

#### Suggested Compilers

| Language | Serial | MPI | OpenMP | MPI + OpenMP |
| :--- | :--- | :--- | :--- | :--- |
| Fortran | ifort | mpif90 | mpif90 -fopenmp | mpif90 -qopenmp |
| C | icc | mpicc | icc -qopenmp | mpicc -qopenmp |
| C++ | icpc | mpicxx | icpc -qopenmp | mpicxx -qopenmp |

For AVX2 support, compile with the -xHOST option. Note that -xHOST alone does not enable aggressive optimization, so compilation with -O3 is also suggested. The -fast flag invokes -xHOST, but should be avoided since it also turns on interprocedural optimization \(-ipo\), which may cause problems in some instances.


---
<a name="pgi"></a>description: PGI Compilers
---

### PGI

The PGI compilers can be loaded by executing the following commands at the Linux prompt or placing in your startup file \(~/.cshrc or ~/.bashrc\)

```text
module purge
module load pgi mvapich2_ib
```

For more information on the PGI compilers: man \[pgf90 \| pgcc \| pgCC\]

#### Suggested Compilers

| Language | Serial | MPI | OpenMP | MPI+OpenMP |
| :--- | :--- | :--- | :--- | :--- |
| Fortran | pgf90 | mpif90 | mpif90 -mp | mpif90 -mp |
| C | pgcc | mpicc | pgcc -mp | mpicc -mp |
| C++ | pgCC | mpicxx | pgCC -mp | mpicxx -mp |

 For AVX support, compile with `-fast`


---
<a name="gnu"></a>description: GNU Compilers
---

### GNU

The GNU compilers can be loaded by executing the following commands at the Linux prompt or placing in your startup files \(~/.cshrc or ~/.bashrc\)

```text
module purge
module load gnu openmpi_ib
```

For more information on the GNU compilers: man \[gfortran \| gcc \| g++\]

#### Suggested Compilers

| Language | Serial | MPI | OpenMP | MPI+OpenMP |
| :--- | :--- | :--- | :--- | :--- |
| Fortran | gfortran | mpif90 | gfortran -fopenmp | mpif90 -fopenmp |
| C | gcc | mpicc | gcc -fopenmp | mpicc -fopenmp |
| C++ | g++ | mpicxx | g++ -fopenmp | mpicxx -fopenmp |

For AVX support, compile with -mavx. Note that AVX support is only available in version 4.7 or later, so it is necessary to explicitly load the gnu/4.9.2 module until such time that it becomes the default




## Running Jobs
<a name="running-jobs"></a>
### Parallel Models

#### Distributed Memory

![](../../.gitbook/assets/distr-memory.png)

* Programs that run asynchronously, pass messages for communication and coordination between resources.
* Examples include: SOA-based systems, massively multiplayer online games, peer-to-peer apps.
* Different types of implementations for the message passing mechanism: HTTP, RPC-like connectors, message queues
* HPC historically uses the Message Passing Interface \(MPI\)

#### Shared Memory

![](../../.gitbook/assets/shared-memory.png)

* CPUs all share same localized memory \(SHMEM\)
  * Coordination and communication between tasks via interprocessor communication \(IPC\) or virtual memory mappings.
* May use: uniform or non-uniform memory access \(UMA or NUMA\); cache-only memory architecture \(COMA\).
* Most common HPC API�s for using SHMEM:
  * Portable Operating System Interface \(POSIX\); Open Multi-Processing \(OpenMP\) designed for parallel computing � best for multi-core computing.

### Methods for Running Jobs

#### Batch Jobs

* Batch Jobs are used to submit batch scripts to Slurm from the login nodes. You need to specify
  * Partition \(queue\)
  * Time limit for the run \(maximum of 48 hours\)
  * Number of nodes, tasks per node; Memory requirements \(if any\)
  * Job name, output file location; Email info, configuration
* When you run in the batch mode, you submit jobs to be run on the compute nodes using the sbatch command.
* Remember that computationally intensive jobs should be run only on the compute nodes and not the login nodes.
* Expanse places limits on the number of jobs queued and running on a per group \(allocation\) and partition basis.
* Please note that submitting a large number of jobs \(especially very short ones\) can impact the overall  scheduler response for all users.

#### Interactive Jobs

Use the [`srun`](slurm-resource-manager.md#common-commands)command to obtain nodes for real-time command line access to a compute node:

`CPU`
```text
srun --partition=debug --qos=debug-normal --pty --account=abc123 \
     --nodes=1 --ntasks-per-node=128 --mem=248 -t 00:30:00 --wait=0 \
     --export=ALL /bin/bash
```

`GPU`
```
srun --pty --account=abc123 --nodes=1 --ntasks-per-node=1 \
     --cpus-per-task=10  -p gpu-debug --gpus=1  \
     -t 00:10:00 /bin/bash
```

#### Command Line Jobs

The login nodes are meant for compilation, file editing, simple data analysis, and other tasks that use minimal compute resources. **Do not run parallel or large jobs on the login nodes** _-_ even for simple tests. Even if you could run a simple test on the command line on the login node, full tests should not be run on the login node because the performance will be adversely impacted by all the other tasks and login activities of the other users who are logged onto the same node. For example, at the moment that this note was written, a `gzip` process was consuming 98% of the CPU time on the Comet HPC system:

```text
    [user@comet-ln3 OPENMP]$ top
    ...
      PID USER      PR  NI  VIRT  RES  SHR S %CPU %MEM    TIME+  COMMAND
    19937 XXXXX     20   0  4304  680  300 R 98.2  0.0   0:19.45 gzip
```

Commands that you type into the terminal and run on the sytem are considered _jobs_ and they consume resources.

Computationally intensive jobs should be run only on the compute nodes and not the login nodes


### Slurm Resource Manager
<a name="slurm-resource-manager"></a>
#### Overview

Expanse uses the _Simple Linux Utility for Resource Management_ \(Slurm\) resource manager. Slurm is an open source, fault-tolerant, and highly scalable cluster management and job scheduling system for large and small Linux clusters. Follow this link to the [Slurm Quick Start Guide](https://Slurm.schedmd.com/quickstart.html)

| Expanse | Slurm |
| :---: | :---: |
| ![Login nodes to cluster diagram](../../.gitbook/assets/login-nodes-cluster-nodes.png) | ![Slurm Scheduler Architecture](../../.gitbook/assets/arch.gif) |
| User logs onto Expanse, and submits a batch script to the Slurm Controller daemon | Slurm parses the batch script for correct syntax and then queues up the job until the requested resources are available |

###### Slurm is the "Glue" for parallel computer to schedule and execute jobs

* Role: Allocate resources within a cluster
* Nodes \(unique IP address\)
* Interconnect/switches
* Generic resources \(e.g. GPUs\)
* Launch and otherwise manage jobs

#### Partitions

| Partition Name | Max Walltime | Max Nodes/ Job | Max Running Jobs | Max Running + Queued Jobs | Charge Factor | Comments |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| compute | 48 hrs | 32 | 32 | 64 | 1 | Used for exclusive access to regular compute nodes |
| shared | 48 hrs | 1 | 4096 | 4096 | 1 | Single-node jobs using fewer than 128 cores |
| gpu | 48 hrs | 4 | 4 | 8 \(32 Tres GPU\) | 1 | Used for exclusive access to the GPU nodes |
| gpu-shared | 48 hrs | 1 | 24 | 24 \(24 Tres GPU\) | 1 | Single-node job using fewer than 4 GPUs |
| large-shared | 48 hrs | 1 | 1 | 4 | 1 | Single-node jobs using large memory up to 2 TB \(minimum memory required 256G\) |
| debug | 30 min | 2 | 1 | 2 | 1 | Priority access to compute nodes set aside for testing of jobs with short walltime and limited resources |
| gpu-debug | 30 min | 2 | 1 | 2 | 1 | \*\* Priority access to gpu nodes set aside for testing of jobs with short walltime and limited resources |
| preempt | 7 days | 32 |  | 128 | 0.8 | Discounted jobs to run on free nodes that can be pre-empted by jobs submited to any other queue \(NO REFUNDS\) |
| gpu-preempt | 7 days | 1 |  | 24 \(24 Tres GPU\) | 0.8 | Discounted jobs to run on unallocated nodes that can be pre-empted by jobs submitted to higher priority queues \(NO REFUNDS\) |

#### Job State Codes

Slurm has a large number of states. The table below lists some of the most common states you will see. For full details, See the section on Slurm JOB STATE CODES, at the [Slurm Squeue data page](https://Slurm.schedmd.com/squeue.html).

| **STATE** | **LABEL** | **DESCRIPTION** |
| :--- | :--- | :--- |
| CA | CANCELLED | Job was explicitly cancelled by the user or system administrator. |
| C | COMPLETED | job is Complete/Clearing |
| F | FAILED | Job terminated with non-zero exit code or other failure condition. |
| PD | PENDING | Job is awaiting resource allocation. |
| R | RUNNING | Job currently has an allocation. |
| ST | STOPPED | Job has an allocation, but execution has been stopped with SIGSTOP signal. CPUS have been retained by this job. |
| TO | TIMEOUT | Job terminated upon reaching its time limit. |

#### Common Commands

Here are a few key Slurm commands. For more information, run the `man Slurm` or see this page:

| **COMMAND** | **DESCRIPTION** |
| :--- | :--- |
| `scancel` | Used to signal or cancel jobs, job arrays or job steps. |
| `sbatch` | Submit a batch script to Slurm. |
| `sinfo` | View information about Slurm nodes and partitions. |
| `squeue` | Used to view job and job step information for jobs managed by Slurm. |
| `srun` | Run a parallel job on cluster managed by Slurm. |

Submit jobs using the sbatch command:

```text
$ sbatch mycode-slurm.sb
```

Submitted batch job 8718049.

Check job status using the squeue command:

```text
$ squeue -u $USER
    JOBID PARTITION     NAME     USER   ST   TIME  NODES  NODELIST(REASON)
  8718049   compute       mycode user   PD   0:00      1        (Priority)
```

Once the job is running:

```text
$ squeue -u $USER
    JOBID PARTITION     NAME     USER    ST     TIME  NODES  NODELIST(REASON)
  8718049     debug   mycode     user     R     0:02      1    expanse-14-01
```

Cancel a running job:

```text
$ scancel 8718049
```

#### Example

Below is an example of a batch script that prints our your environment on the compute node:

`env-slurm.sb`
```bash
###!/bin/bash
###SBATCH --job-name="envinfo"
###SBATCH --output="envinfo.%j.%N.out"
###SBATCH --partition=compute
###SBATCH --nodes=1
###SBATCH --ntasks-per-node=1
###SBATCH --export=ALL
###SBATCH --account=abc123
###SBATCH -t 00:01:00

#### Environment
module purge
module load slurm
module load cpu
####� perform some basic unix commands
echo "----------------------------------"
echo "hostname= " `hostname`�
echo "date= " `date`�
echo "whoami= " `whoami`�
echo "pwd= " `pwd`�
echo "module list= " `module list`�
echo "----------------------------------"
echo "env= " `env`�
echo "----------------------------------"
```

`envinfo.108867.exp-6-56.out`
```bash
----------------------------------
hostname=� exp-6-56
date=� Wed Oct 7 23:45:43 PDT 2020
whoami=� user
pwd=� /home/user/DEMO/ENV_INFO
Currently Loaded Modules:
� 1) slurm/expanse/20.02.3 � 2) cpu/1.0
----------------------------------
env=� SLURM_MEM_PER_CPU=1024 LD_LIBRARY_PATH=/cm/shared/apps/Slurm/current...
[SNIP]
----------------------------------
```




### CPU Jobs
<a name="cpu-jobs"></a>
#### General Steps

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

#### Checking Environment

This simple batch script will show you how to check your user environment and to also verify that your Slurm environment is working.

`env-Slurm.sb`
```bash
###!/bin/bash
###SBATCH --job-name="envinfo"
###SBATCH --output="envinfo.%j.%N.out"
###SBATCH --partition=compute
###SBATCH --nodes=1
###SBATCH --ntasks-per-node=1
###SBATCH --export=ALL
###SBATCH -A sds173
###SBATCH -t 00:1:00

#### Load module environment
module purge
module load slurm
module load cpu
module load sdsc

####  perform some basic unix commands

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


---
<a name="hello-mpi"></a>description: >-
  Simple tutorial to compile and run a MPI hello world program on Expanse CPU
  node
---

#### Hello MPI

##### Code

`hello\_mpi.f90`
```text
!� Fortran example �
�� program hello
�� include 'mpif.h'
�� integer rank, size, ierror, tag, status(MPI_STATUS_SIZE)
� �
�� call MPI_INIT(ierror)
�� call MPI_COMM_SIZE(MPI_COMM_WORLD, size, ierror)
�� call MPI_COMM_RANK(MPI_COMM_WORLD, rank, ierror)
�� print*, 'node', rank, ': Hello world!'
�� call MPI_FINALIZE(ierror)
�� end
```

`mpi-slurm.sb`
```bash
####!/bin/bash
####SBATCH --job-name="hellompi"
####SBATCH --output="hellompi.%j.%N.out"
####SBATCH --partition=compute
#######SBATCH --partition=shared
####SBATCH --nodes=3
####SBATCH --ntasks-per-node=12
####SBATCH --export=ALL
####SBATCH -t 00:04:00
####SBATCH -A abc123

#### This job runs with 3 nodes, and a total of 12 cores.
##### Environment
###### MODULE ENV: updated 01/28/2020 (MPT)
module purge
module load slurm
module load cpu
module load gcc/10.2.0
module load openmpi/4.0.4

##### Use srun to run the job
srun --mpi=pmi2 -n 12 --cpu-bind=rank ./hello_mpi
```

In the batch script we are using the GNU compiler, and asking for 2 CPU compute nodes, with 128 tasks per node for a total of 256 tasks. The name of job is set in line 2, while the name of the output file is set in line 3, where "**%j**" is the Slurm JOB\_ID, and and "**%N**" is the compute node name. You can name your outupt file however you wish, but it helpful to keep track of the JOB\_ID and node info in case something goes wrong.

##### Compiling

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

##### Submission

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

##### Output

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


---
<a name="hello-openmp"></a>description: >-
  Simple tutorial to compile and run a OpenMP hello world program on Expanse CPU
  node
---

#### Hello OpenMP

##### Code

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
####!/bin/bash
##### Example of OpenMP code running on a shared node
####SBATCH --job-name="hell_openmp_shared"
####SBATCH --output="hello_openmp_shared.%j.%N.out"
####SBATCH --partition=shared
####SBATCH --nodes=1
####SBATCH --ntasks-per-node=1
####SBATCH --cpus-per-task=16
####SBATCH --mem=32G
####SBATCH --export=ALL
####SBATCH --account=sds173
####SBATCH -t 00:10:00

#### AOCC environment
module purge
module load slurm
module load cpu
module load aocc

####SET the number of openmp threads
export OMP_NUM_THREADS=16

####Run the openmp job
./hello_openmp
```

The script is loading the module stack, and setting the number of OMP threads

##### Compiling

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

##### Submission

```text
[user@login02 OPENMP]$ sbatch openmp-slurm.sb
Submitted batch job 1088802

[user@login02 OPENMP]$ squeue -u user
   JOBID PARTITION     NAME  USER ST  TIME  NODES NODELIST(REASON)
 1088802    shared hell_ope  user PD  0:00      1 (None)
[...]
```

##### Output

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


---
<a name="hello-hybrid"></a>description: >-
  Simple tutorial to compile and run a hybrid (MPI + OpenMP) hello world program
  on Expanse CPU node
---

#### Hello Hybrid

##### Code

`hybrid.c`
```c
####include <stdio.h>
####include "mpi.h"
####include <omp.h>

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
####!/bin/bash
####SBATCH --job-name="hellohybrid"
####SBATCH --output="hellohybrid.%j.%N.out"
####SBATCH --partition=shared
####SBATCH --nodes=1
####SBATCH --ntasks-per-node=2
####SBATCH --cpus-per-task=16
####SBATCH -B 2:16:1
####SBATCH --export=ALL
####SBATCH -t 01:30:00

####Load Module Environment
module purge
module load slurm
module load cpu
module load intel
module load intel-mpi

####Run
export OMP_NUM_THREADS=16
mpirun -genv I_MPI_PIN_DOMAIN=omp:compact ./hello_hybrid
```

##### Compiling

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

##### Submission

```text
[user@login01 HYBRID]$ sbatch hybrid-slurm.sb
Submitted batch job 1089019
[...]
```

##### Output

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


### GPU Jobs
<a name="gpu-jobs"></a>
#### GPU Hardware

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

#### Using GPU Nodes

* GPU nodes are allocated as a separate resource. The conversion rate is \(TBD\) Expanse Service Units \(SUs\) to 1 V100 GPU-hour.
* GPU nodes are not the same as the login nodes

**GPU codes must be compiled by requesting an interactive session on a GPU nodes**

* Batch: GPU nodes can be accessed via either the "gpu" or the "gpu-shared" partitions: `#SBATCH -p gpu` or `#SBATCH -p gpu-shared`
* Be sure to setup your CUDA environment for the compiler that you want to use   

###### For CUDA codes, you will need the cuda Compiler. Expanse has several CUDA compiler libraries

```text
### Environment for the CUDA Compiler
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

###### For OpenACC codes, you will need the PGI Compiler:

```text
### Environment for the PGI Compiler
module purge
module load slurm
module load gpu
module load pgi
```

#### Obtaining CUDA Information

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

#### Compiling:

All compilng for GPU codes **must be done on an** [**interactive node**](../#interactive-jobs) to compile the code:

1. Load the right Modules
2. Compile the Source code
3. Run code locally or exit interactive node and submit the batch script


---
<a name="hello-cuda"></a>description: >-
  Simple tutorial to compile and run a CUDA hello world program on Expanse GPU
  node
---

#### Hello CUDA

##### Code

`hello\_world\_gpu.cu`
```c
// Cuda By Example - By Sanders and Kudrot
//
// Hello World Program in CUDA C
//
// Contains a function that is executed on the device (GPU)
//

####include<stdio.h>

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
####!/bin/bash
####SBATCH --job-name="hello_world"
####SBATCH --output="hello_world.%j.%N.out"
####SBATCH --partition=gpu-shared
####SBATCH --nodes=1
####SBATCH --ntasks-per-node=1
####SBATCH --gpus=1
####SBATCH --account=sds173
####SBATCH -t 01:00:00

####Environment
module purge
module load slurm
module load gpu
module load cuda10.2/toolkit/10.2.89

####Run the job
./hello_world
```

##### Compiling

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

##### Submission

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

##### Output

`hello\_world.1221237.exp-4-58.out`
```text
Hello World!
```


---
<a name="hello-openacc"></a>description: >-
  Simple tutorial to compile and run an OpenACC laplace2d program on Expanse GPU
  node
---

#### Hello OpenACC

##### Code

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

####include <math.h>
####include <string.h>
####include <stdio.h>
####include "timer.h"

####define NN 4096
####define NM 4096

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

####pragma acc data copy(A), create(Anew)
    while ( error > tol && iter < iter_max )
    {
        error = 0.0;

####pragma acc kernels
        for( int j = 1; j < n-1; j++)
        {
            for( int i = 1; i < m-1; i++ )
            {
                Anew[j][i] = 0.25 * ( A[j][i+1] + A[j][i-1]
                                    + A[j-1][i] + A[j+1][i]);
                error = fmax( error, fabs(Anew[j][i] - A[j][i]));
            }
        }

####pragma acc kernels
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

####ifndef TIMER_H
####define TIMER_H

####include <stdlib.h>

####ifdef WIN32
####define WIN32_LEAN_AND_MEAN
####include <windows.h>
####else
####include <sys/time.h>
####endif

####ifdef WIN32
double PCFreq = 0.0;
__int64 timerStart = 0;
####else
struct timeval timerStart;
####endif

void StartTimer()
{
####ifdef WIN32
    LARGE_INTEGER li;
    if(!QueryPerformanceFrequency(&li))
        printf("QueryPerformanceFrequency failed!\n");

    PCFreq = (double)li.QuadPart/1000.0;

    QueryPerformanceCounter(&li);
    timerStart = li.QuadPart;
####else
    gettimeofday(&timerStart, NULL);
####endif
}

// time elapsed in ms
double GetTimer()
{
####ifdef WIN32
    LARGE_INTEGER li;
    QueryPerformanceCounter(&li);
    return (double)(li.QuadPart-timerStart)/PCFreq;
####else
    struct timeval timerStop, timerElapsed;
    gettimeofday(&timerStop, NULL);
    timersub(&timerStop, &timerStart, &timerElapsed);
    return timerElapsed.tv_sec*1000.0+timerElapsed.tv_usec/1000.0;
####endif
}

####endif // TIMER_H
```

`openacc-gpu-shared.sb`
```bash
####!/bin/bash
####SBATCH --job-name="OpenACC"
####SBATCH --output="OpenACC.%j.%N.out"
####SBATCH --partition=gpu-shared
####SBATCH --nodes=1
####SBATCH --ntasks-per-node=1
####SBATCH --gpus=1
####SBATCH --acount=abc123
####SBATCH -t 01:00:00

####Environment
module purge
module load slurm
module load gpu
module load pgi

####Run the job
./laplace2d.openacc.exe
```

##### Compiling

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

##### Submission

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

##### Output

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


