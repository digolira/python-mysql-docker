#!/bin/bash

function install_docker_compose() {
     sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
     chmod +x /usr/local/bin/docker-compose
}

function compose_up() {
    sudo docker-compose up -d
}

function starting_py_container() {
    sudo docker start first-python;
}

function running_file(){
    sudo docker exec -ti first-python /bin/bash -c 'python3 ./Main.py'
}

compose_up
starting_py_container
running_file