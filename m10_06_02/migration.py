from connection import create_connection


if __name__ == '__main__':
    sql_ex = """
    ALTER TABLE users ADD COLUMN phone varchar(30);
    """

    with create_connection() as conn:
        c = conn.cursor()
        c.execute(sql_ex)
        c.close()
