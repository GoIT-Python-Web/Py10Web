import pytest
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.database.models import Owner
from src.repository.owners import get_owners, get_owner_by_id, get_owner_by_email, create, update, remove
from src.schemas import OwnerModel

# Setup database for tests
engine = create_engine('sqlite:///:memory:')  # Using in-memory SQLite for simplicity.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Owner.metadata.create_all(bind=engine)


def setup_function(function):
    Owner.metadata.create_all(bind=engine)


def teardown_function(function):
    Owner.metadata.drop_all(bind=engine)


@pytest.mark.asyncio
async def test_get_owners():
    # Arrange
    session = SessionLocal()
    owner1 = Owner(email='test1@example.com')
    owner2 = Owner(email='test2@example.com')
    session.add(owner1)
    session.add(owner2)
    session.commit()

    # Act
    result = await get_owners(session)

    # Assert
    assert len(result) == 2
    session.close()


@pytest.mark.asyncio
async def test_get_owner_by_id():
    # Arrange
    session = SessionLocal()
    owner = Owner(email='test@example.com')
    session.add(owner)
    session.commit()

    # Act
    result = await get_owner_by_id(owner.id, session)

    # Assert
    assert result.id == owner.id
    session.close()


@pytest.mark.asyncio
async def test_get_owner_by_email():
    # Arrange
    session = SessionLocal()
    owner = Owner(email='test@example.com')
    session.add(owner)
    session.commit()

    # Act
    result = await get_owner_by_email(owner.email, session)

    # Assert
    assert result.email == owner.email
    session.close()


@pytest.mark.asyncio
async def test_create():
    # Arrange
    session = SessionLocal()
    owner_model = OwnerModel(email='test@example.com')

    # Act
    result = await create(owner_model, session)

    # Assert
    assert result.email == owner_model.email
    session.close()


@pytest.mark.asyncio
async def test_update():
    # Arrange
    session = SessionLocal()
    owner = Owner(email='test@example.com')
    session.add(owner)
    session.commit()
    owner_model = OwnerModel(email='new_test@example.com')

    # Act
    result = await update(owner.id, owner_model, session)

    # Assert
    assert result.email == owner_model.email
    session.close()


@pytest.mark.asyncio
async def test_remove():
    # Arrange
    session = SessionLocal()
    owner = Owner(email='test@example.com')
    session.add(owner)
    session.commit()

    # Act
    result = await remove(owner.id, session)

    # Assert
    assert result.id == owner.id
    session.close()
