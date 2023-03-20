from psycopg2 import connect, Error
from contextlib import contextmanager


@contextmanager
def create_connection():
    """ create a database connection to a Postgres database """
    conn = None
    try:
        conn = connect(host='localhost', user='postgres', password='567234', database='postgres', port=5432)
        yield conn
        conn.rollback()
        conn.close()
    except Error as err:
        print(err)
    finally:
        if conn:
            conn.close()


def create_table(conn, sql_execute):
    try:
        c = conn.cursor()
        c.execute(sql_execute)
        c.close()
        conn.commit()
    except Exception as err:
        print(err)


if __name__ == "__main__":
    sql_e = """
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        name VARCHAR(30),
        email VARCHAR(30),
        password VARCHAR(30),
        age NUMERIC CHECK (age > 0 AND age < 150)
    );
    """
    with create_connection() as conn:
        create_table(conn, sql_e)
        c = conn.cursor()
        c.executemany('INSERT INTO users (name, email, password, age) VALUES (%s, %s, %s, %s)',
                      [('Denis', 'denis@meta.ua', '123456', 32), ('Denis', 'denis@meta.ua', '123456', 32)])
        c.close()
        conn.commit()
