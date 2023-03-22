from connection import create_connection


if __name__ == '__main__':
    sql_ex1 = """
    SELECT * FROM users WHERE id = %s
    """

    sql_ex2 = """
    SELECT id, name, age 
    FROM users 
    WHERE age > 30
    ORDER BY age DESC
    """

    sql_ex3 = """
    SELECT * 
    FROM users 
    WHERE name SIMILAR TO '%(ам|ма)%'
    ORDER BY age DESC
    """

    with create_connection() as conn:
        c = conn.cursor()
        # c.execute(sql_ex1, (13, ))
        # for el in c.fetchone():
        #     print(el)
        c.execute(sql_ex3)
        for u in c.fetchall():
            print(u)
        c.close()
