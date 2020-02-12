#!/usr/bin/python
 
import psycopg2
from config import config
 
def insert_plant_history_record(plant_id, humidity, time_recorded):
    """ insert a new entry into the history table """
    sql = """ INSERT INTO plant_history(plant_id, humidity, time_recorded) VALUES (%s,%s,%s)"""
    record = (plant_id, humidity, time_recorded)
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

def insert_plant_history_record_list(plant_list):
    """ insert multiple plant_history into the plant_history table  """
    sql = """ INSERT INTO plant_history(plant_id, humidity, time_recorded) VALUES (%s,%s,%s)"""
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
    # insert one history
    # plant_id, humidity, time_recorded
    insert_plant_history_record('1',.50,'2019-06-22 02:10:25-07')
    # insert multiple plant_history,
    insert_plant_history_record_list([
        ('1',0.25,'2019-06-22 18:10:25-07'),
        ('2',0.40,'2019-06-22 18:10:25-07'),
        ('3',.10,'2019-06-22 18:10:25-07'),
        ('4',1.0,'2019-06-22 18:10:25-07'),
        ('5',.003,'2019-06-23 19:10:25-07'),
        ('6',1,'2019-06-24 15:10:25-07'),
        ('6',0.999,'2019-07-25 20:10:25-07'),
        ('6',0.808,'2019-07-25 23:10:25-07'),
        ('7',0.808,'2019-07-25 20:10:25-07'),
    ])