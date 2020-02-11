#!/usr/bin/python
 
import psycopg2
from config import config
 
def insert_plant_care_info(type_id, description):
    """ insert a new entry into the plant_care_info table """
    sql = """ INSERT INTO plant_care_info(type_id, description) VALUES (%s,%s)"""
    record = (type_id, description)
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

def insert_plant_care_info_list(plant_list):
    """ insert multiple plant_care_info into the plant_care_info table  """
    sql = """ INSERT INTO plant_care_info(type_id, description) VALUES (%s,%s)"""
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
    # insert one plant info
    insert_plant_care_info('Succulent','Likes to be neglected. Water once a week by misting the plant.')
    # insert multiple plant_care_info,
    insert_plant_care_info_list([
        ('Snake Plant','Tolerates low light and little water. Let soil dry fully between waterings.',),
        ('Heartleaf Philodendon','This little philodendron thrives under fluorescent lights, making it a popular office plant.',),
        ('Aloe Vera','Favors bright light and temps around 65 - 75°F. Keep soil moderately dry.',),
    ])