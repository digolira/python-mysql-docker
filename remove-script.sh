#!/bin/bash

function deleting_containers() {
    sudo docker rm -f first-python first-mysql; 
}

function deleting_image() {
    sudo docker rmi -f python-mysql-docker_python
}

function deleting_networks() {
    sudo docker network prune -f

}

deleting_containers
deleting_image
deleting_networks
