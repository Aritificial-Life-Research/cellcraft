# The Cellcraft Project


### Setup your computer for using Cellcraft

#### Start a Docker Image and create a MongoDB where to store the biological information of your minecraft world (Run only once!!)

* Install Docker in your computer: https://docs.docker.com/docker-for-mac/install/
* You can also install Kinematic as an interface for the docker image

* Create an instance Mongo database
```
docker pull mongo:latest
```

* For accessing the mongo shell
```
docker run -it --link mongo:mongo --rm mongo sh -c 'exec mongo "$MONGO_PORT_27017_TCP_ADDR:$MONGO_PORT_27017_TCP_PORT/cellcraft"'
```

* Create a user as database admin
```
docker run -it --link mongo:mongo --rm mongo sh -c 'exec mongo "$MONGO_PORT_27017_TCP_ADDR:$MONGO_PORT_27017_TCP_PORT/admin"'
db.createUser({ user: 'cellcraft', pwd: 'cellcraft', roles: [ { role: "userAdminAnyDatabase", db: "admin" } ] });
```

* Create other users for the cellcraft database
```
mongo another -u cellcraft -p cellcraft
db.addUser({ user: "cellcraft", pwd: "cellcraft", roles: [{role: "readWrite", db: "cellcraft"}]})
```

* To backup the database into "cellcraft-backup" folder (backup the database regularly)
```
docker exec -it mongo bash
mongodump --db cellcraft --out cellcraft/mongo_storage/data/cellcraft-backup
```


#### Setup your python environment

* Linux Setup
```
curl -L https://raw.githubusercontent.com/pyenv/pyenv-installer/master/bin/pyenv-installer | bash
pyenv update
echo 'export PATH="$HOME/.pyenv/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
source ~/.bashrc
pyenv install 3.5.2

pyenv global 3.5.2
source ~/.bashrc
```

* Mac OX Setup
```
brew update
brew install pyenv
brew install pyenv-virtualenv
echo 'eval "$(pyenv init -)"' >> ~/.bash_profile
source ~/.bash_profile
pyenv install 3.5.2

pyenv global 3.5.2
source ~/.bash_profile
```

* To create and activate the python environment
```
pyenv virtualenv cellcraft
pyenv activate cellcraft
```


##### Install python packages from requirements
```
pip install -r requirements.txt
```


#### Setup your local MongoDB to store biological information about your world
* Create your database (run it only once)




#### Installation
- install forge minecraft server (version 1.8, may not work otherwise)
- install the RaspberryJamMod.jar (https://github.com/arpruss/raspberryjammod)
- Identify a folder called “mcpipy”, within the installation dictionary
- clone our repository “cellcraft” as a subfolder in mcpipy
- copy the cellcraft.py from the subfolder into the mcpipy folder (move cellcraft.py one level up)

#### Getting started
- start the server
- connect with client
- open the minecraft console
- try: py cellcraft pdb 3J9U 2 4 -15 load

#### Usage
  py cellcraft [pdb/cellpack] [PDBcode] <threshold> <blocksize> <horizontal_shift> [load/nolo]
- `py cellcraft` : mandatory
- `[pdb/cellpack]` : load pdb or cellpack structure (the later is not covered here)
- `[PDBcode]` : specify the PDB code (for pdb)
- `<threshold>` : minimum number of atoms found in grid cube to be filled
- `<blocksize>` : spacing of the grid in Angstroem
- `<horizontal_shift>` : horizontal shift of the structure in respect of the player position
- `[load/nolo]` :  load structure from database / take local copy
  (the latter is only possible if the same PDBid was processed before with the same threshold and blocksize)


#### Contact
info@thecellcraftproject.org
