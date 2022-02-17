---
sort: 3
---
# Expanse 101 (Refactored)
## Introduction to Running Jobs on the Expanse Supercomputer

## For more training event and information, see:
[SDSC Advanced User Training](https://www.sdsc.edu/education_and_training/training_hpc.html)

Document last updated: 02/16/2022

<hr>
In this tutorial, you will learn how to compile and run jobs on Expanse,
where to run them, and how to run batch jobs. The commands below can be
cut & pasted into the terminal window, when it is connected to
expanse.sdsc.edu.

# Misc Notes/Updates:
* This tutorial is based on information found in the [Expanse User Guide](https://www.sdsc.edu/support/user_guides/expanse.html). Check the user guide for the most current and updated information.
* You must have an expanse account in order to access the system.
  * To obtain a trial account:
      [Expanse trial account](https://portal.xsede.org/allocations/startup#rapidaccess-trial)
*  You should be familiar with running basic Unix commands on and HPC system: see the
   *  [Basic Skills Tutorial](https://github.com/sdsc-hpc-training/basic_skills)
*  The *hostname* for Expanse is *login01* or *login02*
*  The *login node name* for Expanse is *login.expanse.sdsc.edu*
*  The operating system for Expanse is CentOS
*  The cluster management system is	*Bright Cluster Manager*
*  The Scheduler and Resource Manager	is *SLURM*
*  For information on moving files from Comet to Expanse, see the [Comet to Expanse
Transition Workshop](https://education.sdsc.edu/training/interactive/202010_comet_to_expanse/index.html)

If you have any difficulties completing these tasks, please contact the SDSC Consulting group at help@xsede.org.

<a name="top">TOP
