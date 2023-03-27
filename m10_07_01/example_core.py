"""
Core
"""
from sqlalchemy import Table, Column, Integer, String, ForeignKey, MetaData, create_engine
from sqlalchemy.sql import select

engine = create_engine('sqlite:///:memory:', echo=True)
metadata = MetaData()

users = Table('users', metadata,
              Column('id', Integer, primary_key=True),
              Column('fullname', String),
              )

addresses = Table('addresses', metadata,
                  Column('id', Integer, primary_key=True),
                  Column('user_id', Integer, ForeignKey('users.id')),
                  Column('email', String(150), nullable=False, index=True)
                  )

metadata.create_all(engine)

if __name__ == '__main__':
    with engine.connect() as conn:
        user = users.insert().values(fullname='Деніс Белоконь')
        result = conn.execute(user)
        print(result.lastrowid)
        all_users = conn.execute(select(users)).fetchall()
        print(all_users)

        address = addresses.insert().values(email='denisua@gmail.com', user_id=result.lastrowid)
        conn.execute(address)
        all_address = conn.execute(select(addresses)).fetchall()
        print(all_address)

        # r = select(users.c.fullname, addresses.c.email).join(addresses)
        r = select(users.c.fullname, addresses.c.email).select_from(users).join(addresses).group_by(users.c.id)
        res = conn.execute(r).fetchall()
        print(res)
