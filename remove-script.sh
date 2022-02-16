#!/bin/bash

function deleting_containers() {
    sudo docker rm -f first-python first-mysql; 
}

function deleting_image() {
    sudo docker rmi -f python-mysql-docker_python
}

function deleting_networks() {
    sudo docker network rm python-mysql-docker_mynetwork
}

function deleting_volumes(){
    sudo docker volume rm -f python-mysql-docker_myvolume
}

deleting_containers
deleting_image
deleting_networks
deleting_volumes
