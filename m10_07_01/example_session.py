"""
Session
"""

from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import relationship, declarative_base, sessionmaker

engine = create_engine('sqlite:///:memory:', echo=True)
DBSession = sessionmaker(bind=engine)

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    fullname = Column(String)


class Address(Base):
    __tablename__ = 'addresses'
    id = Column('id', Integer, primary_key=True)
    user_id = Column('user_id', Integer, ForeignKey('users.id'))
    email = Column('email', String(150), nullable=False, index=True)
    user = relationship('User')


Base.metadata.create_all(engine)

if __name__ == '__main__':
    session = DBSession()
    denis = User(fullname='Деніс Белоконь')
    session.add(denis)
    igor = User(fullname='Igor Omelchenko')
    session.add(igor)
    # session.commit()
    print(denis.id)
    denis_address = Address(email='denisua@gmail.com', user=denis)
    session.add(denis_address)
    session.commit()

    users = session.query(User.id, User.fullname).all()
    for u in users:
        print(u.id, u.fullname)

    column_names = ["id", "fullname"]
    db = [dict(zip(column_names, (row.id, row.fullname))) for row in users]
    print(db)

    adr = session.query(Address).join(Address.user).all()

    for a in adr:
        print(a.id, a.email, a.user.fullname)

    session.close()
