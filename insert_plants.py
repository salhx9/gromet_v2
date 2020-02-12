#!/usr/bin/python
 
import psycopg2
from config import config
 
def insert_plants(type_id, nickname, user_id):
    """ insert a new entry into the plants table """
    sql = """ INSERT INTO plants(type_id, nickname, user_id) VALUES (%s,%s,%s)"""
    record = (type_id, nickname, user_id)
    conn = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, record)
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def insert_plants_list(plant_list):
    """ insert multiple plants into the plants table  """
    sql = """ INSERT INTO plants(type_id, nickname, user_id) VALUES (%s,%s,%s)"""
    conn = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.executemany(sql,plant_list)
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    # insert one plant
    # type_id, nickname, user_id
    insert_plants('Succulent','Bucky','jacob')
    # insert multiple plants,
    insert_plants_list([
        ('Snake Plant','Bobby Sue','ryon'),
        ('Heartleaf Philodendron','Salem','sabrina'),
        ('Aloe Vera','Adele','katie'),
        ('Succulent','','katie'),
        ('Succulent','Caleb','jacob'),
        ('Succulent','Hannah','jacob')
    ])