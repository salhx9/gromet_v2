#!/usr/bin/python
 
import psycopg2
from config import config
 
 
def update_plant_nickname(new_nickname,plant_id):
    """ update plant name based on the plant id """
    sql = """ UPDATE plants
                SET nickname = %s
                WHERE plant_id = %s"""
    conn = None
    updated_rows = 0
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the UPDATE  statement
        cur.execute(sql, (new_nickname,plant_id))
        # get the number of updated rows
        updated_rows = cur.rowcount
        # Commit the changes to the database
        conn.commit()
        # Close communication with the PostgreSQL database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
 
    return updated_rows

if __name__ == '__main__':
    update_plant_nickname('Severus',2)