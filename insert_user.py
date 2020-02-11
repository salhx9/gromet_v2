#!/usr/bin/python
 
import psycopg2
from config import config
 

def insert_user(user_id, password):
    """ insert a new user into the users table """
    sql = """ INSERT INTO users(user_id, password) VALUES (%s,%s)"""
    record = (user_id, password)
    conn = None
    user_id = None
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
 
    return user_id

def insert_user_list(user_list):
    """ insert multiple users into the users table  """
    sql = """ INSERT INTO users(user_id, password) VALUES (%s,%s)"""
    conn = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.executemany(sql,user_list)
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
    # insert one user
    insert_user('test_user','test_pw')
    # insert multiple users,
    insert_user_list([
        ('jacob','jacob_pass',),
        ('ryon','ryon_pass',),
        ('katie','katie_pass',),
        ('sabrina','sabrina_pass',),
    ])