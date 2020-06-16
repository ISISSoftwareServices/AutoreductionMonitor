# Containerised Database with Persistent Storage Mounted to External Data Volumes

Compartmentalises a database to allow for easy updates to the database and even easier migrations.

The data is stored separately from the database in a data volume. Data volumes can be located on the 
same host machine somewhere else over a network.

Use the steps detailed below to access/modify the image, container or database:
  
### Build Docker Image with MySQL_image_schema.sql File Located in Current Directory
* `docker build -t system_monitoring_schema .`

### Build MySQL data volume called mysqldata
* `docker create -v /var/lib/mysql --name mysqldata mysql`

### Run The Container with Attached Data Volume and Image Containing Schema from DockerFile
* `docker run -p 15333:1433 --volumes-from mysqldata --name system_monitoring_db -d jack/mysql_system_monitoring`

### Execute Interactive Terminal Inside Container
* `docker exec -it testcontainer3 /bin/bash`

### Sign in to MySQL Using Credentials
* `mysql -uadmin -padmin`

### View Database and Tables of Interest
* `show databases;`
* `use system_monitoring;`
* `show tables;` - want to see tables matching schema so e.g. dates; instrument; statistics

### Additional Instructions for Testing Purposes
* Add data to each table
* Exit database and container:
* Kill system_monitoring_db container:
* Remove container:
* Create container again
* Check data last added still persists in system_monitoring database inside system_monitoring_db 
container.


 