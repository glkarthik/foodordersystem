# Food court ordering system

This project contains food ordering system developed in Django and python. This MVC based development architecture.

### Tools and Applications that are necessary to work with this codebase

1) Django
2) Python
3) Docker 
4) Mysql

### Initial Setup

1) Foodcourt app docker image is created and made to run in local docker. 
2)Dockerfile for the above above app should have the HOST as ipaddress of the computer.
3) Mysql container deployed in docker.
### Commands used to run in local docker

docker run -d -p 3306:3306 --name mysql-docker-container -e MYSQL_ROOT_PASSWORD=root -e MYSQL_DATABASE=foodcourt -e MYSQL_USER=root -e MYSQL_PASSWORD=root mysql/mysql-server:latest

docker build . -t dockerhubkarthik/foodcourt:2.0.0

docker run -p 8000:8000 dockerhubkarthik/foodcourt:2.0.0

# Run the below commands by using the docker command "docker exec -it <container ID> /bin/bash".

python manage.py migrate
python manage.py createsuperuser


# Manage the inventories by logging admin console
http://0.0.0.0:8000/admin/

Enter username as admin |
Enter email as admin@admin.com |
Enter password as test1234

# Below URl is the main page to order the food
http://0.0.0.0:8000/inventories/
