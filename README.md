## Jira Data Miner (POC)                    
This is a lite poc project dealing with Jira.

## Prereqs:

 1. Python3
 2. Plotly
 3. Jira

## Usage

#### Data Miner
 
| Option        | About                                             | Default       | Required       |
| ------------- |:--------------------------------------------------|:-------------:|:--------------:|
|*hostname*         | Jira hostname  |  |
|*username*    | Username for the jira login  |  |
|*password*         | Password for the said user  |      |

#### Run
Before starting the miner, you need to fill in the proper credentials. Have a look in the ``credentials.env`` file and edit it accordingly.
Please note that local changes of your ``credentials.env`` file **must** not be commited.

```sh
$ source ./credentials.env
```

Run the miner

```sh
$ make run
```
