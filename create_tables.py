#!/usr/bin/python
 
import psycopg2
from config import config
 
def create_tables():
    """ create tables in the Gromet database"""
    commands = (
        """
        CREATE TABLE plant_care_info (
            type_id VARCHAR(255) PRIMARY KEY,
            description VARCHAR(255) NOT NULL
        )
        """,
        """ 
        CREATE TABLE users (
            user_id VARCHAR(255) PRIMARY KEY,
            password VARCHAR(255) NOT NULL
        )
        """,
        """
        CREATE TABLE plants (
            plant_id SERIAL PRIMARY KEY,
            nickname VARCHAR(255),
            type_id VARCHAR(255) NOT NULL,
            user_id VARCHAR(255) NOT NULL,
            FOREIGN KEY (type_id)
                REFERENCES plant_care_info (type_id),
            FOREIGN KEY (user_id)
                REFERENCES users (user_id)
                ON UPDATE CASCADE ON DELETE CASCADE
        )
        """,
        """
        CREATE TABLE plant_history (
            record_id SERIAL PRIMARY KEY,
            plant_id INTEGER NOT NULL,
            humidity_measurement_percent smallint,
            time_recorded TIMESTAMPTZ NOT NULL,
            FOREIGN KEY (plant_id)
                REFERENCES plants (plant_id)
                ON UPDATE CASCADE ON DELETE CASCADE
        )
        """)
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
 
 
if __name__ == '__main__':
    create_tables()