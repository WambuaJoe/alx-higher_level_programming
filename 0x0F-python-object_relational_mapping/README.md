# 0x0F. Python - Object-Relational Mapping

## Introduction

This project explores the world of Object-Relational Mapping (ORM) in Python, focusing on connecting to a MySQL database and performing operations using both MySQLdb and SQLAlchemy. The project also covers the basics of setting up a Python Virtual Environment to manage dependencies.

## Learning Objectives

Upon completing this project, you will gain knowledge on:

-   The advantages of Python programming
-   Establishing a connection to a MySQL database using a Python script
-   Executing SELECT and INSERT operations in a MySQL table from a Python script
-   Understanding the concept of Object-Relational Mapping (ORM)
-   Mapping a Python Class to a MySQL table
-   Creating a Python Virtual Environment for project-specific dependencies

## Requirements

### Environment Setup

1.  Install venv:    
    ```
    $ sudo apt-get install python3.8-venv
    $ python3 -m venv venv
    $ source venv/bin/activate
    ```
    
2.  Install MySQLdb module version 2.0.x:
    
    bashCopy code
    ```
    $ sudo apt-get install python3-dev
    $ sudo apt-get install libmysqlclient-dev
    $ sudo apt-get install zlib1g-dev
    $ sudo pip3 install mysqlclient
    ```
    
3.  Install SQLAlchemy module version 1.4.x:
    
	```
	$ sudo pip3 install SQLAlchemy
    ```

### General Project Requirements

-   Editors: vi, vim, emacs
-   Interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
-   Executed with MySQLdb version 2.0.x and SQLAlchemy version 1.4.x
-   Files end with a new line
-   First line of all files: `#!/usr/bin/python3`
-   README.md file at the root of the project folder
-   Code follows pycodestyle (version 2.8.*)
-   All files must be executable
-   Modules, classes, and functions must have documentation

## Key Concepts

### Object-Relational Mapping (ORM)

ORM is a programming technique for converting data between incompatible type systems, often between a relational database and an object-oriented programming language. It allows seamless interaction between the database and the application using high-level, object-oriented code.

### Python Virtual Environment

A Python Virtual Environment is an isolated environment where you can install project-specific dependencies without affecting the global Python installation. It helps manage dependencies and avoids conflicts between different projects.

## Usage

1.  Activate the virtual environment:
    
    bashCopy code
    
    `$ source venv/bin/activate` 
    
2.  Execute your Python script with MySQLdb and SQLAlchemy.
    

## Contributing

Contributions are welcome! Follow the guidelines in the [README.md](https://github.com/WambuaJoe/alx-higher_level_programming/blob/main/0x0F-python-object_relational_mapping/README.md) file for submitting issues or pull requests.