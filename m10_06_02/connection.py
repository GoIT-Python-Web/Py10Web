from psycopg2 import connect, Error
from contextlib import contextmanager


@contextmanager
def create_connection():
    """ create a database connection to a Postgres database """
    conn = None
    try:
        conn = connect(host='localhost', user='postgres', password='567234', database='postgres', port=5432)
        yield conn
        conn.commit()
    except Error as err:
        print(err)
        conn.rollback()
    finally:
        if conn:
            conn.close()
