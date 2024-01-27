
# 0x0E. SQL - More queries

This project focuses on expanding your knowledge and skills in SQL. Entailed in thes [README]() are the key concepts covered and tasks accomplished in this project.

## Learning Objectives

1.  **Creating Users and Managing Privileges**: Learn how to create new MySQL users and grant them specific privileges to databases or tables.
    
2.  **Understanding Constraints**: Explore concepts like PRIMARY KEY, FOREIGN KEY, NOT NULL, and UNIQUE constraints, which help enforce data integrity in databases.
    
3.  **Retrieving Data from Multiple Tables**: Understand how to retrieve data from multiple tables in a single SQL query using techniques like JOIN, UNION, and subqueries.
    

## Concepts Covered

-   Creating a new MySQL user
-   Managing user privileges using the GRANT statement
-   Understanding primary keys and foreign keys
-   Using constraints like NOT NULL and UNIQUE
-   Retrieving data from multiple tables using JOIN and UNION
-   Working with subqueries to perform complex data retrieval

## Task Examples

-   **Creating a New User**: `CREATE USER 'username'@'hostname' IDENTIFIED BY 'password';`
-   **Granting Privileges**: `GRANT SELECT, INSERT, UPDATE ON database.table TO 'username'@'hostname';`
-   **Primary Key**: A PRIMARY KEY is a unique identifier for each record in a table. It ensures that each row is uniquely identifiable.
-   **Foreign Key**: A FOREIGN KEY is a field in a table that points to the PRIMARY KEY of another table. It establishes a link between two tables.
-   **Constraints**: Constraints define rules for the data that can be stored in a table. NOT NULL ensures a column cannot have NULL values, while UNIQUE ensures that all values in a column are distinct.
-   **JOIN and UNION**: JOIN is used to combine rows from two or more tables based on a related column, while UNION is used to combine the results of two or more SELECT queries into a single result set.

## Usage

-   Install MySQL 8.0 on Ubuntu 20.04 LTS
-   Connect to MySQL server using credentials root/root
-   Run SQL queries to create users, manage privileges, and perform various data retrieval operations
-   Import SQL dumps using commands like `mysql -uroot -p < dump_file.sql`

## Additional Resources

-   MySQL documentation: MySQL 8.0 SQL Statement Syntax
-   SQL tutorials and guides: [MySQL Tutorial](https://www.mysqltutorial.org/)
-   SQL style guides: [SQL Style Guide](https://www.sqlstyle.guide/)
-   Understanding relational database design: Normalization, ER Modeling

This project aims to enhance your SQL skills and deepen your understanding of database management. Feel free to explore further resources and practice SQL queries to reinforce your learning.

## More Info
### Comments for your SQL file
```
$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$
```
### Install MySQL 8.0 on Ubuntu 20.04 LTS
```
$ sudo apt update
$ sudo apt install mysql-server
...
$ mysql --version
mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
$
```
Connect to your MySQL server:
```
$ sudo mysql
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 11
Server version: 8.0.25-0ubuntu0.20.04.1 (Ubuntu)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
mysql> quit
Bye
$
```

### Use “container-on-demand” to run MySQL

**In the container, credentials are  `root/root`**

-   Ask for container  `Ubuntu 20.04`
-   Connect via SSH
-   OR connect via the Web terminal
-   In the container, you should start MySQL before playing with it:
```
$ service mysql start                                                   
 * Starting MySQL database server mysqld 
$
$ cat 0-list_databases.sql | mysql -uroot -p                               
Database                                                                                   
information_schema                                                                         
mysql                                                                                      
performance_schema                                                                         
sys                      
$
```
**In the container, credentials are  `root/root`**

### How to import a SQL dump
```
$ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
Enter password: 
$ curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
$ echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
id  name
1   Drama
2   Mystery
3   Adventure
4   Fantasy
5   Comedy
6   Crime
7   Suspense
8   Thriller
$
```