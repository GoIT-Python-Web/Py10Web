from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, func, event
from sqlalchemy.orm import relationship, declarative_base

from database.db import engine

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    login = Column(String(15), unique=True)
    password = Column(String(15))


class Todo(Base):
    __tablename__ = 'todos'
    id = Column('id', Integer, primary_key=True)
    title = Column('title', String(150), nullable=False, index=True)
    description = Column('description', String(150), nullable=False, index=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    user_id = Column('user_id', Integer, ForeignKey('users.id'))
    user = relationship('User')


@event.listens_for(Todo, 'before_update')
def update_updated_at(mapper, conn, target):
    target.title = target.title + ' Test'
    print(target.title)


Base.metadata.create_all(engine)
