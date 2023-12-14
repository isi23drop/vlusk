#!/usr/bin/bash
#
#
podman run -it -p=5432:5432 --name db -d \
    -e POSTGRES_USER=admin \
    -e POSTGRES_PASSWORD=Passw0rd \
    -v /mnt/ssd/dataStore/containers/database/pgad-pod/pgdata:/var/lib/postgresql/data:Z \
    docker.io/library/postgres:16.0


