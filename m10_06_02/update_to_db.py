from faker import Faker

from connection import create_connection

fake = Faker('uk-UA')


if __name__ == '__main__':
    sql_ex = """
    SELECT COUNT(*) FROM users;
    """
    sql_update = "UPDATE users SET phone = %s WHERE id = %s;"

    with create_connection() as conn:
        c = conn.cursor()
        c.execute(sql_ex)
        count, = c.fetchone()
        for i in range(1, count + 1):
            c.execute(sql_update, (fake.phone_number(), i))
        c.close()
