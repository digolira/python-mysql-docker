#!/bin/bash

function checker() { 
    which "$1" | grep -o "$1" > /dev/null && return 0 || return 1
}

function install_docker_compose() {
    #check if docker-compose is already installed
    if checker "docker-compose";
    then
        echo "Docker Compose is already installed. Instalation will continue...";
    else
        echo "Docker-compose is required and not installed. Do you want to install? Y/N"
        read answer
        if [[ ${answer,,} = y ]];
        then
            sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
            chmod +x /usr/local/bin/docker-compose;
        else 
            echo "Installation will crash.";
            fi;
    fi
}

function compose_up() {
    sudo docker-compose up -d
}

function running_file(){
    sudo docker exec -ti first-python /bin/bash -c 'python3 ./Main.py'
}

install_docker_compose
compose_up
running_file