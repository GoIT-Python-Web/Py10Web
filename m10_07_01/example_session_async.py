"""
Async Session
"""
import asyncio

from sqlalchemy import Column, Integer, String, ForeignKey, select
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import relationship, declarative_base

engine = create_async_engine('sqlite+aiosqlite:///:memory:', echo=True)
DBSession = async_sessionmaker(bind=engine, expire_on_commit=False, class_=AsyncSession)

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


async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def main():
    await init_models()

    async with DBSession() as session:
        denis = User(fullname='Деніс Белоконь')
        session.add(denis)
        igor = User(fullname='Igor Omelchenko')
        session.add(igor)
        denis_address = Address(email='denisua@gmail.com', user=denis)
        session.add(denis_address)
        await session.commit()

        users = await session.execute(select(User.id, User.fullname))
        result_user = users.all()
        for u in result_user:
            print(u.id, u.fullname)

        adr = await session.execute(select(Address).join(Address.user))
        result_adr = adr.scalars().all()
        for a in result_adr:
            print(a.id, a.email, a.user.fullname)


if __name__ == '__main__':
    asyncio.run(main())
