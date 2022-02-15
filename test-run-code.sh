
function starting_py_container() {
    sudo docker start first-python;
}

function running_file(){
    sudo docker exec -ti first-python /bin/bash -c 'python3 ./Main.py'
}

starting_py_container
running_file