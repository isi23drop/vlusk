# flask-orm
> backend with flask and sqlite3.

Since it's common for backends to connect to a database, the software infrastructure of these underlying systems can be deployed in a lightweight virtualized manner, using OCI containers. The orchestration tool ```docker-compose``` is compatible with Podman and k8s to deploy multiple containers, and even thinking about tools like Docker Swarm, you can adapt the YAML to run in a single host but to be scalable to run distributed. What makes it possible are components such as __Podman Service__ and the kubernetes distro __k3s__.

This repository attempts to deploy a simple proof-of-concept backend adopting a test driven development approach, seemingly scaling from single host mocking with unit tests to multi-node integration tests if needed.

### Running in Standalone mode

Prepare the environment:

```sh
; git clone git@github.com:deomorxsy/florm.git
; cd ./florm
; python3 -m venv venv
; source ./venv/bin/activate
; pip3 install --upgrade pip
; pip3 install -r ./requirements.txt

```


Now that all dependencies are installed, just run each process from a different terminal:

1. init the sqlite3 database
```sh
flask --app app init-db
```

2.
```sh
flask --app app run --debug
```

### Podman Service and DOCKER_HOST
The orchestration tool ```docker-compose``` supports Podman Service through the DOCKER_HOST environment variable. This makes it possible to run containers with podman but with the benefit of rootless.

1. install docker-compose
2. use the init system to start the Podman Socket. Using Systemd here:
```sh
systemctl -user start podman.socket
```
3. check if the system is running. It should return an "OK"
```sh
$ curl -H "Content-Type: application/json" --unix-socket $XDG_RUNTIME_DIR/podman/podman.sock http://localhost/_ping
```
4. set up the DOCKER_HOST environment variable:
```sh
export DOCKER_HOST=unix://$XDG_RUNTIME_DIR/podman/podman.sock
```

5. run docker-compose at the root of the repository
```sh
docker-compose  up
```

### Running with the podman-compose script
### Running with k8s
Here you can use k3s.
