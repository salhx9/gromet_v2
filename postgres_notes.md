# Shelby's postgresql and python adventure

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
 
### Sign in as unpriv user
```
psql postgres -U bob;
```
 
### Create database
```
CREATE DATABASE gromet;
```
 
### add at least one user who has permission to access the database (aside from the super users, who can access everything)
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
 

## Commandline Opening up Existing DB

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