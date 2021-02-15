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
|*hostname*         | Jira hostname  |  | x
|*username*    | Username for the jira login  |  | x
|*password*         | Password for the said user  |      | x
|*board-filter-id*         | Board filter id  |      | x
|*board-id*         | Board id  |      |
|*project*         | Project name  |      |
|*weeks*         | Number of weeks to retrieve data for  |  6    | x

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
