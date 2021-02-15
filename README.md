## Jira Data Miner (POC)                    
This is a lite poc project dealing with Jira.

## Prereqs:

 * Python3
 * All other dependencies are fetched by running the following:
  ```sh
  $ make pip
  ```

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

### Use venv
It's also possible to use ``venv``, some would argue it's even recommended! 
By default, there is support for creating a virtual environment called ``dev``. Run the following to create it:

```sh
$ make env
```

Now that it's created, let's activate it. Note that once created, it does not need to be re-created unless for some reason it got deleted.

```sh
$ source dev/bin/activate
$ source credentials.env
```

The above command will activate the ``dev`` virtual environment and source the ``credentials.env`` file in this environment.
Run the following to install required dependencies:

```sh
$ make pip
```

Please note that the above command needs to be run only when the env is newly created, not every time after it has been activated.
Run the miner as usual:

```sh
$ make run
```

Deactivate the virtual environment like so:

```sh
$ deactivate
```

If for any reason the ``dev`` virtual env needs to be deleted - run the following:

```sh
$ make clean
```
