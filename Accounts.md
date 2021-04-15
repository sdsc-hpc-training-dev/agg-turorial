---
sort: 4
---

#  Managing Accounts on Expanse
* [Expanse Client Script](#manage-accts-client-script)
* [Using Accounts in Batch Jobs](#manage-accts-batch-script)
* [Managing Users on an Account](#manage-accts-users)

##  <a name="manage-accts-client-script"></a>Expanse-Client Script

* The expanse-client script provides additional details regarding User and Project availability and usage located at:

```
/cm/shared/apps/sdsc/current/bin/expanse-client
```

* Example of Script Usage:

```
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

```
[user@login01 ~]$ expanse-client user -p

 Resource  sdsc_expanse

 NAME     PROJECT  USED  AVAILABLE  USED BY PROJECT
----------------------------------------------------
 user  abc123     33      80000              180
 user  srt456      0       5000               79
 user  xyz789    318     500000          2905439
```

* To see who is on an account:

```
[user@login01]$  expanse-client project abc123 -v

 Resource          sdsc_expanse    
 Project           xyz789         
 Total allocation  500000         
 Total recorded    289243         
 Total queued      13004           
 Expiration        January 1, 2024

╭────┬──────────┬───────────────┬─────────────┬───────────┬──────────────────────────┬────────────────────────╮
│    │ NAME     │ USED RECORDED │ USED QUEUED │ AVAILABLE │ USED BY PROJECT RECORDED │ USED BY PROJECT QUEUED │
├────┼──────────┼───────────────┼─────────────┼───────────┼──────────────────────────┼────────────────────────┤
│  1 │ user1    │             0 │           0 │   500000  │                  289243  │                  13004 │
│  2 │ user2    │          6624 │           0 │   500000  │                  289243  │                  13004 │
[SNIP]
│  9 │ user3    │            33 │           0 │   500000  │                  289243  │                  13004 │
│ 10 │ user4    │            14 │           0 │   500000  │                  289243  │                  13004 │
╰────┴──────────┴───────────────┴─────────────┴───────────┴──────────────────────────┴────────────────────────╯

```

##  <a name="manage-accts-batch-script"></a>Using Accounts in Batch Jobs
As with the case above, some users will have access to multiple accounts (e.g. an allocation for a research project and a separate allocation for classroom or educational use). Users should verify that the correct project is designated for all batch jobs. Awards are granted for a specific purposes and should not be used for other projects. Designate a project by replacing  << project >> with a project listed as above in the SBATCH directive in your job script:

```
  #SBATCH -A << project >>
```

##  <a name="manage-accts-users"></a>Managing Users on an Account
Only project PIs and co-PIs can add or remove users from an account. This can only be done
via the [XSEDE portal](https://portal.xsede.org) account (there is no command line interface for this).
After logging in, go to the Add User page for the account.
