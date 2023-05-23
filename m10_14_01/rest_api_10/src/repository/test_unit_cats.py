import unittest
from unittest.mock import MagicMock

from sqlalchemy.orm import Session

from src.database.models import Cat, Owner
from src.repository.cats import (
    get_cats,
    create
)
from src.schemas import CatModel


class TestCats(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.session = MagicMock(spec=Session)
        self.owner = Owner(id=1, email="test@test.api.com")

    async def test_get_cats(self):
        cats = [Cat() for _ in range(5)]
        self.session.query(Cat).limit().offset().all.return_value = cats
        result = await get_cats(10, 0, self.session)
        self.assertEqual(result, cats)

    async def test_create(self):
        body = CatModel(
            nick='Barsik',
            age=4,
            vaccinated=False,
            description="Це дуже багато коду",
            owner_id=self.owner.id
        )
        result = await create(body, self.session)
        self.assertEqual(result.nick, body.nick)
        self.assertTrue(hasattr(result, 'id'))
