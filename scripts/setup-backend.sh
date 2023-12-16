#!/usr/bin/bash
#
# install podman
#sudo apt-get update
#sudo apt-get -y install podman

# install postgres to get psql
sudo sh -c 'echo "deb https://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
sudo apt-get update
sudo apt-get -y install postgresql

# get oci container image for postgres
# done: debug password
# can be replaced by docker also.
# db or dbdrop
podman run -it -p=5432:5432 --name dbdrop -d \
    -e POSTGRES_USER=admin \
    -e POSTGRES_PASSWORD=Passw0rd \ #${{ secrets.POSTGRES_PASSWORD }}\
    docker.io/library/postgres:16.0

# connect to the container with psql
## Create schema with Raw SQL script then populate the database
for f in ../backend/migrations/*.sql;
do
    psql -h localhost -U admin -f "$f"
done
