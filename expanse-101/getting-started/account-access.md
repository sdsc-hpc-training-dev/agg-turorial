# Account Access

## Logging Onto Expanse

Expanse supports Single Sign-On through the [XSEDE User Portal](https://portal.xsede.org), from the command line using an XSEDE-wide password \(coming soon, the Expanse User Portal\). While CPU and GPU resources are allocated separately, the login nodes are the same. To log in to Expanse from the command line, use the hostname `login.expanse.sdsc.edu`

The following Secure Shell \(ssh\) command may be used to log in to Expanse

```text
ssh <your_user>@login.expanse.sdsc.edu
```

Details about how to access Expanse under different circumstances are described in the [Expanse User Guide](https://www.sdsc.edu/support/user_guides/expanse.html#access)

For instructions on how to use SSH, see [Connecting to SDSC HPC Systems Guide](https://github.com/sdsc-hpc-training-org/hpc-security). Below is the logon message – often called the _MOTD_ \(message of the day, located in /etc/motd\). This has not been implemented at this point on Expanse.

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

#### Example of a terminal connection/Unix login session

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

## Obtaining Tutorial Example Code

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

## [Expanse User Portal](https://portal.expanse.sdsc.edu)

* Quick and easy way for Expanse users to login, transfer and edit files and submit and monitor jobs.
* Gateway for launching interactive applications such as MATLAB, Rstudio
* Integrated web-based environment for file management and job submission
* All Users with valid Expanse Allocation and XSEDE Based credentials have access via their XSEDE credentials

## Expanse-Client Script

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

## Using Accounts in Batch Jobs

As with the case above, some users will have access to multiple accounts \(e.g. an allocation for a research project and a separate allocation for classroom or educational use\). Users should verify that the correct project is designated for all batch jobs. Awards are granted for a specific purposes and should not be used for other projects. Designate a project by replacing &lt;&lt; project &gt;&gt; with a project listed as above in the SBATCH directive in your job script:

```text
  #SBATCH -A <project>
```

## Managing Users on an Account

Only project PIs and co-PIs can add or remove users from an account. This can only be done via the [XSEDE portal](https://portal.xsede.org) account \(there is no command line interface for this\). After logging in, go to the Add User page for the account.

## Job Charging

The basic charge unit for all SDSC machines, including Expanse, is the Service Unit \(SU\). This corresponds to:

* Use of one compute core utilizing less than or equal to 2G of data for one hour
* 1 GPU using less than 96G of data for 1 hour.

  Note: your charges are based on the resources that are tied up by your job and don't necessarily reflect how the resources are used. Charges are based on either the number of cores or the fraction of the memory requested, whichever is larger. The minimum charge for any job is 1 SU.

See the [Expanse User Guide](https://www.sdsc.edu/support/user_guides/expanse.html#charging) for more details and factors that affect job charging.

