#!/usr/bin/python
 
import psycopg2
from config import config
 
def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE plants (
            plant_id SERIAL PRIMARY KEY,
            plant_type VARCHAR(255) NOT NULL,
            plant_nickname VARCHAR(100),
            user_id INTEGER NOT NULL,
            FOREIGN KEY (user_id)
            REFERENCES user (user_id)
            ON UPDATE CASCADE ON DELETE CASCADE
        )
        """,
        """ 
        CREATE TABLE user (
                user_id SERIAL PRIMARY KEY,
                user_password VARCHAR(255) NOT NULL
                )
        """,
        """
        CREATE TABLE plant_care_info (
                plant_type VARCHAR(25) PRIMARY KEY,
                description VARCHAR(255) NOT NULL
        )
        """,
        """
        CREATE TABLE plant_history (
                plant_id INTEGER NOT NULL,
                record_id SERIAL,
                humidity_measurement_percent smallint NOT NULL,
                time_recorded TIMESTAMPTZ NOT NULL,
                PRIMARY KEY (plant_id, record_id),
                FOREIGN KEY (plant_id)
                    REFERENCES plants (plant_id)
                    ON UPDATE CASCADE ON DELETE CASCADE,
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