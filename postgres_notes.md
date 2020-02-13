# Shelby's Postgresql and Python Adventure

## Dependencies
1. Install postgres.
2. Make sure you have python3 installed.
3. Use Python's package manager to install psycopg2 for using postgres within the python scripts.

## Creating the postgres database
 
### Command for creating a service to startup postgres
```
pg_ctl -D /usr/local/var/postgres start && brew services start postgresql
```

### Command for starting postgres once
```
pg_ctl -D /usr/local/var/postgres start
```
 
### Psql command line
```
psql postgres
```
 
### Create a new role
```
CREATE ROLE bob WITH LOGIN PASSWORD 'password';
ALTER ROLE bob CREATEDB;
```
 
### Sign in as the new user
```
psql postgres -U bob;
```
 
### Create database
```
CREATE DATABASE gromet;
```
 
### Add at least one user who has permission to access the database (aside from the super users, who can access everything)
```
GRANT ALL PRIVILEGES ON DATABASE gromet TO bob;
```
 
### login to gromet
```
\connect gromet;
```


## Quick Tips


### Database Viewing
* \connect: connect to a specific database
* \dt: list the tables in the currently connected database
* \du: view database users
* \list: lists all the databases in Postgres
* \q: quits

### Database Managment
* createuser: creates a user
* createdb: creates a database
* dropuser: deletes a user
* dropdb: deletes a database
* postgres: executes the SQL server itself
* pg_dump: dumps the contents of a single database to a file
* pg_dumpall: dumps all databases to a file
 

## Opening up Existing DB

### Command for starting postgres once
```
pg_ctl -D /usr/local/var/postgres start
```
 
### Psql command line
```
psql postgres
```
### Sign in as unpriv user
```
psql postgres -U bob;
```

### login to gromet
```
\connect gromet;
```

## Initializing the Database
1. Run the create_tables.py script to create the tables in the database.
2. Run insert_user.py to create users in the users table.
3. Run insert_plant_care_info.py to create a dictionary of plant types and their care descriptions.
4. Run insert_plants.py to insert plants associated with specific users.
5. Run insert_plant_history.py to insert humidity readings into the plant_history table for the plants in the plant table.
6. Test out some queries on each of the tables. To see the contents of a table use:
``` 
SELECT * FROM table_name;
```

## Normalization Review
This is unrelated to setup but helpful for designing the schema

### Primary Key
* A primary key cannot be NULL
* A primary key value must be unique
* The primary key values should rarely be changed
* The primary key must be given a value when a new record is inserted.

### Foreign Key references the primary key of another Table! It helps connect your Tables
* A foreign key can have a different name from its primary key
* It ensures rows in one table have corresponding rows in another
* Unlike the Primary key, they do not have to be unique. Most often they aren't
* Foreign keys can be null even though primary keys can not 
* You will only be able to insert values into your foreign key that exist in the unique key in the parent table. This helps in referential integrity.

### 1NF (First Normal Form) Rules
* Each table cell should contain a single value.
* Each record needs to be unique.

### 2NF (Second Normal Form) Rules
* Rule 1- Be in 1NF
* Rule 2- Single Column Primary Key

### 3NF (Third Normal Form) Rules
* Rule 1- Be in 2NF
* Rule 2- Has no transitive functional dependencies

### Transitive functional dependency 
* is when changing a non-key column, might cause any of the other non-key columns to change

### 3.5NF Boyce-Codd Normal Form (BCNF)
* Even when a database is in 3rd Normal Form, still there would be anomalies resulted if it has more than one Candidate Key.

### 4NF (Fourth Normal Form) Rules
* If no database table instance contains two or more independent and multivalued data describing the relevant entity, then it is in 4th Normal Form.

### 5NF (Fifth Normal Form) Rules
* A table is in 5th Normal Form only if it is in 4NF and it cannot be decomposed into any number of smaller tables without loss of data.
