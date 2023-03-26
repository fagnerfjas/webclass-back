# WebClass_back!
This is a python aplication, developed with Flask Framwork. 
The propose of this project is to support other applications or features that we want to implement, shuch as monitoring students activities on our web server.
This and other project are being implemented at "ECIT Inácio Antonino" in city Serra Branca - PB, Brazil, technical school with cours in Infromatics for the internet.

## Dependences

- You may need to install the Python 3 and MySQL development headers and libraries like so: `$ sudo apt-get install python3-dev default-libmysqlclient-dev build-essential`

- Now you can Install MysqlClient library via PIP: ` $ pip install mysqlclient `

- Finaly install the library to connect the Flask Framwork to Mysql databases: `pip install flask-mysqldb`

## Requests
eg: 	
**Title**
*methosd* | *Authorization* | `url`
Description

**Get databases** 
*GET* | *free* | `<address>/databases`
Return a Json with list of databases accessibles.
