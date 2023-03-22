from random import randint

from faker import Faker

from connection import create_connection

fake = Faker('uk-UA')


if __name__ == '__main__':
    sql_ex = 'INSERT INTO users (name, email, password, age) VALUES (%s, %s, %s, %s)'

    with create_connection() as conn:
        c = conn.cursor()
        for _ in range(200):
            c.execute(sql_ex, (fake.name(), fake.email(), fake.password(), randint(18, 100)))
        c.close()



