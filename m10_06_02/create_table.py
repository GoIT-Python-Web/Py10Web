from psycopg2 import Error
from connection import create_connection


def create_table(conn, ex_sql):
    c = conn.cursor()
    c.execute(ex_sql)
    c.close()


if __name__ == '__main__':
    sql_e = """
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        name VARCHAR(130),
        email VARCHAR(130),
        password VARCHAR(130),
        age NUMERIC CHECK (age > 0 AND age < 150)
    );
    """
    with create_connection() as conn:
        create_table(conn, sql_e)
